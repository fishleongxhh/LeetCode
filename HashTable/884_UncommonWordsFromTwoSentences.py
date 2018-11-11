# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode884: Uncommon Words from Two Sentences问题

def uncommonFromSentences(A, B):
    sentenceA = A.split(' ')
    sentenceB = B.split(' ')
    res = {}
    for word in sentenceA:
        res[word] = res.get(word,0) + 1
    for word in sentenceB:
        res[word] = res.get(word,0) + 1
    return [word for word in res if res[word]==1]

if __name__ == "__main__":
    A = 'this apple is sweet sweet'
    B = 'banana'
    print(A)
    print(B)
    print(uncommonFromSentences(A,B))
