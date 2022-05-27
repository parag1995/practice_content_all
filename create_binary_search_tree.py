import queue_using_link_list as queue
class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

def insert_node(rootNode, value):
    if rootNode.data is None:
        rootNode.data = value
    elif value <= rootNode.data:
        if rootNode.leftchild is None:
            rootNode.leftchild = BSTNode(value)
        else:
            insert_node(rootNode.leftchild, value)
    else:
        if rootNode.rightchild is None:
            rootNode.rightchild = BSTNode(value)
        else:
            insert_node(rootNode.rightchild, value)
    return "data inserted"

def preorder_traversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preorder_traversal(rootNode.leftchild)
    preorder_traversal(rootNode.rightchild)

def inorder_traversal(rootNode):
    if not rootNode:
        return
    inorder_traversal(rootNode.leftchild)
    print(rootNode.data)
    inorder_traversal(rootNode.rightchild)

def postorder_traversal(rootNode):
    if not rootNode:
        return
    postorder_traversal(rootNode.leftchild)
    postorder_traversal(rootNode.rightchild)
    print(rootNode.data)

def leveorder_traversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.is_empty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftchild is not None:
                customQueue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customQueue.enqueue(root.value.rightchild)

def search_node(rootNode,value):
    if rootNode.data == value:
        print("the value is found")
    elif value < rootNode.data:
        if rootNode.leftchild.data == value:
            print("the value is found")
        else:
            search_node(rootNode.leftchild, value)
    else:
        if rootNode.rightchild.data == value:
            print("the value is found")
        else:
            search_node(rootNode.rightchild, value)

def minimum_value(bstNode):
    currentnode = bstNode
    while (currentnode.leftchild is not None):
        currentnode = currentnode.leftchild
    return currentnode

def deleteNode(rootnode, nodevalue):
    if rootnode is None:
        return rootnode
    if nodevalue < rootnode.data:
        rootnode.leftchild = deleteNode(rootnode.leftchild, nodevalue)
    elif nodevalue > rootnode.data:
        rootnode.rightchild = deleteNode(rootnode.rightchild, nodevalue)
    else:
        if rootnode.leftchild is None:
            temp = rootnode.rightchild
            rootnode = None
            return temp

        if rootnode.rightchild is None:
            temp = rootnode.leftchild
            rootnode = None
            return temp

        temp = minimum_value(rootnode.rightchild)
        rootnode.data = temp.data
        rootnode.rightchild =deleteNode(rootnode.rightchild, temp.data)
    return rootnode

def deletebinary_search_tree(rootnode):
    rootnode.data = None
    rootnode.leftchild =None
    rootnode.rightchild =None
    return "BST successfully deleted"


newBST = BSTNode(None)
insert_node(newBST,70)
insert_node(newBST,50)
insert_node(newBST,90)
insert_node(newBST,30)
insert_node(newBST,60)
insert_node(newBST,80)
insert_node(newBST,100)
insert_node(newBST,20)
insert_node(newBST,40)
# print(newBST.data)
# print(newBST.leftchild.data)
deletebinary_search_tree(newBST)
leveorder_traversal(newBST)
