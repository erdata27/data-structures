class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head =None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        current = self.head

        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  # if node to be deleted is head node
                    self.head = current.next
                return
            current = current.next

    def display_forward(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        return nodes

    def display_backward(self):
        nodes = []
        current = self.head
        if current is None:
            return nodes
        while current.next:
            current = current.next
        while current:
            nodes.append(current.data)
            current = current.prev
        return nodes

    def insert_after(self, prev_node_data, data):
        current = self.head
        while current:
            if current.data == prev_node_data:
                new_node = Node(data)
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next

    def insert_before(self, next_node_data, data):
        current = self.head
        while current:
            if current.data == next_node_data:
                new_node = Node(data)
                new_node.next = current
                new_node.prev = current.prev
                if current.prev:
                    current.prev.next = new_node
                else:
                    self.head = new_node
                current.prev = new_node
                return
            current = current.next

# Example usage:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
print("Forward:", dll.display_forward())   # [1, 2, 3]
print("Backward:", dll.display_backward()) # [3, 2, 1]

dll.prepend(0)
print("After prepend:", dll.display_forward()) # [0, 1, 2, 3]

dll.insert_after(2, 2.5)
print("After inserting 2.5 after 2:", dll.display_forward()) # [0, 1, 2, 2.5, 3]

dll.insert_before(2, 1.5)
print("After inserting 1.5 before 2:", dll.display_forward()) # [0, 1, 1.5, 2, 2.5, 3]

dll.delete(1.5)
print("After deleting 1.5:", dll.display_forward()) # [0, 1, 2, 2.5, 3]
