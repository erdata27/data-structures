class Node:
      def __init__(self,data):
            self.data=data
            self.next=None
class Linked_List:
      def __init__(self,node):
            self.head=node
            self.head.next=None

      def append(self,data):
            nnode=Node(data)
            if self.head!=None:
               current = self.head
               while current.next != None:
                  current = current.next
            current.next = nnode
      def insert_at_end(self,new_node):
            if self.head==None: #if head is None then return string 
                  return 'memory allocation failed'
            elif self.head!=None:# else if head!=None then traverse linked list till current reaches the last 
                  current=self.head
                  while(current.next!=None):
                        current=current.next
                  new_node.next=None
                  current.next=new_node
            
      def insertion_at_beginning(self,new_node):
            if self.head==None:
                  self.head=new_node
            else:#link newnode to head first then assign head to newnode
                  new_node.next=self.head
                  self.head=new_node

      def insertion_at_index(self,new_node,index):
            ptr=self.head
            for i in range(0,index-1):
                  ptr=ptr.next
            new_node.next=ptr.next
            ptr.next=new_node
            
      def display(self):
            current=self.head
            while(current!=None):
                  print(current.data,"--> ",end="")
                  current=current.next
            print("NONE")

      def deleteNode(self, key): 
        current = self.head
        # If head node itself holds the key to be deleted 
        if current is not None and self.head.data==key:
                self.head = current.next
                current = None
                return
        # Search for the key to be deleted, keep track of the 
        # previous node as we need to change 'prev.next' 
        while(current.next!=None): 
            if current.data == key: 
                break
            prev = current 
            current = current.next
 
        # if key was not present in linked list 
        if(current==None): 
            return
 
        # Unlink the node from linked list 
        prev.next = current.next
 
        current=None
      def i_search(self,key):
            current=self.head
            if self.head==key:
                  return "head is the element\n"
            else:
                  while(current.next!=None and current.data!=key):
                        current=current.next
                  if current.data==key:
                        return "element is in this linked list\n"
                  else:
                        return "element not found"
      def r_search(self,ln,key):
            # Base case ln = none means we have reached the end of the linked list 
            if ln==None:
                  return "element not found"
            # If key is present in
            # current node, return elem found
            if ln.data==key:
                  return "element is in this linked list"
            #if the key is not found in the current node, the function calls itself recursively with the next node (ln.next) and the same key. This continues the search in the remaining part of the linked list.
            return self.r_search(ln.next,key)
      
      def i_length(self):
            current=self.head
            count=0 # intialise count to zero 
            while(current!=None):# traversal of entire linked list
                  count+=1 #increment while leaving form a node 
                  current=current.next # moving to next node 
            return count
      
      def r_length(self,ln,count):
            #base case it means we have travelled  entire list
            if ln == None:
                  return count
            else:
                  count+=1
                  return self.r_length(ln.next,count)
      def reverseLL(self):
            prev=None
            current=self.head
            while(current!=None):
                  next=current.next
                  current.next=prev
                  prev=current
                  current=next
            self.head=prev  
      def deleteLL(self):
            self.head=None
            return  
      def nth_node(self,n): 
            current=self.head
            for i in range(n-1):
                  current=current.next
            return current
      def nth_from_last_node(self,n):
            l=self.i_length()
            current=self.head
            for i in range(l-n):
                  current=current.next
            return current.data
      def print_middle(self):
            l=self.i_length()
            current=self.head
            for i in range((l//2)):
                  current=current.next
            return current.data


LL=Linked_List(Node(8))
LL.append(3)
LL.append(5)
LL.append(1)
LL.append(3)
LL.append(5)
LL.display() 


                  
               
                  




                        


                  
                  
                     

            