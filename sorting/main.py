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
      elif A[i]<=B[j]:
         C.append(A[i])
         (i,k)=(i+1,k+1)
      elif B[j]<=A[i]:
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
      swapped=False
      for j in range(0,n-1-i):
         #traverse the list till n-1-i
         #swap if the element found is greater than next 
         if L[j]>L[j+1]:
            (L[j],L[j+1])=(L[j+1],L[j])
             swapped=True
      #if no two elements are swapped in the inner loop then list is sorted 
      if not swapped:
         break
   return L

def Quickort(L,l,r):# sort L[l:r]
   if r-l<=1: # check if slice has atmost one elem,this is the base condition
      return L
   # intialise pivot,lower pointer and upper pointer
   (pivot,lower,upper)=(L[l],l+1,l+1)
   
   for i in range(l+1,r):
      if L[i]>pivot:#if elem in unclassified is greater than pivot then extend upper
         upper=upper+1
      else:#if not i.e <pivot then swap L[i],L[lower]   example: 43,<<32,<<22,>>78{lower},>>63,>>57,>>91,<<13{upper}here pivot is 43,<< is lower ,>>is upper and 13 should be wapped with begin elem of upper i.e at index lower 
         (L[i],L[lower])=(L[lower],L[i])
         (lower,upper)=(lower+1,upper+1)
   #swap pivot and and last lower elem  to make Lower-elems Pivot  upper-elems
   (L[pivot],L[lower-1])=(L[lower-1],L[pivot])
   lower=lower-1 # make lower to point elem before pivot after swaping
   #recursive calls to sort lowersegment and upper segment 
   Quickort(L,l,lower) 
   Quickort(L,lower+1,r)



print(mergesort([2,2,33,4,2,22,56,90,45]))
