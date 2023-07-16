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
