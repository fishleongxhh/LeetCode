# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode54: Spiral Matrix问题

def spiralOrder(matrix):
    if not matrix:
        return []
    res = []
    i, j = 0, 0
    min_left, max_right, max_down, min_up = 0, len(matrix[0])-1, len(matrix)-1, 0
    direction = 'right'
    while True:
        if direction == 'right':
            if j > max_right:
                break
            res.extend(matrix[i][j:max_right+1])
            i, j = i+1, max_right
            min_up += 1
            direction = 'down'
        if direction == 'down':
            if i > max_down:
                break
            res.extend([matrix[k][j] for k in range(i, max_down+1)])
            i, j = max_down, j-1
            max_right -= 1
            direction = 'left'
        if direction == 'left':
            if j < min_left:
                break
            res.extend(reversed(matrix[i][min_left:j+1]))
            i, j = i-1, min_left
            max_down -= 1
            direction = 'up'
        if direction == 'up':
            if i < min_up:
                break
            res.extend([matrix[k][j] for k in range(i, min_up-1, -1)])
            i, j = min_up, j+1
            min_left += 1
            direction = 'right'
    return res

if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    matrix = [[],[]]
    for l in matrix:
        print(l)
    print(spiralOrder(matrix))
