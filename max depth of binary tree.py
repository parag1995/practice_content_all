from collections import deque


def max_depth(rootnode):
    if not rootnode:
        return 0
    level = 0
    q=deque([rootnode])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level+=1
    return level

def max_depth_recursive(rootnode):
    if not rootnode:
        return 0
    return 1+max(max_depth_recursive(rootnode.left),max_depth_recursive(rootnode.right))
