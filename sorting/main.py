def selectionsort(L):#time complexity of this algorithm is O(n^2)
    n=len(L)
    if n<1:#if list is empty return list
      return L
    for i in range(n):
       #assume that L[:i] is sorted 
       mpos=i
       #mpos: position of the minimun in L[:i]
       for j in range(i+1,n):
          if L[j]<L[mpos]:
              mpos=j 
       #mpos is the smallest value in L[i:]
       #exchange L[mpos and L[i]]
       (L[mpos],L[i])=(L[i],L[mpos])
       #now L[:i+1] is sorted 
    return L

def insertionsort(L):
    n=len(L)
    if n<1:#if the list is empty return L
       return L
    for i in range(n):
       #assume that L[:i] is sorted 
       #move L[i] to correct position in L 
       j=i
       while(j>0 and L[j]<L[j-1]):
         (L[j],L[j-1])=(L[j-1],L[j])
         j=j-1
       #now L[:i+1] is sorted
    return L 

def insert(L,v):
   n=len(L)
   if n==0: # if list is empty return L
      return L
   if v>L[-1]: #if v is larger then Last element append it to list 
      return L+[v]
   else:
      return insert(L[:-1],v)+L[-1:] #if v is less than last recursively do above step compare with last elem of L[:-1] i.e L[-2] if it is larger than that append like above if not repeat this step 

def Isort(L):
   n=len(L)
   if n<1: # base condition 
      return L
   L=insert(Isort(L[:-1]),L[-1]) # trying to insert L[-1] in inductively sorted L[:-1]
   return L
   
def merge(A,B):
   (m,n)=(len(A),len(B))
   (C,i,j,k)=([],0,0,0)
   while k<m+n:
      if i==m:#A is exhausted
         C.extend(B[j:]) #copy all B values into C
         k=k+n-j
      elif j==n:#B is exhausted
         C.extend(A[i:])#copy all A values into C
         k=k+m-i
      elif A[i]<B[j]:
         C.append(A[i])
         (i,k)=(i+1,k+1)
      elif B[j]<A[i]:
         C.append(B[j])
         (j,k)=(j+1,k+1)
   return C 

def mergesort(A):
   n=len(A)
   if n<=1: #base case 
      return A
   L=mergesort(A[ :n//2]) # sorted left half of A
   R=mergesort(A[n//2: ])#sorted right half of A
   B=merge(L,R)# merging two sorted lists
   return B
 
def bubblesort(L):
   n=len(L)
   #traverse the list 
   for i in range(n):
      #track if any swapping happens
      swapped=True
      for j in range(0,n-i-1):
         #traverse the list till n-i-1
         #swap if the element found is greater than next 
         if L[j]>L[j+1]:
            (L[j],L[j+1])=(L[j+1],L[j])
      #if no two elements are swapped in the inner loop then list is sorted 
      if not swapped:
         break
   return L






          
   