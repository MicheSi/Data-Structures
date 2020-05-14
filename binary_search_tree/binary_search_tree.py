from queue import Queue
from singly_linked_list import LinkedList
from stack import Stack
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
class BSTNode(object): 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if empty - if empty put node at root
        if self.value is None:
            self.value = BSTNode(value)
        # if < go left
        # if >= got right
        else:
            # if new value less than value in tree, add to left
            if value < self.value:
                if self.left is None:
                    self.left = BSTNode(value)
                else:
                    self.left.insert(value)
            # if new value is greater than value, add to right
            else:
                if self.right is None:
                    self.right = BSTNode(value)
                else:
                    self.right.insert(value)
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # start at root (self) when searching
        # compare target to self
        if target == self.value:
            return True
        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # check if empty
        if self.value is None:
            return
        # if not empty, traverse through right side to get last value on right
        else:
            if self.right:
                return self.right.get_max()
            return self.value
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # check if empty
        if self.value is None:
            return
        # traverse through nodes to get value of each
        if self.value:
            fn(self.value)
            # check left side for values
            if self.left:
                self.left.for_each(fn)
                # check right side for values
            if self.right:
                self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # need to print left side 1st
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        # then print right side
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create queue
        # start at root - add to queue
        # while queue not empty node = head of queue
        # print
        # add children to queue
        # pop node off queue

        queue = Queue()

        queue.enqueue(node)

        while len(queue) > 0:
            current = queue.dequeue()
            print(current.value)

            if current.left:
                queue.enqueue(current.left)
            
            if current.right:
                queue.enqueue(current.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create stack
        # add root to stack
        # while stack not empty node = pop top of stack
        # print
        # add children to stack
        
        stack = []

        stack.append(self)

        while len(stack) > 0:
            node = stack.pop()
            print(node.value)

            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)
            
            if node.left:
                self.left.pre_order_dft(node.left)
            if node.right:
                self.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            if node.left:
                self.left.post_order_dft(node.left)
            if node.right:
                self.right.post_order_dft(node.right)

            print(node.value)
