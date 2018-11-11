# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode496: Next Greater Element问题

def nextGreaterElement(findNums, nums):
    dic, my_stack = {}, []
    for item in nums:
        #只要当前元素比栈的顶端元素要大，就弹出顶端元素，同时用一个字典记录下来
        while len(my_stack) and my_stack[-1] < item:
            dic[my_stack.pop()] = item
        my_stack.append(item)#将当前元素加入栈
    return [dic.get(item,-1) for item in findNums]

if __name__ == "__main__":
    nums = [1,3,4,2,8,6,7,9,5]
    findNums = [4,1,2,8,5,6,9]
    print(nums)
    print(findNums)
    print(nextGreaterElement(findNums,nums))
