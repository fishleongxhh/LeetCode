# -*- coding: utf-8 -*-
#Author: Xu Hanhui
#此程序用来求解LeetCode69: Sqrt(x)，用二分查找求解一个数的平方根，只需返回整数部分即可

#这里x被保证是一个非负整数
def mySqrt(x):
    if x == 0:
        return 0
    low, high = 1, x
    while low <= high:
        middle = int((low + high)/2)
        tmp = middle*middle
        if tmp == x:
            return middle
        if tmp > x:
            high = middle -1
        if tmp < x:
            low = middle + 1
    return high

if __name__ == "__main__":
    for i in range(21):
        print(i, mySqrt(i))
