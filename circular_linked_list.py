class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularsinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break


    def create_circular_linked_list(self, nodevalue):
        node = Node(nodevalue)
        node.next = node
        self.head = node
        self.tail = node
        return "ths CSLL has been created"

    def insert_circular_linked_list(self, value, location):
        if self.head is None:
            return "The head reference is none"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                temporarynode = self.head
                index = 0
                while index < location - 1:
                    temporarynode = temporarynode.next
                    index += 1
                nextNode = temporarynode.next
                temporarynode.next = newNode
                newNode.next = nextNode
            return "the node has been succesfully inserted"

    def traversalCSLL(self):
        if self.head is None:
            print("There is not any element for traversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    def searchCSLL(self, nodeValue):
        if self.head is None:
            return "There is not any node in this CSLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "The node does not exist in this CSLL"


csll = CircularsinglyLinkedList()
print(csll.create_circular_linked_list(1))
csll.insert_circular_linked_list(0, 0)
csll.insert_circular_linked_list(2, 1)
csll.insert_circular_linked_list(3, 1)

print([node.value for node in csll])
