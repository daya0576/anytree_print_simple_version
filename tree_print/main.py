from anytree import Node, RenderTree

from render import dfs


def init_tree():
    a = Node("A")
    b = Node("B", parent=a)
    c = Node("C", parent=a)

    d = Node("D", parent=b)
    e = Node("E", parent=b)

    f = Node("F", parent=d)
    g = Node("G", parent=f)

    return a


if __name__ == '__main__':
    root = init_tree()

    for x in dfs(root):
        print(x)

    r = RenderTree(root)
    print(r)
