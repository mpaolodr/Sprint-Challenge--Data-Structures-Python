"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from doubly_linked_list import DoublyLinkedList as dll


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if tree is empty
        if self.value is None:
            self.value = BinarySearchTree(value)

        # tree not empty
        else:
            # goes left
            if value < self.value:

                if self.left is not None:
                    self.left.insert(value)
                # left of current node is empty
                else:
                    self.left = BinarySearchTree(value)

            # value is greater than or equal to current node value
            # goes right
            else:

                if self.right is not None:
                    self.right.insert(value)
                    # right of current node is empty
                else:
                    self.right = BinarySearchTree(value)

    def contains(self, target):

        if self.value == target:
            return True

        else:

            if target < self.value:

                if self.left is not None:
                    return self.left.contains(target)
                else:
                    return False

            else:

                if self.right is not None:
                    return self.right.contains(target)
                else:
                    return False

    def get_max(self):
        if not self.value:
            return

        else:
            if self.right is None:
                return self.value
            else:
                return self.right.get_max()

    def for_each(self, fn):
        if not self.value:
            return

        else:
            fn(self.value)

            if self.left:
                self.left.for_each(fn)

            if self.right:
                self.right.for_each(fn)

    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)

            print(node.value)

            self.in_order_print(node.right)

    def bft_print(self, node):
        h = self.height(node)

        for i in range(1, h+1):
            self.printGivenLevel(node, i)

    def dft_print(self, node):
        if node:

            print(node.value)

            self.dft_print(node.left)

            self.dft_print(node.right)

    def pre_order_dft(self, node):
        if node:
            print(node.value)

            self.pre_order_dft(node.left)

            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:

            self.post_order_dft(node.left)

            self.post_order_dft(node.right)
            print(node.value)

    def height(self, node):
        if node is None:
            return 0

        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)

            if left_height > right_height:
                return left_height + 1

            else:
                return right_height + 1

    def printGivenLevel(self, node, level):
        if node is None:
            return

        if level == 1:
            print(node.value)

        elif level > 1:
            self.printGivenLevel(node.left, level-1)
            self.printGivenLevel(node.right, level-1)
