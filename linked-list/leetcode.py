class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self, node=None):
        self.head = node
        if node:
            self.head.next = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def Merge_two_sortedLL(self, other_list):
        ptr1, ptr2 = self.head, other_list.head
        dummy_node = Node(-1)
        ptr = dummy_node

        while ptr1 and ptr2:
            if ptr1.data <= ptr2.data:
                ptr.next = ptr1
                ptr1 = ptr1.next
            else:
                ptr.next = ptr2
                ptr2 = ptr2.next
            ptr = ptr.next

        if ptr1:
            ptr.next = ptr1
        else:
            ptr.next = ptr2

        merged_list = Linked_List()
        merged_list.head = dummy_node.next
        return merged_list

    def display(self):
        current = self.head
        while current:
            print(current.data, "--> ", end="")
            current = current.next
        print("NONE")

# Example usage:
n1 = Node(1)
LL1 = Linked_List(n1)
LL1.append(2)
LL1.append(4)
LL1.display()

n2 = Node(1)
LL2 = Linked_List(n2)
LL2.append(3)
LL2.append(4)
LL2.display()

LL3 = LL1.Merge_two_sortedLL(LL2)
LL3.display()
