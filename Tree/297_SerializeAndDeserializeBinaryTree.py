# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode197: Serialize and Deserialize Binary Tree问题

from Tree import *

class Codec:
    def __serializeCore(self, root, res):
        if not root:
            res.append('')
        else:
            res.append(str(root.val))
            self.__serializeCore(root.left, res)
            self.__serializeCore(root.right, res)

    def serialize(self, root):
        res = []
        self.__serializeCore(root, res)
        return ','.join(res)
        
    def __deserializeCore(self, data):
        if data:
            item = data.pop(0)
            if item:
                currNode = TreeNode(int(item))
                currNode.left = self.__deserializeCore(data)
                currNode.right = self.__deserializeCore(data)
                return currNode
            return None
        return None

    def deserialize(self, data):
        return self.__deserializeCore(data.split(','))
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == "__main__":
    nums = [1,5,3,6,7,8,46,4,3,52,5,36,5,765,7,]
    rootNode = initTree(nums)
    solution = Codec()
    series = solution.serialize(rootNode)
    print(series)
    newNode = solution.deserialize(series)
    print(solution.serialize(newNode))
