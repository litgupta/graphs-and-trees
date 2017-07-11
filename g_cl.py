from collections import defaultdict

class graph(object):
    
    connections=defaultdict(list)

    def __init__(self):
        nodes=raw_input('Enter the nodes of the ').strip().split(' ')
        self.connect(nodes)
    
         
    def connect(self,nodes):
        for node in nodes:
            for j in nodes:
                option=int(raw_input('Is '+node+' and '+j+' connected ? (0/1)'))
                if option==1:
                   self. connections[node].append(j)
        print '\nFinal Connections: ' 
        for i,j in self.connections.items():
            print str(i)+' ->'+str(j)
   

    def get_path(self):
        s,e=raw_input('Enter the start and end nodes to find path').strip().split(' ')
        return self.find_path(self.connections,s,e,[])


    def find_path(self,graph,start,end,path):
        if not graph.has_key(start):
            return None
        else:
            if start==end:
                return path
            else:
                path+=[start]
                for node in graph[start]:
                    if node not in path:
                        newpath=self.find_path(graph,node,end,path)
                        if newpath : return newpath
                return None

G=graph()
print G.get_path()
