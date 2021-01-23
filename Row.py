from dataclasses import dataclass

from anytree import Node

LAST_NODE_PRE = "└── "
NODE_PRE = "├── "
INDENT = "│   "


@dataclass
class Row:
    node: Node
    level: int
    is_last: bool = False

    @property
    def pre(self):
        # 根结点
        if self.level == 0:
            return ""

        branch = INDENT * (self.level - 1)
        pre = NODE_PRE if not self.is_last else LAST_NODE_PRE
        return branch + pre

    def __str__(self):
        return self.pre + self.node.name
