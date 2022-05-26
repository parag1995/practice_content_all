class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traverseSLL(self):
        if self.head is None:
            print("the list does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def search_inside_sll(self, nodeValue):
        if self.head is None:
            print("the list does not exist")
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "the value does not exist"

    def delete_node(self, location):
        if self.head is None:
            print("list does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                        node.next = None
                        self.tail = node
            else:
                tempnode = self.head
                index = 0
                while tempnode <location -1:
                    tempnode = tempnode.next
                    index +=1
                nextNode = tempnode.next
                tempnode.next = nextNode.next


singlylinkedlist = SinglyLinkedList()
singlylinkedlist.insertSLL(1,1)
singlylinkedlist.insertSLL(2,1)
singlylinkedlist.insertSLL(3,2)
singlylinkedlist.insertSLL(3,3)
# node1 = Node(1)
# node2 = Node(2)
# singlylinkedlist.head = node1
# singlylinkedlist.head.next = node2
# singlylinkedlist.tail = node2
print([node.value for node in singlylinkedlist])
# singlylinkedlist.traverseSLL()
# print(singlylinkedlist.search_inside_sll(5))