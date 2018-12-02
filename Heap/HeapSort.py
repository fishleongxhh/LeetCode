# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序使用最小堆来对数组进行降序排列（同理，可以使用最大堆对数组进行升序排列）

#nums的第一个元素不是'inf'
#loc为需要执行下沉操作的位置
#size为最大堆最后一个元素的位置
def LeftChild(loc):
    return 2*loc+1

#此函数用于对nums数组的loc位置元素进行下滤，以维持堆序性
def percolateDown(nums, loc, size):
    if loc <= size:
        tmp, LC = nums[loc], LeftChild(loc)
        while LC <= size:
            NextLoc = LC
            if LC+1 <= size and nums[LC+1] > nums[LC]:
                NextLoc = LC+1
            if nums[NextLoc] > tmp:
                nums[loc], loc = nums[NextLoc], NextLoc
                LC = LeftChild(loc)
            else:
                break
        nums[loc] = tmp

#对nums进行升序排序，会原地改变数组
def HeapSort(nums):
    size = len(nums) - 1 #最后一个元素的下标
    #将nums初始化为一个最大堆
    for loc in range(size//2, -1, -1):
        percolateDown(nums, loc, size)
    #不停地将堆顶元素与最后一个元素进行交换，然后更新最大堆
    while size > 0:
        nums[size], nums[0] = nums[0], nums[size]
        size -= 1
        percolateDown(nums, 0, size)

if __name__ == "__main__":
    nums = [4,3,5,6,7,2,44,2,13,13,45,65,147,864,213,653,31,51,536,735,1246,376,41,4,253,75,1,3]
    print(nums)
    print(sorted(nums))
    HeapSort(nums)
    print(nums)
