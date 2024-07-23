class max_heap:
    def __init__(self):
        self.A=[]
    #heapify funtion to swap in build heap 
    def max_heapify(self,k):
        l=2*k+1
        r=2*k+2
        largest=k
        if l<len(self.A) and self.A[l]>self.A[largest]:
            largest=l
        if r<len(self.A) and self.A[r]>self.A[largest]:
            largest=r
        if largest!=k:
            (self.A[largest],self.A[k])=(self.A[k],self.A[largest])
            self.heapify(largest)
    #build heap function starts from leaf nodes fixes them goes level up time complexity is O(n)
    def build_heap(self,L):
        self.A=[]
        for each in L:
            self.A.append(each)
        n=int((len(self.A)//2)-1)
        for k in range(n,-1,-1):
            self.max_heapify(k)
    #intaillly insert at left of heap then fing its correct position by comparing with its parent is greater swap both time complexcity of this algorithm is O(logn)
    def insert_in_maxheap(self,data):
        self.A.append(data)
        index=len(self.A)-1
        while(index>0):
            parent=(index-1)//2  #updating index
            if self.A[index]>self.A[parent]:
                (self.A[index],self.A[parent])=(self.A[parent],self.A[index])
            else:
                break
    #deleting max mean del the root of the tree,before u delete the root swap it with last item in heap bcoz if we delete the root tree will  vanish time complexity of this algorithm is O(logn)
    def del_max(self):
        item=None
        if self.A!=[]:
            (self.A[-1],self.A[0])=(self.A[0],self.A[-1])
            item=self.A.pop()
            self.max_heapify(0)
        return item 

class min_heap:
    def __init_(self):
        self.A=[]
    def min_heapify(self,k):
        l=2*k+1
        r=2*k+2
        smallest=k
        if l<len(self.A) and self.A[l]<self.A[smallest]:
            smallest=l
        if r<len(self.A) and self.A[r]<self.A[smallest]:
            smallest=r
        if smallest!=k:
           (self.A[smallest],self.A[k])=(self.A[k],self.A[smallest])
           self.min_heapify(smallest)

    def build_min_heap(self,L):
        self.A = []
        for each in L:
            self.A.append(each)
        n = int((len(self.A)//2)-1)
        for k in range(n, -1, -1):
            self.min_heapify(k)
    def insert_in_minheap(self,data):
        self.A.append(data)
        index = len(self.A)-1
        while index > 0:
            parent = (index-1)//2
            if self.A[index] < self.A[parent]:
                self.A[index],self.A[parent] = self.A[parent],self.A[index]
                index = parent
            else:
                break

    def delete_min(self):
        item = None
        if self.A != []:
            self.A[0],self.A[-1] = self.A[-1],self.A[0]
            item = self.A.pop()
            self.min_heapify(0)
        return item



