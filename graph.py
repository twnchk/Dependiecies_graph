import os
import random

import networkx as nx
import matplotlib.pyplot as plt
from os import listdir

import sys
import re

current_file_name = sys.argv[0].split('/')[-1]  #return current file name

# ######## Historyjka 1. #########
def extract_filename(file): 
    return file.split(".")[0]  


def get_file_size(file_path): 
    file_path = file_path if file_path.endswith('.py') else './'+file_path+'.py'
    return os.path.getsize(file_path)

def createGraph(path="./"):
    g = nx.DiGraph()  # create direct graph
    files_to_parse = list(filter(lambda f: f.endswith(".py"), listdir(path))) # only python files
    files_to_parse.pop(files_to_parse.index(current_file_name))  # without current file. 
    
    for file_path in files_to_parse:
        g.add_node(extract_filename(file_path)+str(get_file_size(file_path)))
        find_edges_in_file(file_path, g)
    return g

def count_calls(path, module_name): #zliczanie odwołań dla krawędzi
    pattern = re.compile(r'{}\.'.format(module_name)) 
    with open(path, 'r') as f: 
        calls = re.findall(pattern, f.read()) 
        return len(calls) 
    

def find_edges_in_file(file, g): 
    with open(file, 'r') as fr:
        for line in fr: #iteruje po liniach
            if ("import" in line):
                tab = line.split()
                print(tab)
                g.add_edge(
                    extract_filename(file)+str(get_file_size(file)),
                    tab[1]+str(get_file_size(tab[1])),
                    weight=count_calls(file,tab[1])
                )
                
def drawGraph(graph):  #Dominik
    edge_labels = nx.get_edge_attributes(g, "weight")
    pos = nx.spring_layout(g)
    nx.draw(graph, pos=pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(g, pos=pos, edge_labels = edge_labels)
    plt.show()

g = createGraph()
drawGraph(g)

# #### Historyjka nr2 ###########################
def rtrn_python_files(path): #zwraca listę plików .py 
    return list(filter(lambda f: f.endswith(".py"), listdir(path)))

def drawGraph_func(graph): #Dominik
    edge_labels = nx.get_edge_attributes(g, "weight") 
    #node_labels = nx.get_node_attributes(g, "weight") 

    pos = nx.spring_layout(g) 

    nx.draw(graph,pos=pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(g, pos=pos, edge_labels = edge_labels) 

    plt.show() 

def createGraphFunctions(path="./HIS_II/"):
    g = nx.DiGraph()  # create direct graph
    files_to_parse = rtrn_python_files(path)
    #files_to_parse.pop(files_to_parse.index(current_file_name))  # without current file
    funkcje=[] #Tomek
    t_funkcje=[]
    #node'y
    for plik in files_to_parse:
        fs = get_function_names(path+"/"+plik)
        funkcje += fs
        t_funkcje = fs
        for name in t_funkcje:

            
def get_function_names(path): #function names from file. Tomek
   names = []
   with open(path, 'r') as fr:
       for line in fr:
           if re.match(r"^\s*?def", line):
               n = line.split(" ")[1].split("(")[0] 
               names.append(n)
   print(names)
   return names
