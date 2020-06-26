# coding = UTF-8
import bisect
from Bplustree_node import Leaf, Node


class Bplustree:
    def __init__(self, branching_factor=5):
        self.branch = branching_factor
        self.leave = Leaf(None, None, None, self.branch)  # first leaf
        self.root = self.leave

    def get(self, key):
        # print(self.root)
        return self.root.get(key)

    def remove_item(self, key):
        self.root.remove_item(key)
        if type(self.root) is Node and len(self.root.children) == 1:
            self.root = self.root.children

    def sett(self, key, value):
        self.root.sett(key, value)
        if self.root.parent is not None:  # not root
            self.root = self.root.parent

    def size(self):
        result = 0
        leaf = self.leave
        while leaf is not None:
            result = result + leaf.size()
            leaf = leaf.next
        return result

    def spilt(self, key):
        tree = Bplustree()
        tree.root = Node(None, None, [], [], self.branch)
        curr = self.root
        newer = tree.root
        while type(curr) is Node or type(curr) is Leaf:
            child_type = type(curr.children[0])  # check curr is leaf or node
            sp_index = bisect.bisect_left(curr.keys, key)  # find index
            newer.keys = curr.keys[:sp_index]  # put key and children
            newer.children = curr.children[:sp_index]
            curr.keys = curr.keys[sp_index:]
            curr.children = curr.children[sp_index:]
            if len(curr.children) == 0:
                break
            if child_type is Leaf:
                newer.children.append(Leaf(newer.children[-1], None, parent=newer, branching_factor=newer.branch))
                newer.children[-2].next = newer.children[-1]
                curr.children[0].prev = None
            if child_type is Node:
                newer.children.append(Node(newer.children[-1], None, [], [], parent=newer, branch_factor=newer.branch))
                newer.children[-2].next = newer.children[-1]
                curr.children[0].prev = None
            newer.balance()
            curr.balance()
            curr = curr.children[0]
            newer = newer.children[-1]
        return tree

