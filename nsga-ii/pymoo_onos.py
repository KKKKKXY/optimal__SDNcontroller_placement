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
# graph = {
#     0: {2: 54},
#     1: {2: 68},
#     2: {0: 54, 1: 68}
# }

graph = {
    0: {2: 82.99458278043693, 3: 38.0311153294585 },
    1: {5: 71.39569502299298, 6: 164.82129372183246, 7: 125.12889341007268},
    2: {0: 82.99458278043693, 9: 44.40532335578192, 14: 60.085872515938526},
    3: {0: 38.0311153294585},
    4: {17: 40.94078297191167, 5: 73.00240078651599, 6: 39.63429170218247, 7:82.63755970844781},
    5: {1: 71.39569502299298, 4: 73.00240078651599},
    6: {1: 164.82129372183246, 4: 39.63429170218247, 8: 82.95757267021366},
    7: {1: 125.12889341007268, 4: 82.63755970844781},
    8: {6: 82.95757267021366, 16: 128.55298324149916, 17: 69.60040685366947, 15: 80.63749756519596},
    9: {2: 44.40532335578192, 17: 53.8990046198166, 13: 66.0212258943215, 15: 165.44426544490818},
    10: {11: 124.27954969591543, 15: 93.02721253398369},
    11: {10: 124.27954969591543, 17: 97.37414158154495, 12: 56.22293094713925, 15: 38.90792597867574},
    12: {11: 56.22293094713925, 13: 34.37094579691975, 14: 50.643929335722085, 15: 94.00634375520872},
    13: {9: 66.02122589432157, 12: 34.37094579691975, 14: 16.37608707101773},
    14: {2: 60.085872515938526, 12: 50.643929335722085, 13: 16.376087071017736, 17: 5.745325757683184, 15: 134.60231940716625},
    15: {8: 80.63749756519596, 9: 165.44426544490818, 10: 93.02721253398369, 11: 38.90792597867574, 12: 94.00634375520872, 14: 134.60231940716625, 16: 63.939794628835195, 17: 135.54764213855776},
    16: {8: 128.55298324149916, 15: 63.939794628835195},
    17: {4: 40.94078297191167, 8: 69.60040685366947, 9: 53.8990046198166, 11: 97.3741415815449, 14: 5.745325757683184, 15: 135.54764213855776},
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

    # calculate average delay to atomix nodes from each controller
    average_atomix_delay_from = {}
    for c in controller_list:
        delay = []
        for a in atomix_list:
            delay.append(distance_matrix[c][a])
        average_atomix_delay_from[c] = np.mean(delay)

    # find the nearest atomix for each atomix and calculate average delay
    atomix_atomix_delays = []
    for a1 in atomix_list:
        delay = math.inf
        for a2 in atomix_list:
            if(a1 == a2):
                continue
            if distance_matrix[a1][a2] < delay:
                delay = distance_matrix[a1][a2]
        atomix_atomix_delays.append(delay)
    average_atomix_atomix_delay = np.mean(atomix_atomix_delays)

    FTSs = []
    for source in range(num_nodes):
        for distination in range(num_nodes):
            delay = 0
            is_controlled_by_single_controller = True
            counted_controllers = []
            for s in shortest_paths[source][distination]:
                # switch-controller delay
                delay += distance_matrix[s][controller_of[s]] * 4
                # controller-atomix delay
                if(s == source):
                    delay += average_atomix_delay_from[controller_of[s]] * 2
                elif(s != distination):
                    if(controller_of[s] != controller_of[source]):
                        is_controlled_by_single_controller = False
                        if(not controller_of[s] in counted_controllers):
                            counted_controllers.append(controller_of[s])
                            delay += average_atomix_delay_from[controller_of[s]]
                else:
                    if(controller_of[s] == controller_of[source]):
                        if(not is_controlled_by_single_controller):
                            delay += average_atomix_delay_from[controller_of[s]]
                    else:
                        delay += average_atomix_delay_from[controller_of[s]] * 2
            # atomix-atomix delay
            delay +=  average_atomix_atomix_delay * 2
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
                      seed=1,
                      eliminate_duplicates=True)
    res = minimize(problem,
               algorithm,
               ('n_gen', 100),
               save_history=True,
               verbose=True)

if __name__ == "__main__":
    main()
