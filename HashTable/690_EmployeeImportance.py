# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode690: Employee Importance问题

"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

def sumImportance(id, emp_map):
    info = emp_map[id]
    return info.importance + sum([sumImportance(item, emp_map) for item in info.subordinates])
#用递归+深度优先搜索的解法
def getImportance(employees, id):
    emp_map = {emp.id:emp for emp in employees}
    return sumImportance(id, emp_map)

#用循环+深度优先搜索的解法，利用了栈的思想，值得学习！！
def getImportance2(employees, id)
    emap = {e.id:e for e in employees}
    stack = [emap[id]]
    r = 0
    while stack:
        e = stack.pop()
        r += e.importance
        for sid in e.subordinates:
            stack.append(emap[sid])
    return r
