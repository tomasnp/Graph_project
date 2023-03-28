from ast import Not
from modules.import_random import graph_from_adjacency_matrix, random_triangular_int_matrix
from modules.open_digraph import *
import random

class bool_circ(open_digraph):
    def __init__(self, g):
        self.inputs = g.inputs
        self.outputs = g.outputs
        self.nodes = g.nodes

        
        if not(self.is_well_formed):
            raise ValueError('Ce n\'est pas un circuit booléen')

    def is_cyclic(self):
        if self.get_nodes() == []:
            return False
        a = 0
        for i in self.nodes.keys():
            if (self.get_node_by_id(i)).children != {}:
                a += 1
            else:
                self.remove_node_by_id(i)
                return self.is_cyclic()

        if len(self.nodes.keys()) == a:
            return True
    

    def is_well_formed(self):

        if self.is_cyclic() :
            return False

        for i in self.nodes.values():

            if i.get_label() == '':
                if i.indegree() != 1:
                    return False

            if (i.get_label() == '&') or (i.get_label() == '|') or (i.get_label() == '^'):
                if i.outdegree() != 1:
                    return False 

            if i.get_label() =='~' :
                if i.degree() != 2:
                    return False

            if i.get_label() =='0' or i.get_label() =='1' :
                if i.outdegree() != 1 or i.indegree() != 0:
                    return False

        return True       

    def parse_parentheses(ls):
        f = open_digraph.empty()
        F  = bool_circ(f)
        for s in ls:
            Id = 0
            n0 = node(Id,'',{},{})
            G = open_digraph([],[],[n0])
            g = bool_circ(G)
            g.add_output_node(1,0)

            current_node = n0.id

            s2 = ''

            for char in s :

                if char == '(' :
                    G.get_node_by_id(current_node).label += s2
                    current_node = G.add_node('',{},{current_node})

                    s2 =''

                else :
                    if char == ')':
                        noeud = G.get_node_by_id(current_node)
                        noeud.label +=s2
                        current_node = list(noeud.children.keys())[0]
                        s2 = ''

                    else :
                        s2 += char
            l = ['&', '|', '~', '']
            liste = []
            for i in g.nodes:
                if g.nodes[i].label not in l:
                    liste.append(g.nodes[i])
            j = 0
            while j < len(liste):  
                a = liste[j]
                i = 0
                while (i < len(liste)):
                    n = liste[i]
                    if a.label == n.label and a.id != n.id:
                        g.fusionnoeuds(a.id, n.id)
                        liste.remove(n)    
                    i+=1
                j+=1
            while liste:   
                min = liste[0]
                for noeud in liste[1:]:
                    if ord(min.label[1:]) > ord(noeud.label[1:]):
                        min = noeud
                liste.remove(min)
                min.label = ''
                g.add_input_id(min.id)
            F = F.compose(g)
            
        return F   

    def estPuissance2(length):
        k = 0
        v = False
        while(not v):
            if length % (2**k):
                return True
            k += 1
        return False

    def viaTable(op):
        """

        revnvoi un circuit booléen depuis la table de vérité de l'opérateur fourni en paramètre

        paramètre:
        
        op : une chaîne de caractère correspondant à l'opérateur

        résultat:

        g : un bool_circ obtenu à partir de la table de vérité de l'opérateur op

        """
        if not bool_circ.estPuissance2(len(op)):
            raise ValueError("La longueur de la chaîne n'est pas une puissance de 2")

        n0 = node(0,'',{},{})
        n1 = node(1,'',{},{})
        n2 = node(2,'',{},{})
        n3 = node(3,'',{},{})
        G = open_digraph([n0,n1,n2,n3], [], [n0,n1,n2,n3])
        g = bool_circ(G)

        ou = g.add_node('|',{},{})
       
        for i in range(0,len(op)):
            if op[i]=='1':
                n = bin(i)
                n=n[2:]
                aCompleter = 4-len(n)
                n = '0'*aCompleter + n
                et = g.add_node('&',{},{})
                idd = 0
                ident = g.nodes[idd]
                
                for j in range(0,len(n)):
                    
                    if n[j] == '1':
                        ident.add_child_id(et)
                    else:
                        non = g.add_node('~',{},{})
                        ident.add_child_id(non)
                        g.get_node_by_id(non).add_child_id(et)
                    idd+=1
                    ident = g.nodes[idd]   
                g.get_node_by_id(et).add_child_id(ou)  

        return g

    def genergraphe(n, n_input, n_output):

        """
        genergraphe genere un circuit booleen aleatoire de taille n, avec un nombre n_inout d'entrees et n_output de sorties
        
        Parametres:
        n : la taille du graphe
        n_input : le nombre d'entrees voulu dans notre circuit
        n_input : le nombre de sorties voulu dans notre circuit
        
        Sortie:
        g : le circuit booleen construit

        """
        #g´en´erer un graphe dirig´e acyclique sans inputs ni outputs
        m = random_triangular_int_matrix(n, 1)
        g = graph_from_adjacency_matrix(m)

        #ajouter un input vers chaque noeud sans parent, et un output depuis chaque noeud sans enfant
        d = g.nodes.copy()
        for n_id in d:
            if g.nodes[n_id].parents == {}:
                g.add_input_node(g.new_id(), n_id)
            if g.nodes[n_id].children == {}:
                g.add_output_node(g.new_id(), n_id)
        
        #entrees et sorties specifiees
        if n_input > len(g.inputs):
            while(n_input > len(g.inputs)):
                while True:

                    id = random.choice(g.get_node_ids())
                    if id not in g.outputs:
                        break
                    
                if id in g.inputs:
                    g.inputs.remove(id)
                g.add_input_node(g.new_id(), id)

        if n_input < len(g.inputs):
            while(n_input < len(g.inputs)):
                id1 = random.choice(g.inputs)
                g.inputs.remove(id1)
                id2 = random.choice(g.inputs)
                g.inputs.remove(id2)
                in_node_id = g.add_node('', [], [id1, id2])
                g.add_input_node(g.new_id(), in_node_id)

        if n_output > len(g.outputs):
            while(n_output > len(g.outputs)):
                while True:
                    id = random.choice(g.get_node_ids())
                
                    if id in g.inputs:   
                        break
                if id in g.outputs:
                    g.outputs.remove(id)    
                g.add_output_node(g.new_id(), id)
        if n_output < len(g.outputs):
            while(n_output < len(g.outputs)):
                id1 = random.choice(g.outputs)
                g.outputs.remove(id1)
                id2 = random.choice(g.outputs)
                g.outputs.remove(id2)
                out_node_id = g.add_node('', [id1, id2], [])
                g.add_output_node(g.new_id(), out_node_id)
        
        #association noeud/operateur en fonction de leur degre
        
        op_unaire = ['~']
        op_binaire =['&', '|']

        for node in g.get_nodes():
            if node.indegree() == 1 and node.outdegree() == 1:
                node.label = random.choice(op_unaire)
            if node.indegree() > 1 and node.outdegree() == 1:
                node.label = random.choice(op_binaire)
            if node.indegree() > 1 and node.outdegree() > 1:
                id_uop = g.add_node(random.choice(op_binaire), node.parents, {})
                id_ucp = g.add_node('', {}, node.children)
                g.add_edge(id_uop, id_ucp)
                g.remove_node_by_id(node.id)
        
        return g

