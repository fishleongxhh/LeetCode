# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode784: Letter Case Permutation问题

#使用递归
def Core(s, end, record, res):
    if end == len(s):
        res.append(''.join(record))
    else:
        record.append(s[end])
        Core(s, end+1, record, res)
        record.pop()
        if s[end].upper() != s[end]:
            record.append(s[end].upper())
            Core(s, end+1, record, res)
            record.pop()

def letterCasePermutation(S):
    s, record, res = S.lower(), [], []
    Core(s, 0, record, res)
    return res

#使用循环
def letterCasePermutation2(S):
    res = [''] #一定要放置一个空字符，不能初始化为空列表!!
    for char in S:
        if char.isalpha():
            res = [tmp+c for tmp in res for c in [char.lower(), char.upper()]]
        else:
            res = [tmp+char for tmp in res]
    return res

if __name__ == "__main__":
    s = 'a24b34c87d76'
    print(s)
    res = letterCasePermutation2(s)
    print(res)
    print(len(res), len(set(res)))
