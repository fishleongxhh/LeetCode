# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode744: Find Smallest Letter Greater Than Target问题

#letters升序排列，和target均为小写字母
#且letters至少包含两个字母
def nextGreatestLetter(letters, target):
    start, end = 0, len(letters)-1
    if target >= letters[end] or target < letters[start]:
        return letters[start]
    while start <= end:
        mid = (start+end)//2
        if letters[mid] <= target:
            start = mid + 1
        else:
            if letters[mid-1] <= target:
                return letters[mid]
            else:
                end = mid - 1

if __name__ == "__main__":
    letters = ["c", "c", "c", "f", "j"]
    target = 'd'
    print(letters, target)
    print(nextGreatestLetter(letters, target))
