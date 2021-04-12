import networkx as nx
import random
import utils
import parse
import os

Vertex_Number_Small = 30
Vertex_Number_Medium = 50
Vertex_Number_Large = 100

Max_Decimal_Place = 3
Max_Upper_Bound = 100


def build_graph(vertexNum):
    graph = nx.Graph()
    graph.to_undirected()
    graph.add_nodes_from([i for i in range(vertexNum)])
    graph.add_weighted_edges_from(
        [(v1, v2, random.randint(0, Max_Upper_Bound * (10 ** Max_Decimal_Place)) / (10 ** Max_Decimal_Place)) \
         for v1 in range(0, vertexNum - 1) for v2 in range(v1 + 1, vertexNum)])
    return graph

def generate():
    try:
        os.mkdir("./inputs/")
        print("New inputs generated.")
    except:
        print("New inputs updated.")
    parse.write_input_file(build_graph(Vertex_Number_Small), "inputs/30.in")
    parse.write_input_file(build_graph(Vertex_Number_Medium), "inputs/50.in")
    parse.write_input_file(build_graph(Vertex_Number_Large), "inputs/100.in")

