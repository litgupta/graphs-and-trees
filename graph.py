from collections import defaultdict
from numpy import *

class Graph(object):
    def __init__(self):
        self.vertices=raw_input('Enter the vertices of the graph').strip().split(' ')
        self.vertices_dict={}
        for i in xrange(len(self.vertices)):
            self.vertices_dict[i]=self.vertices[i]
        self.create_Adjacency_matrix()
        
    def create_Adjacency_matrix(self):
        self.adj_list=[]
        for i in xrange(len(self.vertices)):
            for j in xrange(len(self.vertices)):
                self.response=int(raw_input('Is '+self.vertices_dict[i]+' and '+self.vertices_dict[j]+' connected? 1-or-0'))
                self.adj_list.append(self.response)
        self.adj_matrix=array(self.adj_list).reshape(len(self.vertices),len(self.vertices))
    def show_Adjacency_matrix(self):
        print self.adj_matrix

    def generate_Graph(self):
        self.elements=defaultdict(set)
        for i in xrange(self.adj_matrix.shape[0]):
            for j in xrange(self.adj_matrix.shape[1]):
                if self.adj_matrix[i][j]==1:
                    self.elements[self.vertices_dict[i]].add(self.vertices_dict[j])
        for i,j in self.elements.iteritems():
            print str(i)+'->'+str(j)
        
if __name__=='__main__':
    g1=Graph()
    g1.show_Adjacency_matrix()
    g1.generate_Graph()
