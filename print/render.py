from typing import Tuple

from anytree import Node

from row import Row


def dfs(root: Node, continues: Tuple[bool] = None, is_last=False):
    if continues is None:
        continues = tuple()

    yield Row(root, continues, is_last)

    if not root.children:
        return
    for child in root.children:
        is_last = root.children[-1] == child
        for grandchild in dfs(child, continues + (not is_last,), is_last):
            yield grandchild
