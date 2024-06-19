class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        nodes = []
        while True:
            nodes.append(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        print("Circular Linked List:", " -> ".join(map(str, nodes))," -> ",self.head.data,"(head)")

    def delete(self, key):
        if self.head:
            if self.head.data == key:
                if self.head.next == self.head:
                    self.head = None
                else:
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next
                    temp.next = self.head.next
                    self.head = self.head.next
            else:
                temp = self.head
                prev = None
                while temp.next != self.head:
                    prev = temp
                    temp = temp.next
                    if temp.data == key:
                        prev.next = temp.next
                        temp = temp.next

    def __len__(self):
        count = 0
        if not self.head:
            return count
        temp = self.head
        while True:
            count += 1
            temp = temp.next
            if temp == self.head:
                break
        return count

# Example usage:
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.display()  # Output: Circular Linked List: 1 -> 2 -> 3 (head -> ... -> head)
cll.prepend(0)
cll.display()  # Output: Circular Linked List: 0 -> 1 -> 2 -> 3 (head -> ... -> head)
cll.delete(2)
cll.display()  # Output: Circular Linked List: 0 -> 1 -> 3 (head -> ... -> head)
print(f"Length of list: {len(cll)}")   # Output: Length of list: 3
