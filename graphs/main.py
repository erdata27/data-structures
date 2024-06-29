class Queue:
    def __init__(self):
        self.queue = []

    def addq(self,v):
        self.queue.append(v)

    def delq(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return(v)
    
    def isempty(self):
        return(self.queue == [])

    def __str__(self):
        return(str(self.queue))

import numpy as np 

def Adjacency_matrix(n,E):#list of tuples(edges)
      Amat=np.zeros(shape=(n,n))#creating an array of all entries zero,size n cross n 
      for (i,j) in E:
        Amat[i,j]=1  #assign value 1 to index[i][j] as E is list of edges
      return Amat
def neighbours_of_vertex(Amat,i):#i is the vertex number which we have to find neighbours
      nbrs=[]
      (rows,cols)=Amat.shape
      for j in range(cols):
           if Amat[i,j]==1:
                nbrs.append(j)
      return nbrs

  