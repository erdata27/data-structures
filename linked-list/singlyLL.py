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
            if self.head==None:
                  return 'memory allocation failed'
            elif self.head!=None:
                  current=self.head
                  while(current.next!=None):
                        current=current.next
                  new_node.next=None
                  current.next=new_node
            return self.head
      def insertion_at_beginning(self,new_node):
            if self.head==None:
                  self.head=new_node
            else:
                  new_node.next=self.head
                  self.head=new_node
            return self.head
      def insertion_at_index(self,new_node,index):
            ptr=self.head
            for i in range(0,index-1):
                  ptr=ptr.next
            new_node.next=ptr.next
            ptr.next=new_node
            return self.head
      def display(self):
            current=self.head
            while(current!=None):
                  print(current.data,"--> ",end="")
                  current=current.next
            print("NONE",end="")


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
n7=Node(90)
LL.insertion_at_index(n7,5)
LL.display()
            
                  
                  
                  
                  




                        


                  
                  
                     

            