# -*- coding: utf-8 -*-
#Author: Xu Hanhui
#此题用来求解LeetCode303: Range Sum Query问题, 涉及到动态规划

#虽然题目很简单，只是求和，但是由于是将数组初始化一个类，然后频繁调用求和方法
#所以，如果每次调用都要计算，那么总的时间会很慢，因此想到初始化类的时候需要做一些类似动态规划的准备工作

class NumArray:
    def __init__(self,nums):
        """
        :type nums: List[int]
        """
        self.cum_sum = nums[:]
        self.length = len(nums)
        if self.length > 1:
            for i in range(1,self.length):
                self.cum_sum[i] = self.cum_sum[i] + self.cum_sum[i-1]

    def sumRange(self, i, j):
        i, j = max(0,i), min(j, self.length-1)
        if i > j or self.length == 0:
            return 0
        if i == 0:
            return self.cum_sum[j]
        else:
            return self.cum_sum[j] - self.cum_sum[i-1]

if __name__ == '__main__':
    nums = [1,]
    print(nums)
    i, j = -1, -1
    print(i,j)
    obj = NumArray(nums)
    print(obj.sumRange(i, j))
