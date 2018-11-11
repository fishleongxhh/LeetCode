# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode811: Subdomain Visit Count问题

def subdomainVisits(cpdomains):
    res = {}
    for cpdomain in cpdomains:
        #找到空格和圆点的位置
        ind = [loc for loc,item in enumerate(cpdomain) if item == ' ' or item == '.']
        #取出数值
        freq = int(cpdomain[0:ind[0]])
        #更新字典
        for i in range(len(ind)):
            res[cpdomain[(ind[i]+1):]] = res.get(cpdomain[(ind[i]+1):],0) + freq
    return [str(value)+' '+key for key, value in res.items()]

if __name__ == "__main__":
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    print(cpdomains)
    print(subdomainVisits(cpdomains))
