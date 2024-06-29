
class Stack:
    def __init__(self):
        self.stack = []
    def isempty(self):
        return(self.stack == [])
    def Push(self,v):
        self.stack.append(v)
    def Pop(self):
        v = None
        if not self.isempty():
            v = self.stack.pop()
        return v    
    def __str__(self):
        return(str(self.stack))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLL:
    def __init__(self):
        self.top = None
        
    def isempty(self):
        if self.top == None: 
            return True
        else:
            return False

    def Push(self,data):
        if self.isempty():
            self.top = Node(data)
        else:
            temp = Node(data)
            temp.next = self.top
            self.top = temp

    def Pop(self):
        if self.isempty() == True:
            return None
        else:
            temp = self.top.data
            self.top = self.top.next
            return temp

    def display(self):
        if self.isempty()==True:
            return None
        else:
            temp = self.top
            while temp != None:
                print(temp.data)
                temp = temp.next       



S = StackLL()
S.Push(10)
S.Push(20)
S.Push(30)
S.Push(40)
print(S.Pop())
print(S.Pop())
S.display()