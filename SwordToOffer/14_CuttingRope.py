# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解剑指offer14: 剪绳子问题，至少切一刀

#使用动态规划求解,n必须要为正整数
def CuttingRope1(n):
    res = [1,1,2,4]
    #n小于5时单独处理
    if n <= 4:
        return res[n-1]
    #n大于等于5时，为保证递推正确，前4项的值需要稍微修改一下
    res = [1,2,3,4]
    for i in range(5,n+1):
        curr_res = max((res[j-1]*res[i-j-1] for j in range(1,i//2+1)))
        res.append(curr_res)
    #print(res)
    return res[-1]

#使用贪心法求解，n>=5时优先切出3来
def CuttingRope2(n):
    res = [1,1,2,4]
    if n <= 4:
        return res[n-1]
    cnt3, tmp = n//3, n%3
    if tmp == 0:
        factor = 1
    elif tmp == 1:
        cnt3, factor = cnt3-1, 4
    else:
        factor = 2
    return (3**cnt3)*factor

if __name__ == "__main__":
    for n in range(1,21):
        print(CuttingRope1(n), CuttingRope2(n))
