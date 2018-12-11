# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode15. 3Sum问题

def threeSum(nums):
    res = []
    nums.sort()
    n = len(nums)
    for i in range(n-2): #只用遍历到倒数第三个就可以了
        if i > 0 and nums[i] == nums[i-1]:
            continue #如果有重复元素，跳过
        if nums[i] > 0:
            break #如果第一个元素开始大于0，就无需再循环了，因为后面的元素都是大于0，其和不可能为0
        start, end = i+1, n-1 #从两边开始往中间走
        while start < end:
            s = nums[i] + nums[start] + nums[end]
            if s < 0:
                start += 1
            elif s > 0:
                end -= 1
            else:
                res.append([nums[i], nums[start], nums[end]]) #找到一组和为0的
                #对于重复的元素，跳过
                while start < end and nums[start] == nums[start+1]:
                    start += 1
                start += 1
                while start < end and nums[end] == nums[end-1]:
                    end -= 1
                end -= 1
    return res

if __name__ == "__main__":
    nums = [-1, 0, 2, -2, -2, 4, 1]
    print(sorted(nums))
    print(threeSum(nums))
