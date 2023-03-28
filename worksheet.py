#from crypt import methods
import inspect
from modules.open_digraph import *
from modules.bool_circ import * 

n0 = node(0, 'a', {3:1, 4:1}, {1:1, 2:1})
n1 = node(1, 'b', {0:1}, {2:2, 5:1})
n2 = node(2, 'c', {0:1, 1:2}, {6:1})
i0 = node(3, 'i0', {}, {0:1})
i1 = node(4, 'i1', {}, {0:1})
o0 = node(5, 'o0', {1:1}, {})
o1 = node(6, 'o1', {2:1}, {})

n3 = node(1, 'e', {4:1, 5:1}, {2:1, 3:1})
n4 = node(2, 'f', {1:1}, {3:2, 6:1})
n5 = node(3, 'g', {1:1, 2:2}, {7:1})
i2 = node(4, 'i2', {}, {1:1})
i3 = node(5, 'i3', {}, {1:1})
o2 = node(6, 'o2', {2:1}, {})
o3 = node(7, 'o3', {3:1}, {})


G = open_digraph([3,4], [5,6], [n0,n1,n2,i0,i1,o0,o1])
G1 = open_digraph([4,5], [6,7], [n3,n4,n5,i2,i3,o2,o3])


#s = "((x0)&((x1)&(x2)))|((x1)&(~(x2)))"
#B = bool_circ.parse_parentheses(s)
#print(B)

#G.fusionnoeuds(0, 1)

#B = bool_circ.genergraphe(4, 2, 4)
#C = bool_circ.genergraphe2(4, 4, 6)
#B.save_as_dot_file("testFichier.dot", True)

#A = bool_circ.viaTable('0100')

#A.save_as_dot_file("testFichier.dot", True)
#a = "01000"
#b = "01011"
#c = bool_circ.Half_Adder(a, b)
#print(c)

#Bin = bool_circ.graphbinaire(26)
#Bin.save_as_dot_file("testFichier.dot", True)
#gg = G.parallel([G1])

h = bool_circ.encodeur()
h.save_as_dot_file("testFichier.dot", True)
#print(gg.connected_components())
#gg = G.iparallel(G1)
#print(G.broke_in_cc())
#print(" \n \n")
#print(G)
#print(G.connected_components())


#G1.save_as_dot_file("testFichier1.dot", False)
#print(G.copy())
#nv = G.compose(G1)
#print(nv.le_plus_long(8,0))
#print(nv.Dijkstra(src = 7,tgt = 2))
#print(G.shortest_path(3,5))
#nv.save_as_dot_file("testFichierF.dot", True)
#G1.save_as_dot_file("testFichier1F.dot", False)

#print(nv.Dijkstra(src = 9, tgt = 3))

#print("Avant : \n \n")
#print(G)
#print('\n\n')
#print("Après : \n \n")

#G.icompose(G1)
#G.shift_indices(4)
#G.display()

#print(G1)
#print("\n")
#print("et G : \n \n")


#G.shift_indices(4)

#print(G)


#G.save_as_dot_file("testFichier.dot", False)
#F = open_digraph.from_dot_file("testFichier.dot")

#print(F)

#print(not(G1.is_well_formed()))
#print(G.is_well_formed())
#G.add_node('o2',{}, {})
#print(G.is_well_formed())
#G.add_edge(0,1)
#print(G.is_well_formed())
#G.add_input_node(8,1)
#G.add_output_node(9,5)
#print(G.is_well_formed())
##print('\n')
#print(G)



#H = open_digraph.empty()
#print(H.__repr__())
#a = n0.copy()
#print(a)
#print(n0.get_children_ids())
#print(G.get_id_node_map())
#print(G.get_nodes())
#print(G.get_node_ids())
#print(G.get_node_by_id(0))
#print(G.get_nodes_by_ids([2, 4, 6]))

#print(G.get_node_by_id(0))
#print(G.get_node_by_id(2))
#open_digraph.add_edge(G, 0, 2)
#print(G.get_node_by_id(0))
#print(G.get_node_by_id(2))

#dir(methods)
#inspect.getmembers(open_digraph.empty)

#print(G.new_id())
#G.add_edge(0, 1)

#G.add_node('z', {1 : 0}, {5 : 0} )
#print(G.__repr__())