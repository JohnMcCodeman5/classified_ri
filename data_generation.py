import random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def generate_random_graph(num_nodes, probability):
    graph = [[0] * num_nodes for _ in range(num_nodes)]
    
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() < probability:
                graph[i][j] = 1
                graph[j][i] = 1

    return graph



def generate_random_solution(num_nodes):
    nodes = list(range(num_nodes))
    random.shuffle(nodes)
    return nodes



def calculate_total_edge_length(graph, solution):
    total_length = 0
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] == 1:
                position_i = solution.index(i)
                position_j = solution.index(j)
                total_length += abs(position_i - position_j)
    return total_length



def write_instance(graph, solution, value, filename):
    with open(filename, 'w') as f:
        #f.write('graph\n')
        n = len(graph)
        for i in range(n):
            for j in range(n):
                f.write(f'{str(graph[i][j])} ')
            f.write('\n')    

        #f.write('solution\n')
        n = len(solution)
        for i in range(n):  
            f.write(f'{str(solution[i])} ')

        f.write('\n')
        #f.write('value\n')
        f.write(f'{str(value)}')




def read_instance(filename):
    n = int((str(filename).split('.')[-2].split('a')[-1]))
    graph = [[0 for _ in range(n)] for _ in range(n)]
    solution = [0 for _ in range(n)]

    with open(filename, 'r') as f:
        for i in range(n):
            row = f.readline()
            row = row.split()
            for j in range(n):
                graph[i][j] = int(row[j])

        sol_tmp = f.readline().split()
        for i, s in enumerate(sol_tmp):
            solution[i] = int(s)
        
        value = int(f.readline())
        
        return graph, solution, value




def generate_data_files():
    edge_probability = 0.5
    dims = [5, 8, 10, 11, 15, 20, 30, 50, 70]

    for i in dims:
        num_nodes = i

        graph = generate_random_graph(num_nodes, edge_probability)

        random_solution = generate_random_solution(num_nodes)

        total_edge_length = calculate_total_edge_length(graph, random_solution)

        filename = 'data\data' + str(num_nodes) + '.txt'

        write_instance(graph, random_solution, total_edge_length, filename)

        #print("Random Graph (Adjacency Matrix):")
        #for row in graph:
        #    print(row)

        #print("\nRandom Solution (Permutation):", random_solution)
        #print("Total Edge Length:", total_edge_length)


generate_data_files()
#read_instance('data\data5.txt')