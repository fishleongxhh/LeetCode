# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode563: Binary Tree Tilt问题

from Tree import *

class Solution:
    tilt = 0

    def __treeSum(self, root):
        if not root:
            return 0
        leftSum = self.__treeSum(root.left)
        rightSum = self.__treeSum(root.right)
        self.tilt += abs(leftSum-rightSum)
        return leftSum + rightSum + root.val

    def findTilt(self, root):
        allSum = self.__treeSum(root)
        return self.tilt

if __name__ == "__main__":
    nums = [5,3,1,2,4,8,6,7,9,0]
    root = initTree(nums)
    obj = Solution()
    print(obj.findTilt(root))
