from anytree import Node, RenderTree

from render import dfs

if __name__ == '__main__':
    a = Node("A")
    b = Node("B", parent=a)
    c = Node("C", parent=a)

    d = Node("D", parent=b)
    e = Node("E", parent=b)

    for x in dfs(a):
        print(x.node, x.level, x.is_last)

    for x in dfs(a):
        print(x)

    for x in RenderTree(a):
        print(x)
