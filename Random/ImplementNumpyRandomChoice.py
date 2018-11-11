# -*- coding: utf-8 -*-
# Author: Xu Hanhui
#此程序使用[0,1]均匀随机数实现np.random.choice

import numpy as np

def NumpyRandomChoice(nums, size, replace=True):
    n = len(nums)
    if (size > n and (not replace)) or size < 0:
        return None
    if size == n and (not replace):
        return nums
    res = []
    for i in range(0,size):
        index = int(np.random.random()*n)
        res.append(nums[index])
        if not replace:
            del nums[index]
            n -= 1
    return res

if __name__ == "__main__":
    nums = list(range(10))
    size = 5
    print(nums)
    print(NumpyRandomChoice(nums, size, replace=True))
    print(NumpyRandomChoice(nums, size, replace=False))
