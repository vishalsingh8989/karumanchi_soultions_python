#!/usr/bin/python
from __future__ import print_function
from platform import node
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""


import sys
import random
import time

class Node:
    def __init__(self, val, node):
        self.val = val
        self.next_node = node
    def setNext(self, node):
        self.next_node = node
    def getNext(self):
        return self.next_node
    def setData(self, val):
        self.val = val
    def getData(self):
        return self.val
    
def test(root):
    node = root
    prev = node.getData()
    node = node.getNext()
    while node is not None:
        if prev > node.getData():
            return False
        prev = node.getData()
        node = node.getNext()
    return True
    

def getLength(root):
    count = 0
    while root is not None:
        count +=1
        root = root.getNext()
    return count


def merge(node_a, node_b):
    head = None
    if node_a is None:
        return node_b
    if node_b is None:
        return node_a
    
    if node_a.getData() >= node_b.getData():
        head = node_b
        next_node = merge(node_a, node_b.getNext())
        head.setNext(next_node)
    else:
        head = node_a
        next_node = merge(node_a.getNext(), node_b)
        head.setNext(next_node)
    
    return head
 
 
#0 ,1  ,2  3  4  5  6  7    
def mergesort(node):
    mid  = getLength(node)/2
    first_node = node
    
    if node.getNext() is None:
        return node
    
    while mid - 1 > 0:
        first_node = first_node.getNext()
        mid -= 1
    
    second_node  = first_node.getNext()
    first_node.setNext(None)
    
    node_a = mergesort(first_node)
    node_b = mergesort(second_node)
    
    return merge(node_a, node_b)
    
    

        
def mklist(initializer):
    head = temp = Node(initializer[0], None)
    for i in xrange(1, len(nums)):
        n = Node(initializer[i], None)
        temp.setNext(n)
        temp = temp.getNext()
    return head

def walk(head):
    while head is not None:
        yield head.getData()
        head = head.getNext()

if __name__ == "__main__":

    res = []
    start = time.time()
    for _ in xrange(2000):
        size = random.randint(1,100)
        nums = [random.randint(-10,200) for _ in xrange(size)]
        root = mklist(nums)
        root = mergesort(root)
        #print(nums)
        res.append(test(root))
     
     
    end = time.time()
    print("%s Pass."%(res.count(True)))
    print("%s Fail."%(res.count(False)))
    print("Time :  %s"%(end-start))



     
    
        