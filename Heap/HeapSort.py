# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序使用最小堆来对数组进行降序排列（同理，可以使用最大堆对数组进行升序排列）

#此函数用于对nums数组的loc位置元素进行下滤，以维持堆序性
def percolateDown(nums, loc, size):
    if loc*2 <= size:
        curr_loc, tmp_loc = loc, loc*2
        next_loc = tmp_loc if size <= tmp_loc or nums[tmp_loc] <= nums[tmp_loc+1] else tmp_loc+1
        while next_loc <= size and nums[next_loc] < nums[curr_loc]:
            nums[curr_loc], nums[next_loc] = nums[next_loc], nums[curr_loc]
            curr_loc, tmp_loc = next_loc, next_loc*2
            next_loc = tmp_loc if size <= tmp_loc or nums[tmp_loc] <= nums[tmp_loc+1] else tmp_loc+1

def heapSort(nums):
    #nums的第一个位置插入负无穷大
    size = len(nums)
    nums.insert(0,float('inf'))
    #首先使用下滤，将nums初始化一个最小堆
    for i in range(size//2,0,-1):
        percolateDown(nums, i, size)
    #循环交换最小元和最后一个元素的位置，然后对第一个位置的元素执行下滤
    while size > 1:
        nums[1], nums[size] = nums[size], nums[1]
        size -= 1
        percolateDown(nums, 1, size)

if __name__ == "__main__":
    nums = [4,3,5,6,7,2,44,2,13,13,45,65,147,864,213,653]
    print(nums)
    heapSort(nums)
    print(nums)
