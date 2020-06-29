# coding = UTF-8
import bisect
import math


class Leaf:  # define leaf class
    def __init__(self, prev_leaf, next_leaf, parent, branching_factor=5):  # leaf constructor
        self.prev = prev_leaf
        self.next = next_leaf
        self.parent = parent
        self.branch = branching_factor
        self.keys = []
        self.children = []

    def sett(self, key, value):
        index = bisect.bisect_left(self.keys, key)  # find key from keys and get index
        if index < len(self.keys) and self.keys[index] == key:  # use key find value
            self.children[index] = value
        else:  # insert new key and value
            self.keys.insert(index, key)
            self.children.insert(index, value)
            if len(self.children) == self.branch:  # when value greater than branching factor
                self.split(math.ceil(self.branch / 2))

    def get(self, key):
        index = self.keys.index(key)
        return self.children[index]

    def split(self, index):
        self.next = Leaf(self, self.next, self.parent, self.branch)  # create new leaf to put value greater than index value
        self.next.keys = self.keys[index:]  # value after index
        self.next.children = self.children[index:]
        self.keys = self.keys[:index]  # value before index
        self.children = self.children[:index]
        if self.parent is None:  # if this Leaf is root node
            self.parent = Node(None, None, [self.next.keys[0]], [self, self.next], branch_factor=self.branch)  # make a parent node to link self and next when this leaf is root leaf
            self.next.parent = self.parent
        else:  # if this is not root node
            self.parent.add_child(self.next.keys[0], self.next)  # make new node
        return self.next

    def remove_item(self, key):
        del_index = self.keys.index(key)
        self.keys.pop(del_index)
        remove_item = self.children.pop(del_index)
        self.balance()
        return remove_item

    def balance(self):
        if self.parent is not None and len(self.children) < self.branch // 2:
            if self.prev is not None and len(self.prev.children) > self.branch // 2:  # if prev leaf have more enough element
                self.keys.insert(0, self.prev.keys.pop(-1))
                self.children.insert(0, self.prev.children.pop(-1))
                self.parent.change_key(self.keys[0], self.keys[0])
            elif self.next is not None and len(self.next.children) > self.branch // 2:  # if next leaf have more enough element
                self.keys.insert(-1, self.next.keys.pop(0))
                self.children.insert(-1, self.next.children.pop(0))
                self.next.parent.change_key(self.keys[0], self.next.keys[0])
            elif self.prev is not None:  # merge left (deflaut)
                del_index = self.prev.keys[-1]
                self.prev.keys.extend(self.keys)
                self.prev.children.extend(self.children)
                self.parent.remove_child(del_index)
            elif self.next is not None:  # merge right (except)
                del_index = self.keys[-1]
                self.keys.extend(self.next.keys)
                self.children.extend(self.next.children)
                self.parent.remove_child(del_index)


class Node:
    def __init__(self, pre_node, next_node, keys, children, parent=None, branch_factor=5):  # node constructor
        self.prev_node = pre_node
        self.next_node = next_node
        self.keys = keys
        self.children = children
        self.parent = parent
        self.branch = branch_factor
        for child in children:
            child.parent = self

    def sett(self, key, value):  # find key from keys and get index
        for i, k in enumerate(self.keys):  # i can get index ank k can get value
            if key < k:
                self.children[i].sett(key, value)
                return
        self.children[i+1].sett(key, value)

    def get(self, key):  #
        for i, k in enumerate(self.keys):   # i can get index and k can get value
            # print(self.children[i].children)
            if key < k:  # return value
                return self.children[i].get(key)
        return self.children[i+1].get(key)

    def add_child(self, key, greater):  # something error
        index = bisect.bisect(self.keys, key)
        self.keys.insert(index, key)
        self.children.insert(index+1, greater)
        if len(self.keys) == self.branch:
            self.split(self.branch // 2)

    def change_key(self, older, newer):
        # print("node change key!!!")
        if newer < self.keys[0]:  # when key smaller than smallest key
            self.parent.change_key(self.keys[0], newer)   # go to parent keys and compare again
            for i, k in enumerate(self.keys):
                if k >= older:  # if find key bigger than older key the newer key can insert
                    self.keys[i] = newer

    def split(self, index):
        # print("node new spilt!!! index is", index)
        self.next_node = Node(self, self.next_node, self.keys[index+1:], self.children[index+1:], self.parent)
        split_key = self.keys[index]
        self.keys = self.keys[:index]
        self.children = self.children[:index+1]
        if self.parent is None:  # root node
            self.parent = Node(None, None, [split_key], [self, self.next_node], branch_factor=self.branch)
        else:
            self.parent.add_child(split_key, self.next_node)
        return self.next_node

    def remove_child(self, key):
        removed_child = None
        for i, k in enumerate(self.keys):
            if k >= key:
                removed_child = self.children.pop(i+1)
                if removed_child.prev is not None:
                    removed_child.prev.next = removed_child.next
                if removed_child.next is not None:
                    removed_child.next.prev = removed_child.prev
                break
        self.balance()
        return removed_child

    def remove_item(self, key):
        for i, k in enumerate(self.keys):
            if k >= key:
                self.children[i].remove_item(k)
                return
        return self.children[-1].remove_item(key)

    def balance(self):  # like leaf balance
        # print("node balance")
        if self.parent is not None and len(self.children) < self.branch // 2:
            if self.prev_node is not None and len(self.prev_node) > self.branch // 2:
                self.keys.insert(0, self.prev_node.keys.pop(-1))
                self.children.insert(0, self.prev_node.children.pop(-1))
                self.parent.change_key(self.keys[0], self.keys[0])
            elif self.next_node is not None and len(self.next_node.children) > self.branch // 2:
                self.keys.insert(-1, self.next_node.keys.pop(0))
                self.children.insert(-1, self.next_node.children.pop(0))
                self.parent.change_key(self.keys[0], self.next_node.keys[0])
            elif self.prev_node is not None:
                del_index = self.prev_node.keys.pop(-1)
                self.prev_node.keys.extend(self.keys)
                self.prev_node.children.extend(self.children)
                self.parent.remove_child(del_index)
            elif self.next_node is not None:
                del_index = self.prev_node.keys.pop(0)
                self.keys.extend(self.next_node.keys)
                self.children.extend(self.next_node.children)
                self.parent.remove_child(del_index)
        if self.parent is None and len(self.children) == 1:  # if self is root node
            self.children[0].parent = None


