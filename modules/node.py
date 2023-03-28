
class node:
    
    def __init__(self, identity, label, parents, children):
        self.id = identity
        self.label = label
        self.parents = parents
        self.children = children

    def __str__(self):
        return f"label : {self.label}, parents : {self.parents}, children : {self.children}"

    def __repr__(self):
        return f"label : '{self.label}', parents : '{self.parents}', children : '{self.children}'"

    def copy(self):
        return node(self.id, self.label, self.parents.copy(), self.children.copy())



#getters
    def get_id(self):
        return self.id
    
    def get_label(self):
        return self.label

    def get_parent_ids(self):
        a = []
        for cle in self.parents.keys():
            a.append(cle)
        return a

    def get_children_ids(self):
        a = []
        for cle in self.children.keys():
            a.append(cle)
        return a

#setters
    def set_id(self, ident):
        self.id = ident
    
    def set_label(self, labl):
        self.label = labl

    def set_parents_ids(self, ids_list):
        self.parents = {}
        for i in ids_list:
            self.parents[i] = None
    
    def set_children_ids(self, ids_list):
        self.children = {}
        for i in ids_list:
            self.children[i] = None
    
    def add_child_id(self, id_child):
        if id_child in self.get_children_ids() :
            self.children[id_child] += 1
        else : 
            self.children[id_child] = 1

    def add_parent_id(self, id_parent):
        if id_parent in self.get_parent_ids() :
            self.parents[id_parent] += 1
        else : 
            self.parents[id_parent] = 1



    def remove_parent_once(self, id_parent):
        if id_parent in self.get_parent_ids() :
            if self.parents[id_parent] != 1:
                self.parents[id_parent] -= 1
            else:
                del self.parents[id_parent]
    
    def remove_child_once(self, id_child):
        if id_child in self.get_children_ids() :
            if self.children[id_child] != 1:
                self.chilren[id_child] -= 1
            else:
                del self.children[id_child]

    def remove_parent_id(self, id_parent):
        if id_parent in self.get_parent_ids() :
            del self.parents[id_parent]
    
    def remove_child_id(self, id_child):
        if id_child in self.get_children_ids() :
            del self.children[id_child]



    def indegree(self):
        a= 0
        for i in self.parents:
            a += self.parents[i]
        return a

    def outdegree(self):
        a = 0
        for i in self.children:
            a += self.children[i]
        return a
    
    def degree(self):
        return self.indegree + self.outdegree