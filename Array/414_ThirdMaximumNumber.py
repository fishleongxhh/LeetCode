# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode414: Third Maximum Number问题

def thirdMax(nums):
    nums = set(nums)
    if len(nums) < 3:
        return max(nums)
    Max1 = max(nums)
    nums.remove(Max1)
    Max2 = max(nums)
    nums.remove(Max2)
    return max(nums)

if __name__ == "__main__":
    nums = [3,2,2,1]
    print(sorted(nums))
    print(thirdMax(nums))
