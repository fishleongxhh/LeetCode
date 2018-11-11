# -*- codingL utf-8 -*-

import sys

n, m = [int(item) for item in sys.stdin.readline().strip().split()]
nums = [int(item) for item in sys.stdin.readline().strip().split()]
print(nums)
nums.sort()
nums.reverse()
print(nums)

bucket = nums[0:m]
print(bucket)
for item in nums[m:]:
    ind = bucket.index(min(bucket))
    bucket[ind] += item
    print(bucket)

print(max(bucket))
print(sum(bucket)/len(bucket))
print(nums)
