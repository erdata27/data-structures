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


#Find level number of vertices using BFS
#Maintain level information to record length of the shortest path, in terms of number of edges or vertex.
# Using BFS approch For Adjacency list, for path, maintaining the parent of each vertex
# Using BFS approch maintaing the adjacent level number from source vertrex
def BFSListPathLevel(AList,v):
    # Initialization
    (level,parent) = ({},{})
    for each_vertex in AList.keys():
        level[each_vertex] = -1
        parent[each_vertex] = -1
    
    # Create Queue object q
    q = Queue()
    
    # Assigning the level 0 for start_vertex and insert it into the queue
    level[v] = 0
    q.enqueue(v)
    
    # Repeat the following until the queue is empty
    while(not q.isempty()):
        # Remove the one vertex from queue
        curr_vertex = q.dequeue()
        # Visit the each adjacent of curr_vertex(if level value is -1) and insert into the queue
        for adj_vertex in AList[curr_vertex]:
            if (level[adj_vertex] == -1):
                # Assign the level value on each adjacent one more than the curr_vertex level
                level[adj_vertex] = level[curr_vertex] + 1
                # Assigne the curr_vertex as parent of adjacent vertex of curr_vertex
                parent[adj_vertex] = curr_vertex
                q.enqueue(adj_vertex)
    return(level,parent)

# Using BFS approch For Adjacency list, for path, maintaining the parent of each vertex
# Using BFS approch maintaing the adjacent level number from source vertrex
def BFSListPathLevel(AList,v):
    # Initialization
    (level,parent) = ({},{})
    for each_vertex in AList.keys():
        level[each_vertex] = -1
        parent[each_vertex] = -1
    
    # Create Queue object q
    q = Queue()
    
    # Assigning the level 0 for start_vertex and insert it into the queue
    level[v] = 0
    q.enqueue(v)
    
    # Repeat the following until the queue is empty
    while(not q.isempty()):
        # Remove the one vertex from queue
        curr_vertex = q.dequeue()
        # Visit the each adjacent of curr_vertex(if level value is -1) and insert into the queue
        for adj_vertex in AList[curr_vertex]:
            if (level[adj_vertex] == -1):
                # Assign the level value on each adjacent one more than the curr_vertex level
                level[adj_vertex] = level[curr_vertex] + 1
                # Assigne the curr_vertex as parent of adjacent vertex of curr_vertex
                parent[adj_vertex] = curr_vertex
                q.enqueue(adj_vertex)
                
    return(level,parent)

#DFS Recursive (without using external stack) 
# Initialization Function
def DFSInitList(AList):
    (visited,parent) = ({},{})
    for each_vertex in AList.keys():
        visited[each_vertex] = False
        parent[each_vertex] = -1
    return(visited,parent)


# DFS Recursive Implementation for Adjacency list
def DFSList(AList,visited,parent,v):
    # Mark vertex v as visited vertex
    visited[v] = True
    # Repeat following for each unvisited adjacent of vertex v
    for adj_vertex in AList[v]:
        if (not visited[adj_vertex]):
            # Assign vertex v as parent of each unvisited adjacent of v 
            parent[adj_vertex] = v
            
            # Recursively call the DFS on unvisited adjacent of v
            (visited,parent) = DFSList(AList,visited,parent,adj_vertex)
            
    return(visited,parent)

# Global variable
(visited,parent) = ({},{})

# Initialization function
def DFSInitListGlobal(AList):   
    for each_vertex in AList.keys():
        visited[each_vertex] = False
        parent[each_vertex] = -1
    return

# DFS Recursive Implementation for Adjacency list
def DFSListGlobal(AList,v):
    # Mark vertex v as visited vertex
    visited[v] = True
    # Repeat following for each unvisited adjacent of vertex v
    for adj_vertex in AList[v]:
        if (not visited[adj_vertex]):
            # Assign vertex v as parent of each unvisited adjacent of v 
            parent[adj_vertex] = v
            # Recursively call the DFS on unvisited adjacent of v
            DFSListGlobal(AList,adj_vertex)                
    return


