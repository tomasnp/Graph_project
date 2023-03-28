from modules.node import *
import webbrowser

class open_digraph_affich_save:
    def save_as_dot_file(self, path, verbose=False): 

        f = open(path, "w")

        f.write("digraph G {\n")

        for s in self.nodes.values() :

            if verbose : 

                f.write(f'v{s.id} [label =  "{s.label} ({s.id})"')

            else : 

                f.write(f'v{s.id} [label =  "{s.label}"')

            if s.parents == {}:
                f.write(' shape=invtriangle')

            if s.children == {}:
                f.write(' shape=triangle')

            f.write('];\n')            


            for enfants in s.children.keys(): 

                for i in range(0, s.children[enfants]):

                    f.write(f'v{s.id} -> v{enfants};\n')

            
        f.write("}\n")            

        f.close()
        
    @classmethod
    def from_dot_file(self, fichier):

        f = open(fichier,"r")
        txt = f.read()
        txt = txt.replace("\n","")
        txtCoupe = txt.split("{")

        noeuds = {}
        inputs = {}
        outputs = {}
        
        for i in txtCoupe[1].split(";")[:-1]:
            decoupe1 = i.split(" ")
            if decoupe1[1][0] == "[" :

                decoupe2 = i.split("\"")

                new = node(decoupe1[0], decoupe2[1], {}, {})
                
                noeuds[decoupe1[0]] = new

                if decoupe2[1][0] == 'i' :
                    inputs[decoupe1[0]] = new

                if decoupe2[1][0] == 'o' :
                    outputs[decoupe1[0]] = new    

        for i in txtCoupe[1].split(";")[:-1]:
            decoupe1 = i.split(" ")
            if decoupe1[1][0] == '-': #####PRENDRE EN COMPTE LE CAS D'ENCHAINEMENT DE FLECHES  

                noeuds[decoupe1[0]].add_child_id(noeuds[decoupe1[2]].get_id())
                noeuds[decoupe1[2]].add_parent_id(noeuds[decoupe1[0]].get_id())

        
        graphe = self(inputs, outputs, noeuds.values())

        return graphe


    def display(self, verbose=False):

        chaine = ''

        chaine += 'digraph{%0A%09'

        for s in self.nodes.values() :

            if verbose : 

                chaine += f'v{s.id} [label =  "{s.label} ({s.id})'

            else : 

                chaine += f'v{s.id} [label =  "{s.label}"'

            if s.parents == {}:
                chaine += ' shape=invtriangle'

            if s.children == {}:
                chaine += ' shape=triangle'

            chaine += ']%3B%0A%09'            


            for enfants in s.children.keys(): 

                for i in range(0, s.children[enfants]):

                    chaine += f'v{s.id} -> v{enfants}%3B%0A%09'


        chaine += '}%0A%09'
        url = 'https://dreampuf.github.io/GraphvizOnline/#'+chaine
        webbrowser.open(url)
