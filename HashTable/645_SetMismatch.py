# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode645: Set Mismatch问题

#我们假设输入的数组必定满足我们的条件
#下面的程序其实是不健壮的
#其实可以通过简单的求和运算，就可以得到结果
def findErrorNums(nums):
    n = len(nums)
    my_set = set(range(1,n+1))
    for item in nums:
        if item in my_set:
            my_set.discard(item)
        else:
            dup_num = item
    return [dup_num, list(my_set)[0]]

if __name__ == "__main__":
    nums = [4,3,6,1,2,3]
    print(nums)
    print(findErrorNums(nums))
