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
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, key):
        if self.head:
            if self.head.data == key:
                if self.head.next == self.head:
                    self.head = None
                else:
                    current = self.head
                    while current.next != self.head:
                        current = current.next
                    current.next = self.head.next
                    self.head = self.head.next
            else:
                current = self.head
                prev = None
                while current.next != self.head:
                    if current.data == key:
                        prev.next = current.next
                        return
                    prev = current
                    current = current.next
                if current.data == key:
                    prev.next = current.next

    def display(self):
        nodes = []
        if self.head:
            current = self.head
            while True:
                nodes.append(current.data)
                current = current.next
                if current == self.head:
                    break
        return nodes

    def insert_after(self, prev_node_data, data):
        if self.head:
            current = self.head
            while True:
                if current.data == prev_node_data:
                    new_node = Node(data)
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next
                if current == self.head:
                    break

    def insert_before(self, next_node_data, data):
        if self.head:
            current = self.head
            prev = None
            while True:
                if current.data == next_node_data:
                    new_node = Node(data)
                    new_node.next = current
                    if prev:
                        prev.next = new_node
                    else:
                        # Find the last node to update its next pointer
                        last = self.head
                        while last.next != self.head:
                            last = last.next
                        last.next = new_node
                        self.head = new_node
                    return
                prev = current
                current = current.next
                if current == self.head:
                    break

# Example usage:
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
print("Circular Linked List:", cll.display())  # [1, 2, 3]

cll.prepend(0)
print("After prepend:", cll.display())  # [0, 1, 2, 3]

cll.insert_after(2, 2.5)
print("After inserting 2.5 after 2:", cll.display())  # [0, 1, 2, 2.5, 3]

cll.insert_before(2, 1.5)
print("After inserting 1.5 before 2:", cll.display())  # [0, 1, 1.5, 2, 2.5, 3]

cll.delete(1.5)
print("After deleting 1.5:", cll.display())  # [0, 1, 2, 2.5, 3]
