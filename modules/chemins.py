from modules.node import *


######################################################### TP7 ##################################################################

class chemins:
#TD7 EX1 et EX2    
    def Dijkstra(self, src, direction = None, tgt = None):

        """
        Dijkstra renvoie un dictionnaire dist associant la valeur (en terme de noeuds) du
        plus court chemin de chaque node.id depuis src (qui est l'id du noeud source)
        et renvoie un dictionnaire prev donnant pour chaque noeud, le noeud qui le précède dans le plus court chemin.
        Si jamais est spécifié dans les paramètres, un id de noeud d'arrivée (paramètre tgt), l'algorithme s'arrête
        dés qu'il connait le chemin le plus court entre le noeud d'arrivée et celui de départ. 
        Il retourne alors les deux dictionnaire correspondant à ce cas précis.

        Paramètres :

        self(open_digraph) : le graphe sur lequel on fait la recherche du plus court chemin

        src(node.id) : id du noeud source

        direction : donne la direction selon les trois valeurs que peut prendre ce paramètre c'est-à-dire
                    None (ce qui signifie qu’on cherche à la fois dans les parents et dans les enfants),
                    -1 (ce qui signiefie que qu'on ne cherche que dans les parents)
                    et 1 (qu'on ne cherche quedans les enfants).
                    (vaut None par défaut)

        tgt(node.id) : id du noeud d'arrivée (si on cherche à avoir le plus court chemin entre deux noeuds particuliers)
                    (vaut None par défaut)

        Retour :

        (dist, prev) : couple de deux dictionnaires. 

                        dist a en clés l'id de chaque noeud du graphe self (ou une partie des noeuds si un tgt est spécifié)
                        et associe à chacune de ces clés le nombre d'arêtes minimales entre noeud et la source 

                        prev a en clés l'id de chaque noeud du graphe self (ou une partie des noeuds si un tgt est spécifié)
                        et associe à chacune d'entre elles, le noeud précédant leur noeud dans le plus court chemin depuis le noeud source

        """

        q = [src]    
        dist = {src: 0}
        prev = {}

        while q != [] :

            u = min(q, key = dist.get)
            if u == tgt : return (dist, prev)
            q.remove(u)
            neighbours = []
            uNode = self.get_node_by_id(u)

            if direction == None :

                for i in uNode.parents.keys():
                    neighbours.append(i)
                for j in uNode.children.keys():
                    neighbours.append(j)

            if direction == -1 :

                for i in uNode.parents.keys():
                    neighbours.append(i)

            if direction == 1 :

                for j in uNode.children.keys():
                    neighbours.append(j)

            for v in neighbours:
                if not(v in dist):
                    q.append(v)

                if (not(v in dist)) or (dist[v]>dist[u]+1):
                    dist[v] = dist[u] + 1
                    prev[v] = u

        return (dist, prev)

    def shortest_path(self, uId, vId ):
        """
        Calule le plus court chemin de u vers v

        Paramètres :

        self(open_digraph) : le graphe sur lequel on fait la recherche du plus court chemin

        uId(node.id) : id du noeud u 

        vId(node.id) : id du noeud v

        Retour:

        liste1 : une liste donnant les noeuds qui composent le plus court chemin de u vers v
        
        """

        dic = self.Dijkstra(src = uId, tgt = vId)[1]
        list1 = []

        i = vId

        while i != uId:

            list1.append(i)
            i = dic[i]

        list1.append(uId)    

        list1.reverse()

        return list1
            


            
    # EX 3
    def ancetres_communs(self, noeud1, noeud2):

        """
        ancetres_communs renvoie un dictionnaire qui associe a chaque ancetre commun des deux noeuds sa distance a chacun des deux noeuds
        
        Paramètres :

        self(open_digraph) : le graphe de noeuds
        noeud1(node) : un noeud du graphe self
        noeud2(node) : un noeud du graphe self

        Sortie : 

        parentscommuns(dictionnaire) : dictionnaire qui associe a chaque ancetre commun a noeud1 et noeud2 sa distance a chacun des deux noeuds
        
        """

        # on recupere les parents des deux noeuds
        id1 = self.Dijkstra(src = noeud1.id, direction = -1)
        id2 = self.Dijkstra(src = noeud2.id, direction = -1)
        parentscommuns = {}

        for id in id1[0].keys():
            # on cherche les parents communs
            if id in id2[0].keys() and id != noeud1.id:
                # si on en a trouve un, on construit un element du dictionnaire avec comme cle: id du parent commun et valeur: les distances du parent aux deux noeuds a l'aide de Dijkstra
                parentscommuns[id] = (id1[0][id], id2[0][id])
        return parentscommuns

     # EX 4
    def tritopologique(self):

        """
        tritopologique renvoie une liste de liste des id des noeuds du graphe en fonction de leur profondeur dans le graphe
        
        Parametre:
        self(open_digraph) : le graphe de noeuds
        
        Sortie:
        tri(liste) : liste de liste des id des noeuds 
        """

        g = self.copy()
        # on ignore les inputs et outputs du graphe
        for inp in g.inputs:
            g.remove_node_by_id(inp)
        for out in g.outputs:
            g.remove_node_by_id(out)
        end = 0
        d = {}
        n = 0

        while(end == 0):
            #if g.is_cyclic():
             #   return ValueError("graphe cyclique")
            liste = []

            # pour chaque noeud du graphe on regarde si le noeud n'a pas de parents, si oui on l'ajoute à la liste
            for node in g.nodes.keys():
                if g.get_node_by_id(node).parents == {}:
                    liste.append(self.get_node_by_id(node).id)
                    #print(self.get_node_by_id(node))
            # on construit le dictionnaire stockant les listes dans l'ordre de leur profondeur
            d[n] = liste

            # pour tous les noeuds selectionnes on les enleve du graphe
            for id in liste:
                g.remove_node_by_id(id)

            # pour finir la boucle while si on a plus de noeud dans le graphe
            if g.nodes == {}:
                end = 1
            
            # on incremente la profondeur et on recommence la boucle avec les noeuds restants
            n = n + 1
        
        # pour transformer le dictionnaire en liste de liste
        tri = []
        for p in d:
            tri.append(d[p])
        return tri
    
    # EX 5
    def profondeurnoeud(self, noeud):

        """
        profondeurnoeud renvoie la profondeur d'un noeud donne
        
        Parametres:
        self(open_digraph) : le graphe de noeuds
        noeud(node) : le noeud dont on veut la profondeur
        
        Sortie:
        profondeur(int) : la profondeur du noeud

        """

        profondeur = 0

        # on extrait le tri topologique du graphe
        tri = self.tritopologique()
        id = noeud.id

        # on parcout les partitions du graphe par le tri pour savoir ou le noeud est situe et a quelle profondeur
        for n in tri:
            if id in n:
                return profondeur 
            profondeur = profondeur + 1

    def profondeurgraphe(self):
        """
        profondeur graphe renvoie la profondeur du graphe
        
        Parametre:
        self(open_digraph) : le graphe de noeuds
        
        Sortie:
        
        len(tri) (int) : la longueur de la liste de liste des ids des noeuds
        
        """

        tri = self.tritopologique()

        # la profondeur du graphe est le nombre des ensembles partitionnes par le tri
        return len(tri)

    def le_plus_long(self, src, tgt):

        """
        chemin_le_plus_long calcule le chemin le plus long entre le noeud source (dont l'id est src) et le noeud d'arrivée (dont l'id est tgt) 
        dans un graphe acyclique.
        Cette méthode renvoie un dictionnaire dist qui associe à tgt (l'id du noeud d'arrivée), la distance (en nombre d'arêtes) du noeud source
        vers le noeud d'arrivée (elle renvoie également la distance la plus longue vers quelques noeuds autour de lui par lesquels elle est
        passée pour faire la recherche) et renvoie un dictionnaire prev donnant pour chaque noeud, l'id du noeud qui le précède dans le plus long chemin
        du noeud source vers le noeud d'arrivée.

        Paramètres :

        self(open_digraph) : le graphe sur lequel on fait la recherche du plus court chemin

        src(node.id) : id du noeud source

        tgt(node.id) : id du noeud d'arrivée

        Retour :

        (dist, prev) : couple de deux dictionnaires.

                        dist a en clés l'id du noeud d'arrivée dans self (et l'id des noeuds autour de lui par lesquels l'algorithme est
                        passé pour faire la recherche).
                        Il associe à chacune de ces clés le nombre d'arêtes maximale entre ce noeud et la source 

                        prev a en clés l'id (et l'id des noeuds autour de lui par lesquels l'algorithme est
                        passé pour faire la recherche).
                        Il associe à chacune des clés, l'id du noeud précédant leur noeud dans le plus long chemin depuis le noeud source

       
    

        """

        l = self.tritopologique()
        
        prev = {}

        #Init de dist avec tous les enfants de la source à distance 1
        dist = {src:0}

        for i in self.nodes[src].children.keys():
            dist[i] = 1
        
        cpt = 0
        for i in l:
            if src in i :
                break
            cpt+=1
        cpt += 1  

        for i in range(cpt, len(l)):
            
            for j in l[i] :

                p = self.get_node_by_id(j).parents
                sp = set(p.keys())
                sd = set(dist.keys())
                s = set(sp).intersection(sd)
                p = list(s)
                
                if p != [] :   

                    m = max(p, key = dist.get)
                    dist[j] = dist[m] + 1
                    prev[j] = m

                if j == tgt :
                    return (dist, prev)  
        return (dist, prev)            


    def chemin_le_plus_long(self, uId, vId) : 
        
            """
            Calule LE plus long chemin de u vers v

            Paramètres :

            self(open_digraph) : le graphe sur lequel on fait la recherche du plus court chemin

            uId(node.id) : id du noeud u 

            vId(node.id) : id du noeud v

            Retour:

            (liste1, d)

            liste1 : une liste donnant les noeuds qui composent le plus long chemin de u vers v

            d(int) : la distance maximale du noeud u au noeud v
            
            """
            c = self.le_plus_long(uId, vId)

            d = c[0][vId]

            dic = c[1]
            list1 = []

            i = vId

            while i != uId:

                list1.append(i)
                i = dic[i]

            list1.append(uId)    

            list1.reverse()

            return (list1,d)