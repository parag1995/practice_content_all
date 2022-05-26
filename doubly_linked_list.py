class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def create_dll(self,nodevalue):
        node = Node(nodevalue)
        node.previous = None
        node.next = None
        self.head = node
        self.tail = node
        return "the DLL is created successfully"

    def insert_dll(self,value, location):
        if self.head is None:
            print("Node cannot be inserted")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.previous = None
                newNode.next = self.head
                self.head.previous = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.previous = self.tail
                self.tail.next = newNode
                self.tail =newNode
            else:
                tempNode = self.head
                index = 0
                while index<location-1:
                    tempNode = tempNode.next
                    index+=1
                newNode.next = tempNode.next
                newNode.previous = tempNode
                newNode.next.previous = newNode
                tempNode.next = newNode

    def traverse_dll(self):
        if self.head is None:
            print("there is not any element to traverse")
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.next

    def reverse_traverse_dll(self):
        if self.head is None:
            print("there is not any element to traverse")
        else:
            tempnode = self.tail
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.previous

    def search_dll(self, value):
        if self.head is None:
            print("there is not any element to traverse")
        else:
            tempnode = self.head
            while tempnode:
                if tempnode.value == value:
                    return tempnode.value
                tempnode = tempnode.next
            return "the node does not exist in this list"

    def delete_node(self,location):
        if self.head is None:
            print("there is not any element in linked list")
        else:
            if location == 0:
                if self.head==self.tail:
                    self.head =None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.previous = None
            elif location == 1:
                if self.head==self.tail:
                    self.head =None
                    self.tail = None
                else:
                    self.tail = self.tail.previous
                    self.tail.next = None
            else:
                currentnode = self.head
                index = 0
                while index <location-1:
                    currentnode =currentnode.next
                    index +=1
                currentnode.next = currentnode.next.nex
                currentnode.previous = currentnode
            print("node is deleted successfully")
    def delete_dll(self):
        if self.head is None:
            print("There is no node in DLL")
        else:
            tempnode = self.head
            while tempnode:
                tempnode.previous = None
                tempnode = tempnode.next
            self.head = None
            self.tail = None
            print("the dll has been deleted successfully")

doubyll = DoublyLinkedList()
doubyll.create_dll(5)

print([node.value for node in doubyll])
doubyll.insert_dll(0,0)
doubyll.insert_dll(2,1)
doubyll.insert_dll(6,2)
print([node.value for node in doubyll])
# doubyll.traverse_dll()
# doubyll.reverse_traverse_dll()
# print(doubyll.search_dll(6))
# print(doubyll.delete_node(1))
doubyll.delete_dll()
print([node.value for node in doubyll])

