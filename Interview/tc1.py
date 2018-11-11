# -*- coding: utf-8 -*-

import sys

k = int(sys.stdin.readline().strip())
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

my_set = set()
cnt = 0
for i in range(len(str1)-k+1):
    my_set.add(str1[i:i+k])

for i in range(len(str2)-k+1):
    if str2[i:i+k] in my_set:
        cnt += 1

print(cnt)
