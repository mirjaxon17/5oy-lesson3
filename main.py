class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


    def push(self, new_data):
        # listning boshiga element qo'shish
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def insert(self, prev_node, new_data):
        # listning ixtiyoriy nuqtasiga element qo'shish
        if prev_node is None:
            print("Error")
        # yangi element qo'shamiz
        new_node = Node(new_data)
        # yangi tugunni keyingi elementga bog'laymiz
        new_node.next = prev_node.next
        # avvalgi tugunni yangi elementga bog'laymiz
        prev_node.next = new_node


    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

#
a = Node(5)
b = Node(7)
c = Node(9)
d = Node(11)
ll = LinkedList()
ll.head = a
a.next = b
b.next = c
c.next = d
# f = Node(45)
# ll.push(25)
ll.insert(b, 89)
ll.printList()

# print("Linked 1")
# ll.printList()

# ll1 = LinkedList()
# ll1.head = f

# print("Linked 2")
# ll1.printList()


# data = list(range(100))
# ll = LinkedList()

# a = Node(data[0])
# ll.head = a
# for i in range(1, len(data)):
#     b = Node(data[i])
#     a.next = b
#     a = b

# print("After")
# ll.printList()
# print("____________________________________________________")
# ll.push(89)
# print("Before")
# ll.printList()