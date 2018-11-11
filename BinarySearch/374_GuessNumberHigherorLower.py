# -*- coding: utf-8 -*-
# Author: Xu Hanhui
#此程序用来求解LeetCode374: Guess Number Higher or Lower问题，需要用到二分查找

#n为大于等于1的正整数
def guessNumber(n):
    low, high = 1, n
    while low <= high:
        middle = int((low+high)/2)
        feed_back = guess(middle)
        if feed_back == 0:
            return middle
        elif feed_back  == -1:
            high = middle - 1
        else:
            low = middle + 1
    return -1

def guess(item):
    target = 7
    if item == target:
        return 0
    elif item > target:
        return -1
    else:
        return 1

if __name__ == "__main__":
    print(guessNumber(10))
