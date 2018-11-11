# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode500: Keyboard Row问题

dic = {'q':1,'w':1,'e':1,'r':1,'t':1,'y':1,'u':1,'i':1,'o':1,'p':1,'Q':1,'W':1,'E':1,'R':1,'T':1,'Y':1,'U':1,'I':1,'O':1,'P':1,
        'a':2,'s':2,'d':2,'f':2,'g':2,'h':2,'j':2,'k':2,'l':2,'A':2,'S':2,'D':2,'F':2,'G':2,'H':2,'J':2,'K':2,'L':2,
        'z':3,'x':3,'c':3,'v':3,'b':3,'n':3,'m':3,'Z':3,'X':3,'C':3,'V':3,'B':3,'N':3,'M':3,
        ' ':4}

def sameRow(word):
    if (not word):
        return True
    row = dic.get(word[0],-1)
    for item in word[1:]:
        curr_row = dic.get(item, -1)
        if curr_row == -1 or curr_row != row:
            return False
    return True and (row != -1)

def findWords(words):
    return [word for word in words if sameRow(word)]

if __name__ == "__main__":
    words = ["QWE", "Alaska", "Dad", "xcVBN"]
    print(words)
    print(findWords(words))
