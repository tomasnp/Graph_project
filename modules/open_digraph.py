from lib2to3.refactor import get_all_fix_names
#import random_int_matrix
import webbrowser
import itertools

from modules.node import *
from modules.open_digraph_affich_save import *
from modules.chemins import *


class open_digraph(open_digraph_affich_save, chemins): # for open directed graph
    
    def __init__(self, inputs, outputs, nodes): 
        self.inputs = inputs
        self.outputs = outputs
        self.nodes = {node.id:node for node in nodes} # self.nodes: <int,node> dict

    def __str__(self):
        for node in self.nodes:
           return (self.nodes.__str__())

    def __repr__(self):
        for node in self.nodes:
            return (self.nodes.__repr__())


    @classmethod
    def empty(cls):
        return cls([], [], [])

    def copy(self):
        noeuds = []
        for n in self.nodes.values():
            noeuds.append(n.copy())
        return open_digraph(self.inputs.copy(), self.outputs.copy(), noeuds)

    def new_id(self):
        
        for i in self.get_node_ids():
            if self.nodes[i] == None:
                return i
        return len(self.nodes)

    def add_edge(self, src, tgt):
        a =  self.get_node_by_id(src) 
        if tgt in a.children.keys():
            a.children[tgt] = a.children[tgt] + 1
        else:
            a.children[tgt] = 1
        b = self.get_node_by_id(tgt)
        if src in b.parents.keys():
            b.parents[src] = b.parents[src] + 1
        else:
            b.parents[src] = 1

    def add_node(self, label, parents, children):
        Id = self.new_id()
        self.nodes[Id] = node(Id, label, {}, {})
        for i in parents:
            self.add_edge(i, Id)
        for j in children:
            self.add_edge(Id, j)
        return Id
#getters
    def get_input_ids(self):
        return self.inputs
    
    def get_output_ids(self):
        return self.outputs

    def get_id_node_map(self):
        return self.nodes
    
    def get_nodes(self):
        a = []
        for i in self.nodes:
            a.append(self.nodes[i])
        return a
    
    def get_node_ids(self):
        a = []
        for i in self.nodes:
            a.append(i)
        return a

    def get_node_by_id(self, ident):
        for node in self.nodes:
            if self.nodes[node].id == ident:
                return self.nodes[node]
    
    def get_nodes_by_ids(self, ids_list):
        a = []
        for i in ids_list:
            a.append(self.get_node_by_id(i))
        return a

