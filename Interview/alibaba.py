# -*- coding: utf-8 -*-
# Author: Xu Hanhui

import sys

my_map = {}
list1 = [item.split("_") for item in sys.stdin.readline().strip().decode("utf-8").split(";")]
for item in list1:
    for i in item[1].split('|'):
        if i in my_map:
            my_map[i].append(item[0])
        else:
            my_map[i] = [item[0]]
print(my_map)

res = my_str = sys.stdin.readline().strip().decode('utf-8')
n, i = len(my_str), 0
while i < n:
    j = i + 1
    while j > i and j < n:
        if my_str[i:j] in my_map and my_str[i:j+1] not in my_map:
            res = res.replace(my_str[i:j], ' '+my_str[i:j]+'/'+(','.join(sorted(my_map[my_str[i:j]])))+' ')
            i = j
        j += 1
    i += 1
print(res)
