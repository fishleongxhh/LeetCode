# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode300. Longest Increasing Subsequence问题

#解法1
class Solution1:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res, maxLen = [1]*n, 1*int(n>0)
        for i in range(1,n):
            res[i] = max([res[j]+1 for j in range(i) if nums[j]<nums[i]]+[1])
            maxLen = res[i] if res[i]>maxLen else maxLen
        return maxLen

#解法2，复杂度更低
class Solution2:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        tails = []
        for item in nums:
            if (not tails) or (item > tails[-1]):
                tails.append(item)
            else:
                start, end = 0, len(tails)-1
                while start < end:
                    mid = (start+end)//2
                    if tails[mid] < item:
                        start = mid + 1 
                    else:
                        end = mid 
                tails[end] = item
        return len(tails)
