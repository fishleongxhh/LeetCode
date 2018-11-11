# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode59: Spiral Matrix2问题

def generateMatrix(n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    i, j = 0, 0
    min_left, max_right, max_down, min_up = 0, n-1, n-1, 0
    direction, curr_value = 'right', 1
    while True:
        if direction == 'right':
            if j > max_right:
                break
            matrix[i][j:max_right+1] = range(curr_value, curr_value+(max_right+1-j))
            curr_value += (max_right+1-j)
            i, j = i+1, max_right
            min_up += 1
            direction = 'down'
        if direction == 'down':
            if i > max_down:
                break
            for k in range(i, max_down+1):
                matrix[k][j] = curr_value
                curr_value += 1
            i, j = max_down, j-1
            max_right -= 1
            direction = 'left'
        if direction == 'left':
            if j < min_left:
                break
            matrix[i][min_left:j+1] = range(curr_value+j-min_left, curr_value-1, -1)
            curr_value += (j+1-min_left)
            i, j = i-1, min_left
            max_down -= 1
            direction = 'up'
        if direction == 'up':
            if i < min_up:
                break
            for k in range(i, min_up-1, -1):
                matrix[k][j] = curr_value
                curr_value += 1
            i, j = min_up, j+1
            min_left += 1
            direction = 'right'
    return matrix

if __name__ == "__main__":
    n = 6
    matrix = generateMatrix(n)
    print(matrix)
    for item in matrix:
        print(item)
