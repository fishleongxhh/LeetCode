# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解剑指offer21: 调整数组顺序使得奇数位于偶数前面

#为了提高程序的重用性，将奇偶判断的函数抽象出来
#将来可以替换成任意一个合理的函数，这个函数对于任意一个输入只会输出一个True或者False
def isEven(x):
    return not x%2

#core函数
def Reorder(nums, func):
    start, end = 0, len(nums)-1
    while start < end:
        while start < end and (not func(nums[start])):
            start += 1
        while start < end and func(nums[end]):
            end -= 1
        if start < end:
            nums[start], nums[end] = nums[end], nums[start]

if __name__ == "__main__":
    nums = [1,3,5,7,9]
    print(nums)
    Reorder(nums, isEven)
    print(nums)
