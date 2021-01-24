from typing import Tuple

from anytree import Node

from row import Row


def dfs(root: Node, continues: Tuple[bool] = None):
    if continues is None:
        continues = tuple()

    yield Row(root, continues)

    if not root.children:
        return
    for child in root.children:
        is_last = root.children[-1] == child
        for grandchild in dfs(child, continues + (not is_last,)):
            yield grandchild
