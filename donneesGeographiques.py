# Chargement des librairies Pandas, Networkx et folium
from networkx.classes.function import set_node_attributes
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import csv
import folium

# %matplotlib inline

############################################## PARTIE 1 ##############################################

# Utilisation de la bibliothéque pandas pour lire le fichier transport-nodes.csv

transportNodes = pd.read_csv(r"C:/Users/Mrs GUEYE/Documents/POO2/PROJET2_POO2/transport-nodes.csv")
print(transportNodes)

# Utilisation de la bibliothéque pandas pour lire le fichier transport-relationships.csv

transportRelationships = pd.read_csv(r"C:/Users/Mrs GUEYE/Documents/POO2/PROJET2_POO2/transport-relationships.csv")
print(transportRelationships)

# Construction du graphe et le visualiser avec la fonction from_pandas_dataframe de networkx
# Cette dernière étant obsolète, on utilise la fonction from_pandas_edgelist de la même bibliothèque

with open("C:/Users/Mrs GUEYE/Documents/POO2/PROJET2_POO2/transport-nodes.csv") as f:
    csv_list = [[val.strip() for val in r.split(",")] for r in f.readlines()]
del csv_list[0]
cles = []
valeurs = []
for minList in csv_list :
    cles.append(str(minList[0]))
    posList = [float(minList[1]), float(minList[2])]
    valeurs.append(posList)

pos = dict(zip(cles, valeurs))

G = nx.Graph()

df = pd.read_csv("C:/Users/Mrs GUEYE/Documents/POO2/PROJET2_POO2/transport-relationships.csv")

G = nx.from_pandas_edgelist(df, source = 'src', target = 'dst', edge_attr = True)

print(dict(G.nodes.data()))

nx.draw_networkx(G, pos = pos, with_labels = True, edge_color = 'red', node_color = 'yellow')
plt.show()

# Ajout des attributs longitude et latitude aux noeuds avec Networkx en utilisant :
# - le dictionnaire "node" de networkx qui contient les noeuds
# - le dataframe transport-nodes defini plus haut

def ajouterAttribut(myGraph, dfnode, nameAttr, index):
    keys = []
    values = []
    i = 0
    for minList in csv_list :
        if nameAttr == 'latitude' :
            values.append(float(minList[1]))
            keys.append('latitude' + str(i))
        elif nameAttr == 'longitude' :
            values.append(float(minList[2]))
            keys.append('longitude' + str(i))
        else :
            values.append(float(minList[3]))
            keys.append('population' + str(i))
        i += 1
    value = dict(zip(keys, values))
    print(value)
    nx.set_node_attributes(myGraph, value)
    print(dict(G.nodes.data()))
    
ajouterAttribut(G, transportNodes, 'latitude', 'id')
ajouterAttribut(G, transportNodes, 'longitude', 'id')
ajouterAttribut(G, transportNodes, 'population', 'id')

# Représentation des noeuds sur une carte avec Folium
# On met en place d'abord le fond de la carte