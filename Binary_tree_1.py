
import queue_using_link_list as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBt =TreeNode('Drinks')
leftchild = TreeNode('hot')
rightchild = TreeNode('cold')
tea = TreeNode('tea')
coffee = TreeNode('coffee')
leftchild.leftChild = tea
leftchild.rightChild = coffee
newBt.leftChild = leftchild
newBt.rightChild = rightchild

def pre_order_traversal(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    pre_order_traversal(rootnode.leftChild)
    pre_order_traversal(rootnode.rightChild)

pre_order_traversal(newBt)

def inorder_traversal(rootnode):
    if not rootnode:
        return
    inorder_traversal(rootnode.leftChild)
    print(rootnode.data)
    inorder_traversal(rootnode.rightChild)

inorder_traversal(newBt)

def post_order_traversal(rootnode):
    if not rootnode:
        return
    post_order_traversal(rootnode.leftChild)
    post_order_traversal(rootnode.rightChild)
    print(rootnode.data)

def level_order_traversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.is_empty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
def searchBT(rootnode, nodeValue):
    if not rootnode:
        return "The BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootnode)
        while not(customQueue.is_empty()):
            root = customQueue.dequeue()
            if root.value.data ==nodeValue:
                return "success"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Not found"

def insert_node(rootNode,newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customqueue = queue.Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.is_empty()):
            root = customqueue.dequeue()
            if root.value.leftChild is not None:
                customqueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "successfully inserted node"
            if root.value.rightChild is not None:
                customqueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "successfully inserted node"

def get_deepest_node(rootNode):
    if not rootNode:
        return
    else:
        customqueue = queue.Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.is_empty()):
            root = customqueue.dequeue()
            if root.value.leftChild is not None:
                customqueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customqueue.enqueue(root.value.rightChild)


newNode = TreeNode("cola")
print(insert_node(newBt,newNode))
print(level_order_traversal(newBt))