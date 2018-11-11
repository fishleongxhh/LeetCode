# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode47: Permutations2问题

#nums中的数字可能有重复
def permuteUnique(nums):
    res = [[]]
    for item in nums:
        new_res = []
        for prevPermute in res:
            for i in range(len(prevPermute)+1):
                new_res.append(prevPermute[:i]+[item]+prevPermute[i:])
                if i < len(prevPermute) and prevPermute[i] == item:
                    break
        res = new_res
    return res

if __name__ == "__main__":
    nums = [1,1,2,1,1,2]
    print(nums)
    print('\n')
    res = permuteUnique(nums)
    for permute in res:
        print(permute)
