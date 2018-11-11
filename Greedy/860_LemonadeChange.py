# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode860: Lemonade Change问题

def lemonadeChange(bills):
    dic = {5:0, 10:0, 20:0}
    for money in bills:
        if money == 10:
            if dic[5] <= 0:
                return False
            else:
                dic[5] -= 1
        if money == 20:
            if dic[10] >=1 and dic[5] >= 1:
                dic[10] -= 1
                dic[5] -= 1
            elif dic[5] >=3:
                dic[5] -= 3
            else:
                return False
        dic[money] += 1
    return True

if __name__ == "__main__":
    bills = [5,5,10,10,20]
    print(bills)
    print(lemonadeChange(bills))
