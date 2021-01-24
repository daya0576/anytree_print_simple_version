from dataclasses import dataclass
from typing import List

from anytree import Node

LAST_NODE_PRE = "╰── "
NODE_PRE = "├── "
INDENT = "│   "
BLANK = "    "


@dataclass
class Row:
    node: Node
    continues: List[int]

    @property
    def pre(self):
        # 根结点特殊处理
        if len(self.continues) == 0:
            return ""

        indent = "".join([INDENT if x else BLANK for x in self.continues[:-1]])
        branch = NODE_PRE if self.continues[-1] else LAST_NODE_PRE
        return indent + branch

    def __str__(self):
        return self.pre + self.node.name
