#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Leslee
# @Email    : leelovesc@gmail.com
# @Time    : 2019.10.15 17:09

class BitNode(object):
    def __init__(self,data):
        self.data =data
        self.left = None
        self.right = None
        return

class BitTree(object):
    def __init__(self):
        self.root = None
        self.bitList = []

    def add_bit_item(self,item):
        if not isinstance(item,BitNode):
            item = BitNode(item)

        if self.root is None:
            self.root = item
            self.bitList.append(item)
        else:
            rootNode = self.bitList[0]
            while True:
                if item.data < rootNode.data:
                    if rootNode.left ==None:
                        rootNode.left = item
                        self.bitList.append(item)
                        break
                    else:
                        rootNode = rootNode.left
                elif item.data > rootNode.data:
                    if rootNode.right == None:
                        rootNode.right = item
                        self.bitList.append(item)
                        break
                    else:
                        rootNode = rootNode.right
if __name__ == '__main__':
    node1 = BitNode(15)
    node2 = BitNode(9)
    node3 = BitNode(19)
    node4 = BitNode(10)
    bittree = BitTree()
    for i in [node1,node2,node3,node4]:
        bittree.add_bit_item(i)

    print(bittree)