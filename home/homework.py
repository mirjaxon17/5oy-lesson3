class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        #tugunning boshlanishi

    def printList(self):
        temp = self.head
        #endi bu tugunning boshi (temp)
        while temp:
            print(temp.data)
            temp=temp.next

    def push(self, new_data):
        #listning boshiga element qoshish
        new_node = Node(new_data)
        #(new_node) endi bu boshi
        new_node.next = self.head
        #(self.head) yangi qoshilgan element boshiga otadi, 
        # a bu elementdan olding element ikkinchiga otadi
        self.head = new_node
        #(self.head = new_node) bu yerda yangi element qatorda birinchiga
        #aylanadi, a qolganlar bitta qator suriladi

    def insert(self, prev_node, new_data):
        #listning ixtiyoriy nuqtasiga element qoshish
        if prev_node is None:
            print("Error")
        #bu yerda tekshiruv ketadi (yani "prev_node" oldingi qator None
            #teng bolsa print(Error) qaytaradi, bu yerga element qoshib bomaydi)
        new_node = Node(new_data)
        #yangi element qoshamiz bunda undan oldingi tugunni uzub uning 
        #qiymatini oziga oladi
        new_node.next = prev_node.next
        # yangi tugundi ong tomondagi elementga boglaymiz
        prev_node.next = new_node
        # yangi tugundi endi chap tomonga ulaymiz
    
    def append(self, new_data):
        # elementni oxiriga aqoshish
        new_node = Node(new_data)
        #yangi element (Node)ga qoshilyapti
        if self.head is None:
                self.head = new_node
        #bu yerda tekshiruv ketadi (yani "self.head" oldingi qator None
            #teng bolsa tugunning boshiga new_node qoshadi)
        last = self.head
        # last yangi elementni oziga olyapti
        while last.next:
                #bu yerda last.next oxiri none teng bolmaguncha tekshiryapti
                last = last.next
                #bu yerda ?
        last.next = new_node
        # bu yerda last.next = yangi qoshilgan otribudni oz ichiga olyapti


a = Node(3)
b = Node(14)
c = Node(25)
d = Node(36)
g = Node(45)
ll = Linkedlist()
ll.head = a
a.next = b
b.next = c
c.next = d
d.next = g

"""push"""
# ll.push(65)
# # ll.push(54)
# # ll.push(76)
# # ll.push(33)
# # ll.push(88)

"""insert"""
# ll.insert(a, 2)
# ll.insert(b, 15)
# ll.insert(a, 26)
# ll.insert(a, 34)
# ll.insert(a, 78)

"""append"""
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.append(5)
ll.printList()


        