#DFS global for adjacency matrix of graph
# Function to return list of neighbours or adjacent vertex of vertex i
# def neighbours(AMat,i):
#     nbrs = []
#     (rows,cols) = AMat.shape
#     for j in range(cols):
#         if AMat[i,j] == 1:
#             nbrs.append(j)
#     return(nbrs)

# # Initialization Function
# def DFSInitGlobal(AMat):
#     (rows,cols) = AMat.shape    
#     for each_vertex in range(rows):
#         visited[each_vertex] = False
#         parent[each_vertex] = -1
#     return

# # DFS Recursive Implementation for Adjacency matrix
# def DFSGlobal(AMat,v):
#     # Mark vertex v as visited vertex
#     visited[v] = True
#     # Repeat following for each unvisited adjacent of vertex v
#     for adj_vertex in neighbours(AMat,v):
#         if (not visited[adj_vertex]):
#             # Assign vertex v as parent of each unvisited adjacent of v
#             parent[adj_vertex] = v
#             # Recursively call the DFS on unvisited adjacent of v
#             DFSGlobal(AMat,adj_vertex)                
#     return

# Implementation of Topological sort for Adjacency list
def toposortlist(AList):
    # Initialization
    (indegree,toposortlist) = ({},[])
    zerodegreeq = Queue()
    for u in AList.keys():
        indegree[u] = 0
    
    # Compute indegree for each vertex
    for u in AList.keys():
        for v in AList[u]:
            indegree[v] = indegree[v] + 1
    
    # Find the vertex with indegree 0 and added into the queue
    for u in AList.keys():
        if indegree[u] == 0:
            zerodegreeq.enqueue(u)
    
    # Topological sort Computing process
    while (not zerodegreeq.isempty()):
        # Remove one vertex from queue which have zero degree vertices
        curr_vertex = zerodegreeq.dequeue()       
        # Store the removed vertex in toposortlist and reduce the indegree by one 
        toposortlist.append(curr_vertex)
        indegree[curr_vertex] = indegree[curr_vertex]-1
        
        # Repeat for each adjacent of the removed vertex
        for adj_vertex in AList[curr_vertex]:
            # Reduce the indegree of each adjacent of the removed vertex by 1
            indegree[adj_vertex] = indegree[adj_vertex] - 1
            # If after reducing the degree of adjacent, it becomes zero then insert it into the queue
            if indegree[adj_vertex] == 0:
                zerodegreeq.enqueue(adj_vertex)                
    
    return(toposortlist)



# Implementation Longest path on DAG for Adjacency list
def longestpathlist(AList):
    # Initialization
    (indegree,lpath) = ({},{})
    zerodegreeq = Queue()
    for u in AList.keys():
        (indegree[u],lpath[u]) = (0,0)
    
    # Compute indegree for each vertex
    for u in AList.keys():
        for v in AList[u]:
            indegree[v] = indegree[v] + 1

    # Find the vertex with indegree 0 and added into the queue
    for u in AList.keys():
        if indegree[u] == 0:
            zerodegreeq.enqueue(u)
            
    # Longest path computing process            
    while (not zerodegreeq.isempty()):
        # Remove one vertex from queue which have zero degree vertices and reduce the indegree by 1
        curr_vertex = zerodegreeq.dequeue()
        indegree[curr_vertex] = indegree[curr_vertex] - 1
        
        # Repeat for each adjacent of the removed vertex 
        for adj_vertex in AList[curr_vertex]:
            # Reduce the indegree of each adjacent of the removed vertex by 1
            indegree[adj_vertex] = indegree[adj_vertex] - 1
            # Assign the longest path value for each adjacent of the removed vertex
            lpath[adj_vertex] = max(lpath[adj_vertex],lpath[curr_vertex]+1)
            # If after reducing the degree of adjacent, it becomes zero then insert it into the queue
            if indegree[adj_vertex] == 0:
                zerodegreeq.enqueue(adj_vertex)
                
    return(lpath)




