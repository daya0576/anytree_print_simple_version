from dataclasses import dataclass
from typing import List

from anytree import Node

LAST_NODE_PRE = "└── "
NODE_PRE = "├── "
INDENT = "│   "
BLANK = "    "


@dataclass
class Row:
    node: Node
    continues: List[int]
    is_last: bool = False

    @property
    def pre(self):
        # 根结点特殊处理
        if len(self.continues) == 0:
            return ""

        branch = "".join([INDENT if x else BLANK for x in self.continues[:-1]])
        pre = NODE_PRE if not self.is_last else LAST_NODE_PRE
        return branch + pre

    def __str__(self):
        return self.pre + self.node.name
