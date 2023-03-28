zimport sys
import os
root = os.path.normpath(os.path.join(__file__, './../..')) 
sys.path.append(root)# allows us to fetch files from the project root 
import unittest
from modules.open_digraph import *


class InitTest(unittest.TestCase):
    def test_init_node(self):
        n0 = node(0, 'i', {}, {1:1}) 
        self.assertEqual(n0.id, 0) 
        self.assertEqual(n0.label, 'i') 
        self.assertEqual(n0.parents, {}) 
        self.assertEqual(n0.children, {1:1}) 
        self.assertIsInstance(n0, node)
       # if __name__ == '__main__': # the following code is called only when unittest.main() # precisely this file is run


class NodeTest(unittest.TestCase): 
    
    def setUp(self):
        self.n0 = node(0, 'a', [], [1]) 
    
    def test_get_id(self):
        self.assertEqual(self.n0.get_id(), 0)
    
    def test_get_label(self): 
        self.assertEqual(self.n0.get_label(), 'a')

  #  def test_copy(self):
  #      self.assertIsNot(self.copy(), self)


class open_digraphTest(unittest.TestCase): 


    #Methode shift_indices

   # def test_shift_indices(self):
   #     n0 = node(0, 'a', {3:1, 4:1}, {1:1, 2:1})
   #     n1 = node(1, 'b', {0:1}, {2:2, 5:1})
   #     n2 = node(2, 'c', {0:1, 1:2}, {6:1})
   #     i0 = node(3, 'i0', {}, {0:1})
   #     i1 = node(4, 'i1', {}, {0:1})
   #     o0 = node(5, 'o0', {1:1}, {})
   #     o1 = node(6, 'o1', {2:1}, {})

    #    G = open_digraph([3,4], [5,6], [n0,n1,n2,i0,i1,o0,o1])
    #    G.shift_indices(4)
    #    self.assertEqual(G.nodes[1].get_id(), 5)
    #    self.assertEqual(G.nodes[2].get_id(), 6)
    #    self.assertEqual(G.nodes[3].get_id(), 7)
    #    self.assertEqual(G.nodes[4].get_id(), 8)
    #    self.assertEqual(G.nodes[5].get_id(), 9)
    #    self.assertEqual(G.nodes[6].get_id(), 10)

    #Methode Dijkstra

    def test_Dijkstra(self) :

        n0 = node(0, 'a', {3:1, 4:1}, {1:1, 2:1})
        n1 = node(1, 'b', {0:1}, {2:2, 5:1})
        n2 = node(2, 'c', {0:1, 1:2}, {6:1})
        i0 = node(3, 'i0', {}, {0:1})
        i1 = node(4, 'i1', {}, {0:1})
        o0 = node(5, 'o0', {1:1}, {})
        o1 = node(6, 'o1', {2:1}, {})

        G = open_digraph([3,4], [5,6], [n0,n1,n2,i0,i1,o0,o1])

        dic0 = {0: 0, 3: 1, 4: 1, 1: 1, 2: 1, 5: 2, 6: 2}
        dic3 = {3: 0, 0: 1, 4: 2, 1: 2, 2: 2, 5: 3, 6: 3}
        dic5 = {5: 0, 1: 1, 0: 2, 2: 2, 3: 3, 4: 3, 6: 3}

        self.assertEqual(G.Dijkstra(0)[0], dic0)
        self.assertEqual(G.Dijkstra(3)[0], dic3)
        self.assertEqual(G.Dijkstra(5)[0], dic5)

        n3 = node(1, 'e', {4:1, 5:1}, {2:1, 3:1})
        n4 = node(2, 'f', {1:1}, {3:2, 6:1})
        n5 = node(3, 'g', {1:1, 2:2}, {7:1})
        i2 = node(4, 'i2', {}, {1:1})
        i3 = node(5, 'i3', {}, {1:1})
        o2 = node(6, 'o2', {2:1}, {})
        o3 = node(7, 'o3', {3:1}, {})

        G1 = open_digraph([4,5], [6,7], [n3,n4,n5,i2,i3,o2,o3])

        nv = G.compose(G1)

        dicNv0 = {0: 0, 3: 1, 4: 1, 1: 1, 2: 1, 12: 2, 13: 2, 5: 2, 6: 2, 8: 3, 9: 3, 7: 4, 10: 5, 11: 5}
        dicNv7 = {7: 0, 10: 1, 11: 1, 8: 1, 9: 1, 12: 2, 13: 2, 3: 3, 4: 3, 0: 4, 1: 5, 2: 5, 5: 6, 6: 6}
        dicNv11 = {11: 0, 7: 1, 10: 2, 8: 2, 9: 2, 12: 3, 13: 3, 3: 4, 4: 4, 0: 5, 1: 6, 2: 6, 5: 7, 6: 7}
        self.assertEqual(nv.Dijkstra(0)[0], dicNv0)
        self.assertEqual(nv.Dijkstra(7)[0], dicNv7)
        self.assertEqual(nv.Dijkstra(11)[0], dicNv11)

        #Avec tgt

        dicNvtgt = {3: 0, 12: 1, 0: 1, 8: 2, 4: 2, 1: 2, 2: 2, 7: 3, 9: 3, 13: 3}
        dicNvTgt0 = {12: 3, 0: 3, 8: 12, 4: 0, 1: 0, 2: 0, 7: 8, 9: 8, 13: 4}
        dicNvTgt1 = {9: 0, 7: 1, 8: 1, 13: 1, 10: 2, 11: 2, 12: 2, 4: 2, 3: 3, 0: 3}
        dicNvTgt2 = {7: 9, 8: 9, 13: 9, 10: 7, 11: 7, 12: 8, 4: 13, 3: 12, 0: 4}
        self.assertEqual(nv.Dijkstra(src = 3, tgt = 1)[0], dicNvtgt)
        self.assertEqual(nv.Dijkstra(src = 3, tgt = 1)[1], dicNvTgt0)
        self.assertEqual(nv.Dijkstra(src = 9, tgt = 3)[0], dicNvTgt1)
        self.assertEqual(nv.Dijkstra(src = 9, tgt = 3)[1], dicNvTgt2)

    def test_shortest_path(self):

        n0 = node(0, 'a', {3:1, 4:1}, {1:1, 2:1})
        n1 = node(1, 'b', {0:1}, {2:2, 5:1})
        n2 = node(2, 'c', {0:1, 1:2}, {6:1})
        i0 = node(3, 'i0', {}, {0:1})
        i1 = node(4, 'i1', {}, {0:1})
        o0 = node(5, 'o0', {1:1}, {})
        o1 = node(6, 'o1', {2:1}, {})

        G = open_digraph([3,4], [5,6], [n0,n1,n2,i0,i1,o0,o1])

        n3 = node(1, 'e', {4:1, 5:1}, {2:1, 3:1})
        n4 = node(2, 'f', {1:1}, {3:2, 6:1})
        n5 = node(3, 'g', {1:1, 2:2}, {7:1})
        i2 = node(4, 'i2', {}, {1:1})
        i3 = node(5, 'i3', {}, {1:1})
        o2 = node(6, 'o2', {2:1}, {})
        o3 = node(7, 'o3', {3:1}, {})

        G1 = open_digraph([4,5], [6,7], [n3,n4,n5,i2,i3,o2,o3])

        nv = G.compose(G1)

        self.assertEqual(G.shortest_path(3,5), [3, 0, 1, 5])
        self.assertEqual(nv.shortest_path(7,2), [7, 8, 12, 3, 0, 2])
        self.assertEqual(nv.shortest_path(13,12), [13, 9, 8, 12])

    def test_ancetres_communsTest(self):
        n0 = node(0, 'a', {3:1, 4:1}, {1:1, 2:1})
        n1 = node(1, 'b', {0:1}, {2:2, 5:1}) 
        n2 = node(2, 'c', {0:1, 1:2}, {6:1})    
        i0 = node(3, 'i0', {}, {0:1})
        i1 = node(4, 'i1', {}, {0:1})
        o0 = node(5, 'o0', {1:1}, {})
        o1 = node(6, 'o1', {2:1}, {})
        G = open_digraph([3,4], [5,6], [n0,n1,n2,i0,i1,o0,o1])

        #self.assertIsNot(G.ancetres_communs(n0, n0), {3: (1, 1), 4: (1, 1)})
        self.assertEqual(G.ancetres_communs(i0, i1), {})
        self.assertEqual(G.ancetres_communs(o1, o0), {0: (2, 2), 1: (2, 1), 3: (3, 3), 4: (3, 3)})
        
        a0 = node(1, 'e', {4:1, 5:1}, {2:1, 3:1})
        a1 = node(2, 'f', {1:1}, {3:2, 6:1})
        a2 = node(3, 'g', {1:1, 2:2}, {7:1})
        b0 = node(4, 'h', {}, {1:1})
        b1 = node(5, 'i', {}, {1:1})
        c0 = node(6, 'j', {2:1}, {})
        c1 = node(7, 'k', {3:1}, {})
        F = open_digraph([4,5], [6,7], [a0,a1,a2,b0,b1,c0,c1])
        H = G.compose(F)

        self.assertEqual(H.ancetres_communs(H.get_node_by_id(9), H.get_node_by_id(3)), {7: (1, 3), 8: (1, 2), 10: (2, 4), 11: (2, 4)})
        self.assertEqual(H.ancetres_communs(H.get_node_by_id(10), H.get_node_by_id(5)), {})
        self.assertEqual(H.ancetres_communs(H.get_node_by_id(7), H.get_node_by_id(8)), {10: (1, 2), 11: (1, 2)})
        
    def test_tritopologiqueTest(self):
        n0 = node(0, 'a', {3:1, 4:1}, {1:1, 2:1})
        n1 = node(1, 'b', {0:1}, {2:2, 5:1}) 
        n2 = node(2, 'c', {0:1, 1:2}, {6:1})    
        i0 = node(3, 'i0', {}, {0:1})
        i1 = node(4, 'i1', {}, {0:1})
        o0 = node(5, 'o0', {1:1}, {})
        o1 = node(6, 'o1', {2:1}, {})
        G = open_digraph([3,4], [5,6], [n0,n1,n2,i0,i1,o0,o1])

        a0 = node(1, 'e', {4:1, 5:1}, {2:1, 3:1})
        a1 = node(2, 'f', {1:1}, {3:2, 6:1})
        a2 = node(3, 'g', {1:1, 2:2}, {7:1})
        b0 = node(4, 'h', {}, {1:1})
        b1 = node(5, 'i', {}, {1:1})
        c0 = node(6, 'j', {2:1}, {})
        c1 = node(7, 'k', {3:1}, {})
        F = open_digraph([4,5], [6,7], [a0,a1,a2,b0,b1,c0,c1])
        H = G.compose(F)

        tri = H.tritopologique()

        self.assertIn([1], tri)
        self.assertIn(1, tri[6])
        self.assertEqual(tri, [[7], [8], [9, 12], [3, 13], [4], [0], [1], [2]])
        self.assertNotIn([6], tri)

    def test_profondeurnoeudTest(self):
        n0 = node(0, 'a', {3:1, 4:1}, {1:1, 2:1})
        n1 = node(1, 'b', {0:1}, {2:2, 5:1}) 
        n2 = node(2, 'c', {0:1, 1:2}, {6:1})    
        i0 = node(3, 'i0', {}, {0:1})
        i1 = node(4, 'i1', {}, {0:1})
        o0 = node(5, 'o0', {1:1}, {})
        o1 = node(6, 'o1', {2:1}, {})
        G = open_digraph([3,4], [5,6], [n0,n1,n2,i0,i1,o0,o1])

        a0 = node(1, 'e', {4:1, 5:1}, {2:1, 3:1})
        a1 = node(2, 'f', {1:1}, {3:2, 6:1})
        a2 = node(3, 'g', {1:1, 2:2}, {7:1})
        b0 = node(4, 'h', {}, {1:1})
        b1 = node(5, 'i', {}, {1:1})
        c0 = node(6, 'j', {2:1}, {})
        c1 = node(7, 'k', {3:1}, {})
        F = open_digraph([4,5], [6,7], [a0,a1,a2,b0,b1,c0,c1])
        H = G.compose(F)

        self.assertEqual(H.profondeurnoeud(H.get_node_by_id(12)), 2)
        self.assertEqual(H.profondeurnoeud(H.get_node_by_id(2)), 7)

    def test_profondeurgrapheTest(self):
        n0 = node(0, 'a', {3:1, 4:1}, {1:1, 2:1})
        n1 = node(1, 'b', {0:1}, {2:2, 5:1}) 
        n2 = node(2, 'c', {0:1, 1:2}, {6:1})    
        i0 = node(3, 'i0', {}, {0:1})
        i1 = node(4, 'i1', {}, {0:1})
        o0 = node(5, 'o0', {1:1}, {})
        o1 = node(6, 'o1', {2:1}, {})
        G = open_digraph([3,4], [5,6], [n0,n1,n2,i0,i1,o0,o1])

        a0 = node(1, 'e', {4:1, 5:1}, {2:1, 3:1})
        a1 = node(2, 'f', {1:1}, {3:2, 6:1})
        a2 = node(3, 'g', {1:1, 2:2}, {7:1})
        b0 = node(4, 'h', {}, {1:1})
        b1 = node(5, 'i', {}, {1:1})
        c0 = node(6, 'j', {2:1}, {})
        c1 = node(7, 'k', {3:1}, {})
        F = open_digraph([4,5], [6,7], [a0,a1,a2,b0,b1,c0,c1])
        H = G.compose(F)

        self.assertEqual(G.profondeurgraphe(), 3)
        self.assertEqual(H.profondeurgraphe(), 8)            


    def test_le_plus_long(self):   

        n0 = node(0, 'a', {3:1, 4:1}, {1:1, 2:1})
        n1 = node(1, 'b', {0:1}, {2:2, 5:1})
        n2 = node(2, 'c', {0:1, 1:2}, {6:1})
        i0 = node(3, 'i0', {}, {0:1})
        i1 = node(4, 'i1', {}, {0:1})
        o0 = node(5, 'o0', {1:1}, {})
        o1 = node(6, 'o1', {2:1}, {})

        G = open_digraph([3,4], [5,6], [n0,n1,n2,i0,i1,o0,o1])

        n3 = node(1, 'e', {4:1, 5:1}, {2:1, 3:1})
        n4 = node(2, 'f', {1:1}, {3:2, 6:1})
        n5 = node(3, 'g', {1:1, 2:2}, {7:1})
        i2 = node(4, 'i2', {}, {1:1})
        i3 = node(5, 'i3', {}, {1:1})
        o2 = node(6, 'o2', {2:1}, {})
        o3 = node(7, 'o3', {3:1}, {})

        G1 = open_digraph([4,5], [6,7], [n3,n4,n5,i2,i3,o2,o3])

        nv = G.compose(G1)  

        #self.assertEqual(nv.le_plus_long(7,2),{7: 0, 8: 1, 9: 2, 12: 2, 3: 3, 13: 3, 4: 4, 0: 5, 1: 6, 2: 7}, {8: 7, 9: 8, 12: 8, 3: 12, 13: 9, 4: 13, 0: 4, 1: 0, 2: 1})
        #self.assertEqual(nv.le_plus_long(8,0),({8: 0, 9: 1, 12: 1, 3: 2, 13: 2, 4: 3, 0: 4}, {9: 8, 12: 8, 3: 12, 13: 9, 4: 13, 0: 4}))

    def chemin_test_le_plus_long(self):   

        n0 = node(0, 'a', {3:1, 4:1}, {1:1, 2:1})
        n1 = node(1, 'b', {0:1}, {2:2, 5:1})
        n2 = node(2, 'c', {0:1, 1:2}, {6:1})
        i0 = node(3, 'i0', {}, {0:1})
        i1 = node(4, 'i1', {}, {0:1})
        o0 = node(5, 'o0', {1:1}, {})
        o1 = node(6, 'o1', {2:1}, {})

        G = open_digraph([3,4], [5,6], [n0,n1,n2,i0,i1,o0,o1])

        n3 = node(1, 'e', {4:1, 5:1}, {2:1, 3:1})
        n4 = node(2, 'f', {1:1}, {3:2, 6:1})
        n5 = node(3, 'g', {1:1, 2:2}, {7:1})
        i2 = node(4, 'i2', {}, {1:1})
        i3 = node(5, 'i3', {}, {1:1})
        o2 = node(6, 'o2', {2:1}, {})
        o3 = node(7, 'o3', {3:1}, {})

        G1 = open_digraph([4,5], [6,7], [n3,n4,n5,i2,i3,o2,o3])

        nv = G.compose(G1)  

        self.assertEqual(G.chemin_le_plus_long(0,2),([0, 1, 2], 2))
        self.assertEqual(nv.chemin_le_plus_long(7,2),([7, 8, 9, 13, 4, 0, 1, 2], 7))
        self.assertEqual(nv.chemin_le_plus_long(13,2),([13, 4, 0, 1, 2], 5))
        self.assertEqual(nv.chemin_le_plus_long(8,1),([8, 9, 13, 4, 0, 1], 5))


if __name__ == '__main__': # the following code is called only when
    unittest.main() # precisely this file is run
