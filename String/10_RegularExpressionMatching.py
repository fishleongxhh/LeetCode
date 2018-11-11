# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode10: Regular Expression Matching问题

#函数仍有不完善的地方，最下方的测试用例会陷入死循环
def isMatch(s, p):
    if not p:
        return not bool(s)
    if not s:
        flag = len(p)>=2 and p[1]=='*' and isMatch(s,p[2:])
        return flag
    if len(p)>=2 and p[1]=='*':
        if p[0] != '.' and p[0]!=s[0]:
            flag = isMatch(s,p[2:])
        else:
            flag = isMatch(s[1:],p[2:]) or isMatch(s[1:],p) or isMatch(s,p[2:])
        return flag
    if p[0]!='.' and p[0]!=s[0]:
        flag = False
    else:
        flag = isMatch(s[1:],p[1:])
    return flag

if __name__ == "__main__":
    s = "aaaaaaaaaaaaab"
    p = 'a*a*a*a*a*a*a*a*a*a*c'
    print(s,p)
    print(isMatch(s,p))
