# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode190: Reverse Bits问题

class Solution():
    dic = {}
    def reverseBits(self, n):
        if n in self.dic:
            return self.dic[n]
        res, n1 = 0, n
        for i in range(32):
            res = (res << 1) + (n1 & 1)
            n1 = (n1 >> 1)
        self.dic[n] = res
        return res

if __name__ == "__main__":
    n = 43261596
    #n = 964176192
    solu = Solution()
    print(solu.reverseBits(n))
