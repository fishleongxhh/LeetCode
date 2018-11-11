# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode239: Sliding Window Maximum问题

def maxSlidingWindow(nums, k):
    if (not nums) or k <= 0:
        return []
    q, res = [], []
    for i, item in enumerate(nums):
        while q and nums[q[-1]] <= nums[i]:
            q.pop()
        q.append(i)
        if i >= k-1:
            while i - q[0] >= k:
                q.pop(0)
            res.append(nums[q[0]])
    return res

if __name__ == "__main__":
    nums = [2,3,4,2,6,2,5,1]
    k = 8
    print(nums, k)
    print(maxSlidingWindow(nums, k))
