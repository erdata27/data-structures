class Node:
      def __init__(self,data):
            self.data=data
            self.next=None
      def get_data(self):
            return self.data
      def get_next(self):
            return self.next
      def set_next(self,next_node):
            self.next=next_node
class Linked_List:
      def __init__(self,node):
            self.head=node
            self.next=None
      def insertion_at_end(self,new_node):
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
            print("NONE",end="")

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
  
            

n1=Node(1)
n2=Node(3)
n3=Node(6)
n4=Node(8)
n5=Node(9)
n6=Node(20)
LL=Linked_List(n1)
LL.insertion_at_end(n2)
LL.insertion_at_end(n3)
LL.insertion_at_end(n4)
LL.insertion_at_end(n5)
LL.insertion_at_end(n6)
# n7=Node(90)
# LL.insertion_at_index(n7,5)
LL.deleteNode(9)
LL.display()
                  
                  
                  
                  




                        


                  
                  
                     

            