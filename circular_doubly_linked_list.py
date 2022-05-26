class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class CircularDoublyLinkedList:
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

    def create_cdll(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.previous = newNode
        newNode.next = newNode
        return "The CDLL created successfully"

    def insertion_cdll(self, value, location):
        if self.head is None:
            return "cdll does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.previous = self.tail
                self.head.previous = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.previous = self.tail
                self.head.previous = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                newNode.next = tempnode.next
                newNode.previous = tempnode
                newNode.next.previous = newNode
                tempnode.next = newNode
            return "the node has been successfully inserted"

    def traverse_cdll(self):
        if self.head is None:
            print("there is not any node for traversal")
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value)
                if tempnode == self.tail:
                    break
                tempnode = tempnode.next

    def reverse_traversal_cdll(self):
        if self.head is None:
            print("there is not any node for traversal")
        else:
            tempnode = self.tail
            while tempnode:
                print(tempnode.value)
                if tempnode == self.head:
                    break
                tempnode = tempnode.previous

    def search_cdll(self, value):
        if self.head is None:
            print("there is not any node for traversal")
        else:
            tempnode = self.head
            while tempnode:
                if tempnode.value == value:
                    return tempnode.value
                if tempnode == self.tail:
                    return " the vale does not exist"
                tempnode = tempnode.next

    def delete_node(self, location):
        if self.head is None:
            print("tehre is no node to delete")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.previous = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.previous = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.previous = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.previous
                    self.tail.next = self.head
                    self.head.previous = self.tail

            else:
                tempnode = self.head
                index = 0
                while index <location-1:
                    tempnode = tempnode.next
                    index +=1
                tempnode.next = tempnode.next.next
                tempnode.next.previous = tempnode
            print("the node has been deleted")

    def delete_cdll(self):
        if self.head is None:
            print("no node in list")
        else:
            self.tail.next = None
            tempnode = self.head
            while tempnode:
                tempnode.previous = None
                tempnode = tempnode.next
            self.head = None
            self.tail = None
            print("list deleted")



circulardll = CircularDoublyLinkedList()
print(circulardll.create_cdll(5))
circulardll.insertion_cdll(0, 0)
circulardll.insertion_cdll(1, 1)
circulardll.insertion_cdll(2, 2)
print([node.value for node in circulardll])
# circulardll.traverse_cdll()
# print("cirecular in reverse")
# circulardll.reverse_traversal_cdll()
# print("check for search")
# print(circulardll.search_cdll(2))
circulardll.delete_node(-1)
print([node.value for node in circulardll])
circulardll.delete_cdll()
print([node.value for node in circulardll])