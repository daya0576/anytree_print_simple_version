from anytree import Node

from Row import Row


def dfs(root: Node, level=0, is_last=False):
    yield Row(root, level, is_last)
    level += 1

    if not root.children:
        return
    for child in root.children:
        is_last = root.children[-1] is child
        for grandchild in dfs(child, level, is_last):
            yield grandchild
