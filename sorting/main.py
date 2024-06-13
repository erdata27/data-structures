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

