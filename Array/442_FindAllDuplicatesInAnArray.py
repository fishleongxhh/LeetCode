# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode442: Find All Duplicates in an Array问题

def findDuplicates(nums):
    res = set()
    for loc in range(len(nums)):
        item = nums[loc]
        while loc != (item-1):
            if nums[item-1] == item:
                res.add(item)
                break
            else:
                nums[loc], nums[item-1] = nums[item-1], nums[loc]
                item = nums[loc]
    return list(res)

#解法2,简单地利用哈希集合.此题每个元素至多出现2次,所以res可以是一个列表，否则res应初始化为空集合
def findDuplicates2(nums):
    my_set, res = set(), []
    for item in nums:
        if item in my_set:
            res.append(item)
        else:
            my_set.add(item)
    return res

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    print(sorted(nums))
    print(findDuplicates2(nums[:]))
