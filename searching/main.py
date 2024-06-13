def linear_search(L,key): #time complexity of this search is O(n) space complexity is O(1)
    for elem in L: #looping through this list L
        if key==elem: # checking wheather key is equal to elem or not 
            return True 
    return False



#iterative binary search algorithm
#left and right are pointers pointing case list starting and ending point ,mid is avg of left and right it should be updated for each iteration
def i_binary_search(L,key):#time complexity of this code is O(logn)
    n=len(L)
    left=0
    right=n-1
    while(right-left>1):#loop condition is if left,right are not concecutiv, get into the loop
        mid=left+right//2
        if key==L[mid]:
            return True 
        elif key>L[mid]:
            left=mid+1
        elif key<L[mid]:
            right=mid-1
    if key==L[left] or key==L[right]:
        return True
    else:
        return False

def bsearch(key,L):#time complexity of this method is O(logn)
    n=len(L)
    if L==[]:
        return False
    mid=n//2
    if key>L[mid]:
        return bsearch(key,L[mid+1:])
    else:
        return bsearch(key,L[:mid])
def r_binary_search(L,key,left,right):
    mid=left+right//2

    if(left==right):
        if(L[left]==key):
            return True
        return False

    if(right-left==1):
        if(L[left]==key or L[right]==key):
            return True
        return False

    if(right-left>1):
        if(L[mid]==key):
            return True
        if(key>L[mid]):
            return r_binary_search(L,key,mid+1,right)
        if(key<L[mid]):
            return r_binary_search(L,key,left,mid-1)

    if(left-right<0):
        return False
    
    return False  


L=[1,2,11,312,554,999,9100]
print(r_binary_search(L,0,0,len(L)-1))