############### TD 10 EXO 3 à moitié fait ##########################
    def Half_Adder(a, b):
    
        """
        Half-Addern prend deux registres de tailles 2 puissance n et renvoie un registre de taille 2 puissance n (qui contient la somme des deux nombres donnees en entreee, modulo 2n)
        
        Paramètres:
        a, b : deux chaines de caracteres composees de 0 et de 1 representant chacun un nombre ecrit en binaire 
        
        Sortie:
        (res, retenue) : couple avec :  - res : la somme de a et b
                                        - retenue : un bit indiquant si le calcul de la somme a depasse la taille du registre (1 pour vrai, 0 pour faux)
        """

        if not bool_circ.estPuissance2(len(a)) or not bool_circ.estPuissance2(len(b)) or len(a) != len(b):
            raise ValueError("La longueur de la chaîne n'est pas une puissance de 2")

        somme = bin(int(a, 2) + int(b, 2))
        s = list(str(somme))
        s.remove('b')
        res = "".join(s)
        if(len(res) > len(a)):
            retenue = 1
        else:
            retenue = 0
        return (res, retenue)

############### TD 11 EXO 2, 3, 4 pas finis ##########################
    def graphbinaire(int, size = 8):
        """
        genere un circuit booleen avec un nombre size de noeuds representant le registre instancie en l’entier int

        Parametres:
        int : l'entier a representer
        size : le nombre de noeuds dans le circuit

        Sortie:
        g : le circuit booleen construit en fonction de l'entier et de la taille size
        
        """
        b = list(str(bin(int)[2:]))
        print(b)
        G = open_digraph.empty()
        if size > len(b):
            for i in range(0, size - len(b)):
             
                Sortie = G.add_node("", {}, {})
                Id = G.add_node("0", {}, {})
                G.add_output_node(Sortie, Id)

        for i in range(0, len(b)):
            
            Sortie = G.add_node("", {}, {})
            Id = G.add_node(b[i], {}, {})
            G.add_output_node(Sortie, Id)

        g = bool_circ(G)
        
        return g

    def copies(self, n : node):
        """
        copie le noeud en fonction de ses enfants
        
        Parametre:
        n : le noeud dont on va copier
        
        """
        self.fusionnoeuds(n.get_id(), n.get_children_ids()[0])
        outputs = n.get_children_ids()
        self.remove_node_by_id(n.get_id())
        G = self.graphbinaire(n.get_label(), len(outputs))
        self.iparallel([G])

    def porte_NON(self, n : node):
        """
        transforme le bit represente dans le noeud par sa negation

        Parametre:
        n : le noeud dont on va appliquer la transformation

        """
        self.fusionnoeuds(n.get_id(), n.get_children_ids()[0])
        if (n.get_label() == "0"):
            n.set_label("1")
        else:
            n.set_label("0")

    def porte_ET(self, n : node):
        """
        reduit et simplifie la partie du circuit concernee avec la transformation porte ET

        Parametre:
        n : le noeud dont on va appliquer la transformation
        
        """
        if (n.get_label() == "0"):
            self.fusionnoeuds(n.get_id(), n.get_children_ids()[0])
     
            for i in range(0, len(n.get_parent_ids)):
                p = self.get_node_by_id(n.get_parent_ids[i])
                new_child = self.add_node("", {}, {})
                self.add_edge(p, new_child)
                self.remove_edge(p.get_id(), n.get_id())
        else:
            self.remove_node_by_id(n.get_id())

    def porte_OU(self, n :node):
        """
        reduit et simplifie la partie du circuit concernee avec la transformation porte OU

        Parametre:
        n : le noeud dont on va appliquer la transformation
        
        """
        if (n.get_label() == "1"):
            self.fusionnoeuds(n.get_id(), n.get_children_ids()[0])
              
            for i in range(0, len(n.get_parent_ids)):
                p = self.get_node_by_id(n.get_parent_ids[i])
                new_child = self.add_node("", {}, {})
                self.add_edge(p, new_child)
                self.remove_edge(p.get_id(), n.get_id())
        else:
            self.remove_node_by_id(n.get_id())

    def elems_neutres(self, n : node):
        """
        transforme l'operation du noeud en un bit (en fonction de l'operation) 

        Parametre:
        n : le noeud dont on va appliquer la transformation
        
        """
        if(n.get_label() == "|" or n.get_label() == "^"):
            n.set_label("0")
        elif (n.get_label() == "&"):
            n.set_label("1")

    def porte_OU_EXCLUSIF(self, n : node):
        """
        reduit et simplifie la partie du circuit concernee avec la transformation porte OU EXCLUSIF

        Parametre:
        n : le noeud dont on va appliquer la transformation
        
        """
        if(n.get_label() == "0"):
            self.remove_node_by_id(n.get_id())
        else:
            op = self.get_node_by_id(n.get_children_ids()[0])   
            output = op.get_children_ids()[0]
            self.remove_edge(n.get_children_ids()[0], output)
            self.add_node("~", {op.get_id()}, {output}) 
            self.remove_node_by_id(n.get_id())   

    def evaluate(self):
        """
        evalue le graphe en appliquant, lorsque c'est possible et tant qu'il y a des co-feuilles qui ne sont pas directement reliees a une sortie
        les transformations qui reduit et simplifie le circuit
        
        """
        lbin = ["1", "0"]
        lneutre = ["|", "^", "&"]
        profondeur = self.profondeurgraphe()
        while(profondeur != 1):
            for n in self.get_nodes():
                if n.label in lbin:
                    op = self.get_node_by_id(n.get_children_ids()[0]) 
                    if op.label == "~":
                        self.porte_NON(n)
                    elif op.label == "&":
                        self.porte_ET(n)
                    elif op.label == "|":
                        self.porte_OU(n)
                    elif op.label == "^":
                        self.porte_OU_EXCLUSIF(n)
                    elif op.label == "":
                        self.copies(n)
                elif n.label in lneutre:
                    self.elems_neutres(n)
            profondeur = self.profondeurgraphe()

    def encodeur():
        """
        genere un circuit, a l'aide de la fonction parse_parentheses, representant l'encodeur
        
        Sortie:
        g : le circuit booleen de l'encodeur
        
        """
        g = bool_circ.parse_parentheses(["(x1)^(x2)^(x4)", "(x1)^(x3)(x4)", "(x2)^(x3)^(x4)"]) 
        return g

    def decodeur():
        """
        genere un circuit, a l'aide de la fonction parse_parentheses, representant le decodeur
        
        Sortie:
        g : le circuit booleen du decodeur
        
        """
        g = bool_circ.parse_parentheses(["(x1)^(x2)^(x4)", "(x1)^(x3)^(x4)", "(x2)^(x3)^(x4)"])
        f = bool_circ.parse_parentheses(["((x5)&(x6)&(~(x7))^(x1)", "((x5)&(~(x6))&(x7))^(x2)", "((~(x5))&(x6)&(x7))^(x3)", "((x5)&(x6)&(x7))^(x4)"])
        g.parallel(f)
        
        return g

    def assoc_XOR_et_COPIE(self, n : node):
        """
        reduit et simplifie la partie du circuit concernee avec l'associativite de XOR ou de COPIE'

        Parametre:
        n : le noeud dont on va appliquer l'associativite
        
        """
        c = self.get_node_by_id(n.get_children_ids()[0])
        self.fusionnoeuds(n.id, c.id)
        
    def involution_XOR(self, n : node):
        """
        reduit et simplifie la partie du circuit concernee avec l'involution de XOR

        Parametre:
        n : le noeud dont on va appliquer l'associativite
        
        """
        for c in n.get_children_ids:
            ch = self.get_node_by_id(c)
            if (ch.label == "^"):
                if (n.children[c] >= 2):
                    if (n.children[c] % 2 == 0):
                        self.remove_parallel_edges(n.id, c)
                    else:
                        self.remove_parallel_edges(n.id, c)
                        self.add_edge(n.id, c)
    
    def effacement(self, n: node):
        """
        reduit et simplifie la partie du circuit concernee avec l'effacement

        Parametre:
        n : le noeud dont on va appliquer l'effacement
        
        """
        for i in range(0, len(n.get_parent_ids)):
                p = self.get_node_by_id(n.get_parent_ids[i])
                new_child = n.get_children_ids()[0].copy()
                self.add_edge(p, new_child)
                self.remove_edge(p.get_id(), n.get_id())
        self.remove_node_by_id(n.get_children_ids()[0])        
        self.remove_node_by_id(n.id)

    def NON_travers_XOR(self, n : node):
        """
        reduit et simplifie la partie du circuit concernee en prenant en compte la negation a travers XOR

        Parametre:
        n : le noeud dont on va appliquer la transformation
        
        """
        ou_id = n.get_children_ids()[0]
        self.fusionnoeuds(ou_id, n.id)
        out_id = self.get_node_by_id(ou_id).get_children_ids()[0]
        self.remove_edge(ou_id, out_id)
        non_id = self.add_node("~", {ou_id}, {out_id})
        
    def NON_travers_COPIE(self, n : node):
        """
        reduit et simplifie la partie du circuit concernee en prenant en compte la negation a travers la copie

        Parametre:
        n : le noeud dont on va appliquer la transformation
        
        """
        f = n.get_children_ids()[0]
        self.fusionnoeuds(f, n.id)
        for c_id in self.get_node_by_id(f).get_children_ids():
            self.remove_edge(f, c_id)
            t = self.add_node("~", {f}, {c_id})

    def involution_NON(self, n : node):
        """
        reduit et simplifie la partie du circuit concernee avec l'involution de NON

        Parametre:
        n : le noeud dont on va appliquer l'associativite
        
        """
        self.fusionnoeuds(n.id, self.get_node_by_id(n.get_children_ids()[0]))
        p_id = n.get_parent_ids()[0]
        c_id = n.get_children_ids()[0]
        self.add_edge(p_id, c_id)
        self.remove_node_by_id(n.id)


    def evaluateHamming(self):
        
        """
        evalue le graphe en appliquant, lorsque c'est possible et tant qu'il y a des co-feuilles qui ne sont pas directement reliees a une sortie
        les transformations qui reduit et simplifie le circuit
        
        """
        self.evaluate()










        



