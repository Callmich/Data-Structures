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
from stack import Stack
from queue import Queue


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: value is < self.value
        if value < self.value:
            # if there is no left child insert value here
            if self.left is None:
                self.left = BSTNode(value)
            else:
                #repeat the process on left subtree 
                self.left.insert(value)
        # Case 2: value is > or =  self.value
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
                
    def contains(self, target):
        # Case 1: if self.value is equal to target
        if self.value == target:
            return True
        # Case 2: target is less than self.value
        elif target < self.value:
            # if self.lef is None, it isnt in tree
            if self.left is None:
                return False
            # if self.left is there then run recursion
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # set a max val to be rewritten and a current for the loop
        maxVal = self.value
        current = self
        #set up loop to rewrite max and continue loop
        while current is not None:
            if current.value > maxVal:
                maxVal = current.value
            current = current.right
        # return final max
        return maxVal
        
    def for_each(self, fn):
        #Need to run fn on value of self
        fn(self.value)
        # Case 1: If there is a right run function on it.
        if self.right:
            self.right.for_each(fn)
        # Case 2: If there is a left run function on it.
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # stack = []
        # stack.append(self)

        # if current node is None
        # we know weve reached the end of a recursion 
        # base case we want to return
    
        if self is None:
            return
        # check if we can move left
        if self.left is not None:
            self.left.in_order_print(self)
        
        # visit node by printing value
        print(self.value)

        if self.right is not None:
            self.right.in_order_print(self)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # use a queue to form a "line" for the nodes to get in
        line = Queue()

        # start by placing the root in the queue
        line.enqueue(node)
        
        # need a while loop to iterate
        while line.__len__() > 0:
        # while length of queue is greater than 0
            # dequeue item from from of queue
            val = line.dequeue()
            val
            # print item
            print(val.value)

            # place current item's left node in queue if not none
            if val.left:
                line.enqueue(val.left)
            # place current item's right node in queue if not none
            if val.right:
                line.enqueue(val.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # init an empty stack
        line = Stack()
        # push the root node onto the stack
        line.push(node)

        # need a while loop to manage out itteration
        # if stack is not empty enter the while loop
        while line.__len__() > 0:
            # pop top item off stack
            val = line.pop()
            val
            
            # print that items's value
            print(val.value)

            # if right subtree 
                # push right item onto stack
            if val.right:
                line.push(val.right)
            # if left subtree
                #  push left item onto stack
            if val.left:
                line.push(val.left)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
