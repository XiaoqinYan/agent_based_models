import numpy as np
import random as rnd
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from agent import Agent

class Simulation:
    
    def __init__(self, population, average_degree, network_type):
        """
        network_type has several options, give following network type as string;
            1. lattice
            2. ring
            3. ER-random
            4. Complete (Not recommended!!! Too heavy!!!)
            4. Watts Strogatz(Small World)
            5. BA-SF
        """

        self.network_type = network_type
        self.network = None
        self.agents = self.__generate_agents(population, average_degree)
        self.initial_cooperators = self.__choose_initial_cooperators()

    def __generate_agents(self, population, average_degree):
        if self.network_type == "lattice":
            self.network = self.__generate_lattice(population)
            
        elif self.network_type == "ring":
            self.network = nx.circulant_graph(population, [1])
            
        elif self.network_type == "ER":
            self.network = nx.random_regular_graph(average_degree, population)
        
        elif self.network_type == "Complete":
            self.network = nx.complete_graph(population)
            
        elif self.network_type == "WS":
            self.network = nx.watts_strogatz_graph(population, average_degree, 0.5)
        
        elif self.network_type == "BA-SF":
            rearange_edges = int(average_degree*0.5)
            self.network = nx.barabasi_albert_graph(population, rearange_edges)

        agents = [Agent() for id in range(population)]

        if self.network_type == "lattice":
            n = int(np.sqrt(population))   
            for index, focal in enumerate(agents):
                neighbors_id = list(self.network[int(index//n), int(index%n)])
                for (x,y) in neighbors_id:
                    nb_id = int(x*n+y)
                    focal.neighbors_id.append(nb_id)

        # When using another topology
        else:
            for index, focal in enumerate(agents):
                neighbors_id = list(self.network[index])
                for nb_id in neighbors_id:
                    focal.neighbors_id.append(nb_id)
        
        return agents
