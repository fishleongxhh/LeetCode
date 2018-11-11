# -*- coding: utf-8 -*-

import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
nums = [int(item) for item in sys.stdin.readline().strip().split()]
sum_cnt = int(sys.stdin.readline().strip())

"""
dic = Counter(nums)
res = []
if sum_cnt/2 in dic:
    if dic[sum_cnt/2] >= 2:
        res.append([sum_cnt/2,sum_cnt/2])
    del dic[sum_cnt/2]
for val in nums:
    if val in dic and sum_cnt-val in dic:
        res.append([min(val,sum_cnt-val),max(val,sum_cnt-val)])
        dic[val] -= 1
        dic[sum_cnt-val] -= 1
        if dic[val] == 0 or dic[sum_cnt-val] == 0:
            del dic[val]
            del dic[sum_cnt-val]
"""
"""
res = []
my_set = set()
for item in nums:
    if sum_cnt - item in my_set:
        res.append([min(item,sum_cnt-item),max(item,sum_cnt-item)])
        my_set.remove(sum_cnt-item)
    else:
        my_set.add(item)
"""

nums.sort()
print(nums)
res = []
start, end = 0, len(nums)-1
while start < end:
    if nums[start] + nums[end] == sum_cnt:
        res.append([nums[start], nums[end]])
        start, end = start+1, end-1
    elif nums[start] + nums[end] > sum_cnt:
        end -= 1
    else:
        start += 1

#print(res)
#res = sorted(res, key=lambda item:item[0])
print(res)
if res:
    for item in res:
        print(str(item[0])+' '+str(item[1]))
else:
    print('⑨\n')
