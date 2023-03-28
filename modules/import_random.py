import random
from urllib.response import addinfo

from modules.open_digraph import open_digraph

def random_int_list(n, bound):
    l = []
    for _ in range(n):
        l.append(random.randint(0,bound))
    return l

def affiche(m):
    for i in range(len(m)):
        print(m[i])

def random_int_matrix(n, bound,null_diag=True):
    l = []
    for _ in range(n):
        m = random_int_list(n, bound)
        l.append(m)
    if null_diag:
        for i in range(n):
            l[i][i] = 0
    return l


def random_symetric_int_matrix(n, bound, null_diag=True):
    l = random_int_matrix(n,bound)
    for i in range (0,n):
        for j in range (0,n):
            if i !=j : 
                l[i][j]=l[j][i]
    return l
        
def random_oriented_int_matrix(n, bound, null_diag=True):
    l = random_int_matrix(n,bound)
    for i in range(len(l)):
        for j in range (len(l)):
            if l[i][j] != 0 and l[j][i] != 0 and i != j:
                p = random.randint(0,1)
                if p == 0:
                    l[j][i] = 0
                else :
                    l[i][j] = 0
    return l

def random_triangular_int_matrix(n, bound, null_diag=True):
    l = random_int_matrix(n,bound)
    for i in range(len(l)):
        for j in range (len(l)):
            if i > j:
                l[i][j] = 0
    return l

#Exercice 7


def graph_from_adjacency_matrix(l):
    G = open_digraph.empty()
    for i in range(len(l)):
        G.add_node("n" + str(i),{},{})
    for j in range (len(l)):
        for k in range (len(l)):
            if l[j][k] != 0:
                for _ in range(l[j][k]):
                    G.get_node_by_id(j).add_child_id(k)
                    G.get_node_by_id(k).add_parent_id(j)
    return G



@classmethod
def Random(n, bound, inputs=0, outputs=0, form="free"):

    ''' Doc Bien pr ́eciser ici les options possibles pour form ! '''
    
    if form=="free":
        resultat = graph_from_adjacency_matrix(random_int_matrix(n, bound, True))
        if not(resultat.is_well_formed()):
             raise RuntimeError("Le graphe généré est incorrect.")
        return resultat 

    elif form=="DAG":
         
        resultat = graph_from_adjacency_matrix(random_triangular_int_matrix(n, bound,True))
        if not(resultat.is_well_formed()):
             raise RuntimeError("Le graphe généré est incorrect.")
        return resultat 
         
    elif form=="oriented":
         
        resultat = graph_from_adjacency_matrix(random_oriented_int_matrix(n, bound, True)) 
        if not(resultat.is_well_formed()):
             raise RuntimeError("Le graphe généré est incorrect.")
        return resultat 


    elif form=="loop-free":

        resultat = graph_from_adjacency_matrix(random_int_matrix(n, bound, False))
        if not(resultat.is_well_formed()):
             raise RuntimeError("Le graphe généré est incorrect.")
        return resultat 


    elif form=="undirected":

        resultat = graph_from_adjacency_matrix(random_symetric_int_matrix(n, bound, True)) 
        if not(resultat.is_well_formed()):
            raise RuntimeError("Le graphe généré est incorrect.")
        return resultat 

    elif form=="loop-free undirected":

        resultat = graph_from_adjacency_matrix(random_symetric_int_matrix(n, bound, False))
        if not(resultat.is_well_formed()):
             raise RuntimeError("Le graphe généré est incorrect.")
        return resultat 


    