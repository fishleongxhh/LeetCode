# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode137: Single Number2问题

#对于负数会输出错误结果(已修正)
def singleNumber(nums):
    if nums:
        bitSum = [0]*32
        for item in nums:
            for j in range(31,-1,-1):
                bitSum[j] += (item & 1)
                item = item >> 1
        res = 0
        for item in bitSum:
            res = res << 1
            res += (item % 3)
        if res >= 2**31: #为了应付负数出现的情况
            res -= 2**32
        return res
    return None

if __name__ == "__main__":
    nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
    nums = [1,3,3,3,1,1,-2,-2,-2,-0]
    print(sorted(nums))
    print(singleNumber(nums))
