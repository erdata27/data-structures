# Queue Implementation
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,v):
        self.queue.append(v)
    def isempty(self):
        return(self.queue == [])
    def dequeue(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return(v)    
    
    def __str__(self):
        return(str(self.queue))

import numpy as np 
# G=(V,E) V is list of vertices and E is list of tuples (i,j) where there is an edge between i and j

def Adjacency_matrix(n,E):#list of tuples(edges),n is len(V)
      Amat=np.zeros(shape=(n,n))#creating an array of all entries zero,size n cross n 
      for (i,j) in E:
        Amat[i,j]=1  #assign value 1 to index[i][j] as E is list of edges
      return Amat
def Adjacency_list(n,E):
      #V = [0,1,2,3,4],E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)] ,n=len(v),
      #{0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
      # for example, AList[i] = [j,k] represent two edge from i to j and i to k
      Alist={}
      for i in range(n):
          Alist[i]=[]
      for (i,j) in E:
          Alist[i].append(j)
      return Alist
# Function to return list of neighbours or adjacent vertex of vertex i
def neighbours(Amat,i):
    nbrs=[]  # create an empty list to store neighbours of i 
    (rows,cols)=Amat.shape
    for  j in range(cols):
        if Amat[i,j]==1:
            nbrs.append(j)
    return nbrs

# BFS Implementation For Adjacency matrix
def BFS(AMat,start_vertex):
    # Initialization
    (rows,cols) = AMat.shape
    visited = {}
    for each_vertex in range(rows):
        visited[each_vertex] = False    
    
    # Create Queue object q
    q = Queue()
    
    # Mark the start_vertex visited and insert it into the queue 
    visited[start_vertex] = True
    q.enqueue(start_vertex)
    
    # Repeat the following until the queue is empty 
    while(not q.isempty()):
        # Remove the one vertex from queue
        curr_vertex = q.dequeue()
        # Visit the each adjacent of removed vertex(if not visited) and insert into the queue
        for adj_vertex in neighbours(AMat,curr_vertex):
            if (not visited[adj_vertex]):
                visited[adj_vertex] = True
                q.enqueue(adj_vertex)
                
    return(visited)

#Implementation BFS for adjacency list of graph
def BFSList(AList,start_vertex):
    # Initialization
    visited = {}
    for each_vertex in AList.keys():
        visited[each_vertex] = False    
    
    # Create Queue object q
    q = Queue()
    
    # Mark the start_vertex visited and insert it into the queue 
    visited[start_vertex] = True
    q.enqueue(start_vertex)
    
    # Repeat the following until the queue is empty 
    while(not q.isempty()):
        # Remove the one vertex from queue
        curr_vertex = q.dequeue()
        # Visit each adjacent of the removed vertex (if not visited), mark that visited, and insert it into the queue 
        for adj_vertex in AList[curr_vertex]:
            if (not visited[adj_vertex]):
                visited[adj_vertex] = True
                q.enqueue(adj_vertex)               
    return(visited)
#Find parent of each vertex using BFS,
#Parent information is useful to determine shortest path from vertex v in term of number of edges or vertex in path.
# Using BFS approch For Adjacency list, for path, maintaining the parent of each vertex
# Path can be found by backtracking from destination to source using parent information
def BFSListPath(AList,start_vertex):
    # Initialization
    (visited,parent) = ({},{})
    for each_vertex in AList.keys():
        visited[each_vertex] = False
        parent[each_vertex] = -1   
    
    # Create Queue object q
    q = Queue()
    
    # Mark the start_vertex visited and insert it into the queue 
    visited[start_vertex] = True
    q.enqueue(start_vertex)
    
    # Repeat the following until the queue is empty
    while(not q.isempty()):
        # Remove the one vertex from queue
        curr_vertex = q.dequeue()
        # Visit the each adjacent of removed vertex(if not visited) and insert into the queue
        for adj_vertex in AList[curr_vertex]:
            if (not visited[adj_vertex]):
                visited[adj_vertex] = True
                # Assigne the curr_vertex as parent of each unvisited adjacent of curr_vertex
                parent[adj_vertex] = curr_vertex
                q.enqueue(adj_vertex)
                
    return(visited,parent)


AList ={0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
print(BFSListPath(AList,2))