#setters
    def set_input_ids(self, ids_list):
        self.inputs = ids_list
    
    def set_output_ids(self, ids_list):
        self.outputs = ids_list
    
    def add_input_id(self, id):
        self.inputs.append(id)

    def add_output_id(self, id):
        self.inputs.append(id)


    def remove_edge(self, src, tgt):
        self.get_node_by_id(src).remove_child_once(tgt)
        self.get_node_by_id(tgt).remove_parent_once(src)

    def remove_parallel_edges(self, src, tgt):
        self.get_node_by_id(src).remove_child_id(tgt)
        self.get_node_by_id(tgt).remove_parent_id(src)

    def remove_node_by_id(self, id):
        temp1 = list(self.get_node_by_id(id).parents.keys())
        for i in (temp1) :
            self.get_node_by_id(i).remove_child_id(id)
            self.get_node_by_id(id).remove_parent_id(i)

        temp2 = list(self.get_node_by_id(id).children.keys())
        for i in (temp2) :
            self.get_node_by_id(i).remove_parent_id(id)
            self.get_node_by_id(id).remove_child_id(i)

        self.nodes.pop(id)
    
    #Exercice 4
    def add_input_node(self, self_id, child_id):
        nouveau = node(self_id, '',{} , {child_id:1})
        self.inputs.append(self_id)
        self.get_node_by_id(child_id).add_parent_id(self_id)
        self.nodes[self_id] = nouveau

        if child_id in self.inputs : 
            self.inputs.remove(child_id)

    def add_output_node(self, self_id, parent_id):
        nouveau = node(self_id, '',{parent_id:1}, {})
        self.outputs.append(self_id)
        self.get_node_by_id(parent_id).add_child_id(self_id)
        self.nodes[self_id] = nouveau

        if parent_id in self.outputs : 
            self.outputs.remove(parent_id)
    
    def is_well_formed(self):
        for i in self.inputs:
           if i not in self.nodes.keys() or len((self.get_node_by_id(i)).get_children_ids()) != 1 or len((self.get_node_by_id(i)).get_parent_ids()) != 0:
                return False
                
        for j in self.outputs:
            if j not in self.nodes.keys() or len((self.get_node_by_id(j)).get_parent_ids()) != 1 or len((self.get_node_by_id(j)).get_children_ids()) != 0:
                return False

        for i in self.nodes.keys():
            if i != self.nodes[i].id:
                return False
        for k in self.nodes.keys() :
            for i in self.get_node_by_id(k).parents.keys() :
                if self.get_node_by_id(k).parents[i] != self.get_node_by_id(i).children[k] :
                    return False
        return True


    def method(self):
        a = {}
        j = 0
        for i in self.nodes.keys():
            a[i] = j
            j = j + 1
        return a    


    def adjacency_matrix(self):

        #On initie notre matrice d'adjacence avec random_int_matrix(len(self.nodes), 0) qui génére des matrice carrés avec
        #des éléments entre 0 et 0 et qui est de taille 'nombre de noeuds' * 'nombre de noeuds'

        matrice = ()
        #matrice = random_int_matrix(len(self.nodes), 0)

        #On parcourt ensuite tous les noeuds du graphe via le dictionnaire nodes et on rentre dans chaque noeud

        for valeur in self.nodes.values() :

            #entrée des indices de 'parents'

            for indice in valeur.parents.keys():
                matrice[indice][valeur.id] = valeur.parents[indice]

            #entrée des indices de 'children'    

            for indice in valeur.children.keys():
                matrice[valeur.id][indice] = valeur.children[indice]    

        return matrice


    #Méthode d'enregistrement 
    #Exercice 1 TD4

    
    # min_id() et max_id() renvoient respectivement l’indice min et l’indice max des noeuds du graphe.

    def min_id(self):
        ids = self.get_node_ids()
        a = ids[0]
        for n in ids:
            if n <= a:
                a = n
        return a

    def max_id(self):
        ids = self.get_node_ids()
        a = ids[0]
        for n in ids:
            if n >= a:
                a = n
        return a    

    #shift_indices(self, n) ajoute n à tous les indices (de chaque noeud) du graphe  

    def shift_indices(self,n):
        
        #On déclare le futur nouveau dictionnaire de noeuds
        nvDic = {}

        #On parcourt chaque noeud du dictionnaire de noeuds actuel
        for i in self.nodes.values() :

            #On incrémente de n l'id du noeud    
            i.id += n 
            
            #On fait une copie du dictionnaire des parent du noeud 
            # (pour éviter une boule infinie). On parcourt ses clés 
            dicParent = i.parents.copy()
            for j in dicParent.keys() :
                
                #Pour chaque clés j, on crée un nouvel élément à la clé j + n 
                # auquel on associe ala valeur qui est à la clé j.
                # On supprime ensuite l'élément à la clé j

                i.parents[j+n] = i.parents[j]
                i.parents.pop(j)
                
            #Même raisonnement avec le dictionnaire des enfants    
            dicChild = i.children.copy()
            for j in dicChild.keys() :
                i.children[j+n] = i.children[j]
                i.children.pop(j)


            #Enfin, on ajoute au futur nouveau dictionnaire, le noeud i
            # avec comme clé sont nouvel id
            nvDic[i.id] = i

        #Au passage, on incremente de n toute la liste d'inputs et d'outputs
        for i in range(0,len(self.inputs)) :
            self.inputs[i] += n
        
        for i in range(0,len(self.outputs)) :
            self.outputs[i] += n

        
        #Pour conclure, on fait pointer self.nodes vers le futur nouveau noeud 
        # qui devient enfin le nouveau noeud
        self.nodes = nvDic

    def iparallel(self, liste_g):
        for g in liste_g:
            if g.min_id() <= self.max_id():
                g.shift_indices(self.max_id() - g.min_id() + 1)
            for n in g.nodes.values():
                #self.add_node(n.label, n.parents, n.children)
                self.nodes[n.get_id()] = node(n.get_id(), n.label, n.parents, n.children)
            for i in g.get_input_ids():
                a = g.get_node_by_id(i)
                b = a.get_children_ids()
                self.add_input_node(i, b[0])
            for j in g.get_output_ids():
                c = g.get_node_by_id(j)
                d = c.get_parent_ids()
                self.add_output_node(j, d[0])

    def parallel(self, liste_g):
        G = self.copy()
        for g in liste_g:
            G.iparallel(g) 
        return G    
                

    #icompose(self, g) fait la composition séquentielle de self et g (les entrées de self devront être reliées aux sorties de g). 
    #On lance une exception dans le cas où les nombres d’entrées (de self) et de sorties (de g) ne coîncident pas.

    def icompose(self, g):

        #On regarde d'abord si les nombres d’entrées (de self) et de sorties (de g) coïncident.

        if (len(self.inputs) != len(g.outputs)) :
            raise IndexError("Le nombre d'entrees et de sorties ne correspond pas.")

        #On s'assure ensuite d'avoir des ids distincts pour tous les noeuds du futur graphe    

        m = max(self.min_id(), g.min_id())
        M = min(self.max_id(), g.max_id())

        if m == self.min_id() : 
            self.shift_indices(M-m+1)
        else : 
            g.shift_indices(M-m+1)

        #On parcourt la liste des outputs de g et on les lient aux inputs de self et inversement 

        #Pour ne pas avoir à parcourir le dictionnaire des noeuds de g plusieurs fois, on définie cpt qu'on décrementera et un i 
        # qu'on incrementera.

        cpt = len(g.outputs)
        i = 0

        #On parcourt le dictionnaire des noeuds de g
        for j in g.nodes.values() : 

            #Pour chacun des noeuds, on regarde si l'id de celui ci correspond à l'id d'indice i de la liste des outputs de g
            if j.id == g.outputs[i] :
                
                #Si c'est le cas, on "sauvegarde" (pointe vers) l'id de l'input d'indice i de la liste des inputs de self 
                # et on "sauvegarde" (pointe) l'input en question (pour optimiser)

                inputId = self.inputs[i]
                input = self.get_node_by_id(inputId)

                #Dans le dictionnaire des enfants de notre output courant (qui est à la base vide), on ajoute l'input sauvegardé
                # avec comme comme clé la clé de cet input. On fait ensuite lel lien inverse depuis le dictionnaire des parents de 
                #l'input.


                j.children[inputId] = 1
                input.parents[j.id] = 1

                #On incrémente i de 1 et décrémente cpt de 1 pour pouvoir parcourir convenablement 
                i +=1 
                cpt -= 1

            if cpt == 0 : break    

        #Enfin, on met la liste des outputs de g et la liste des inputs de self à vide

        g.outputs = []
        self.inputs = []


    #compose(g) renvoie une composée de self et de g (sans les modifier)
    def compose(self, g): 

        #On copie les deux graphes pour ne pas modifier les originaux
        copieSelf = self.copy()
        gCopie = g.copy()

        #On compose les deux copies (c'est-à-dire qu'on crée les liens entre eux)
        copieSelf.icompose(gCopie)
        
        #on crée une liste d'outputs et une liste d'inputs en concatenant les listes respectives des
        # deux copies et on remplie la nouvelle liste de noeuds composée des noeuds des deux graphes

        inputs = copieSelf.inputs+gCopie.inputs
        outputs = copieSelf.outputs+gCopie.outputs
        noeuds = []

        for n in copieSelf.nodes.values():
            noeuds.append(n)

        for n in gCopie.nodes.values():
            noeuds.append(n)

        #On crée ensuite un nouveau graphe (à l'aide de ces trois nouvelles listes) que l'on retourne
        res = open_digraph(inputs, outputs, noeuds)

        return res

    #fonction annexe 

    def calcul_cc(self, noeud, dic, acc):
        dic[noeud.id] = acc

        for p in noeud.parents.keys() :
            if dic[p] == - 1:
                self.calcul_cc(self.nodes[p], dic, acc)

        for c in noeud.children.keys() :
            if dic[c] == -1:
                self.calcul_cc(self.nodes[c], dic, acc)

    # connected_components(self) renvoie un couple composé
    # du nombre de composantes connexes et d'un dictionnaire qui associe à chaque id de noeuds du graphe un int qui correspond à une composante connexe.
    # On utilise la fonction annexe calcul_cc (pour la récursivité) que l'on a défini plus haut
    def connected_components(self):
        
        #Déclaration du compteur de cc, et du dictionnaire
        acc = 0
        dic = {}

        #On déclare dans le dictionnaire chaque noeud de self à -1 (par convention) ce qui signifie qu'ils n'ont pas étés parcourus pour l'instant et qu'on ne sait pas à quelle 
        # composante ils appartiennent
        for i in self.nodes.keys():
            dic[i] = -1

        #On parcourt ensuite chaque noeud ... JE COMPLETERAI LA DOC PLUS TARD
        for i in self.nodes.items():

            if dic[i[0]] == -1 :
                self.calcul_cc(i[1],dic ,acc)
                acc+=1
                        

        return (acc, dic)

    # EX6 TD6
    # broke_in_cc(self) renvoie une liste d’open_digraphs, chacun correspondant `a une composante connexe de self

    def broke_in_cc(self):

        """
        broke_in_cc(self) renvoie une liste d’open_digraphs, chacun correspondant `a une composante connexe de self

        Paramètres : 

        self(open_digraph) : le graphe sur lequel on fait la recherche du plus court chemin


        """

        #On sauve le resultat de self.connected_components()
        cc = self.connected_components()

        #La future liste de graphes
        res = []

        #La liste de liste de noeuds, l'indice de chaque liste correspond à l'indice de la comopsante
        ll = []

        #initiation de la liste de listes
        for i in range(0,cc[0]):
            l = []
            ll.append(l)
        
        #Parcours du dict de cc, on ajoute nodes à la liste d'indice indiceDeComposante dans la liste de liste
        for i in cc[1].items():
            ll[i[1]].append(self.nodes[i[0]])

        #Parcours de la liste de listes, pour chacune des listes, création d'un nouveau graphe avc la liste courante en node
        # et on ajoute ce nv graphe à res qui sera le resultat 
        for i in ll :
            g = open_digraph([],[],i)
            res.append(g)

        return res  

    def fusionnoeuds(self, id1, id2):
        n2 = self.get_node_by_id(id2)
        for c in n2.get_children_ids():
            if(c != id1):
                for i in range(n2.children[c]):
                    self.add_edge(id1, c)
        for d in n2.get_parent_ids():
            if(d != id1):
                for i in range(n2.parents[d]):
                    self.add_edge(d, id1)
        self.remove_node_by_id(id2)



          



    

    




