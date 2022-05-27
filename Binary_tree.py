
class TreeNode:
    def __init__(self, data, children=[]):
        self.data= data
        self.children = children

    def __str__(self, level=0):
        ret  =" "*level+str(self.data)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def addChild(self,TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('Drinks',[])
cold = TreeNode('cold',[])
hot = TreeNode('Hot',[])
tea = TreeNode('tea',[])
coffee = TreeNode('coffee',[])
cola = TreeNode('cola',[])
fenta = TreeNode('fenta',[])
hot.addChild(tea)
hot.addChild(coffee)
cold.addChild(cola)
cold.addChild(fenta)
tree.addChild(cold)
tree.addChild(hot)
print(tree)