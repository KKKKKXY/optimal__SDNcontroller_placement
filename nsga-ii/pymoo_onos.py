#!/usr/bin/env python
import numpy as np
import networkx as nx
import math
from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.operators.crossover.pntx import TwoPointCrossover
from pymoo.operators.mutation.bitflip import BitflipMutation
from pymoo.operators.sampling.rnd import BinaryRandomSampling
from pymoo.optimize import minimize

# Node ID should start from 0
graph = {
    0: {2: 54},
    1: {2: 68},
    2: {0: 54, 1: 68}
}

# graph = {
#     1: {3: 82.99458278043693, 4: 38.0311153294585 },
#     2: {6: 71.39569502299298, 7: 164.82129372183246, 8: 125.12889341007268},
#     3: {1: 82.99458278043693, 10: 44.40532335578192, 15: 60.085872515938526},
#     4: {1: 38.0311153294585},
#     5: {18: 40.94078297191167, 6: 73.00240078651599, 7: 39.63429170218247, 8:82.63755970844781},
#     6: {2: 71.39569502299298, 5: 73.00240078651599},
#     7: {2: 164.82129372183246, 5: 39.63429170218247, 9: 82.95757267021366},
#     8: {2: 125.12889341007268, 5: 82.63755970844781},
#     9: {7: 82.95757267021366, 17: 128.55298324149916, 18: 69.60040685366947, 16: 80.63749756519596},
#     10: {3: 44.40532335578192, 18: 53.8990046198166, 14: 66.0212258943215, 16: 165.44426544490818},
#     11: {12: 124.27954969591543, 16: 93.02721253398369},
#     12: {11: 124.27954969591543, 18: 97.37414158154495, 13: 56.22293094713925, 16: 38.90792597867574},
#     13: {12: 56.22293094713925, 14: 34.37094579691975, 15: 50.643929335722085, 16: 94.00634375520872},
#     14: {10: 66.02122589432157, 13: 34.37094579691975, 15: 16.37608707101773},
#     15: {3: 60.085872515938526, 13: 50.643929335722085, 14: 16.376087071017736, 18: 5.745325757683184, 16: 134.60231940716625},
#     16: {9: 80.63749756519596, 10: 165.44426544490818, 11: 93.02721253398369, 12: 38.90792597867574, 13: 94.00634375520872, 15: 134.60231940716625, 17: 63.939794628835195, 18: 135.54764213855776},
#     17: {9: 128.55298324149916, 16: 63.939794628835195},
#     18: {5: 40.94078297191167, 9: 69.60040685366947, 10: 53.8990046198166, 12: 97.3741415815449, 15: 5.745325757683184, 16: 135.54764213855776},
# }

config = {
    "half_pop_size" : 20,
    "problem_dim" : 1,
    "gene_min_val" : 2,
    "gene_max_val" : 18,
    "mutation_power_ratio" : 1.05,
}

class ONOSControllerPlacement(ElementwiseProblem):
    def __init__(self, num_nodes, distance_matrix, shortest_paths):
        super().__init__(n_var=2*num_nodes, 
                         n_obj=3, 
                         n_constr=2, 
                         xl=0, xu=1)
        self.num_nodes = num_nodes
        self.distance_matrix = distance_matrix
        self.shortest_paths = shortest_paths
    
    def _evaluate(self, x, out, *args, **kwargs):
        controller_nodes = x[:self.num_nodes]   # first half is controller placement
        atomix_nodes = x[self.num_nodes:]       # second half is atomix placement

        num_controller = np.sum(controller_nodes)
        num_atomix = np.sum(atomix_nodes)

        # Obj1: Minimize number of contrtoller
        f1 = num_controller

        # Obj2: Minimize number of atomix
        f2 = num_atomix

        # Obj3: Minimize average FSP
        f3 = calculate_FST(self.num_nodes, 
                           controller_nodes, 
                           atomix_nodes, 
                           self.distance_matrix, 
                           self.shortest_paths)

        # Constr1: The number of controller is equal to or greater than 2
        g1 = 2 - num_controller

        # Constr1: The number of atomix is equal to or greater than 3
        g2 = 3 - num_atomix

        out["F"] = [f1, f2, f3]
        out["G"] = [g1, g2]


def calculate_FST(num_nodes, controller_nodes, atomix_nodes, distance_matrix, shortest_paths):
    num_controller = np.sum(controller_nodes)
    num_atomix = np.sum(atomix_nodes)
    controller_list = np.nonzero(controller_nodes)[0].tolist()
    atomix_list = np.nonzero(atomix_nodes)[0].tolist()

    if(num_controller == 0 or num_atomix ==0):
        return math.inf

    # calculate avarage delay between controllers and atomix nodes
    controller_atomix_delays = []
    for c in controller_list:
        for a in atomix_list:
            controller_atomix_delays.append(distance_matrix[c][a])
    average_controller_atomix_delay = np.mean(controller_atomix_delays)

    # find the nearest controller for each switch
    controller_of = []
    for s in range(num_nodes):
        delay = math.inf
        nearest_controller = None
        for c in controller_list:
            if distance_matrix[s][c] < delay:
                delay = distance_matrix[s][c]
                nearest_controller = c
        controller_of.append(nearest_controller)

    FTSs = []
    for source in range(num_nodes):
        for distination in range(num_nodes):
            # TODO: need to fix based on the latest model design
            delay = distance_matrix[source][distination] * 2
            delay += distance_matrix[source][controller_of[source]] * 4
            delay += distance_matrix[distination][controller_of[distination]] * 4
            delay +=  average_controller_atomix_delay * 3
        FTSs.append(delay)

    return np.mean(FTSs)

def calc_distance_matrix(graph):
    G = nx.Graph()
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(vertex, neighbor, weight=weight)
    distance_matrix = dict(nx.all_pairs_dijkstra_path_length(G))
    shortest_paths = dict(nx.all_pairs_dijkstra_path(G))

    return distance_matrix, shortest_paths

def main():
    num_nodes = len(graph)
    distance_matrix, shortest_paths = calc_distance_matrix(graph)


    problem = ONOSControllerPlacement(num_nodes, distance_matrix, shortest_paths)
    algorithm = NSGA2(pop_size=100,
                      sampling=BinaryRandomSampling(),
                      crossover=TwoPointCrossover(),
                      mutation=BitflipMutation(),
                      eliminate_duplicates=True)
    res = minimize(problem,
               algorithm,
               ('n_gen', 100),
               save_history=True,
               verbose=True)

if __name__ == "__main__":
    main()
