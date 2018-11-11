# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode599: Minimum Index Sum of Two Lists问题

#list1和list2中的元素都是唯一的，无重复
def findRestaurant(list1, list2):
    dic, common = {}, set()
    min_ind_sum = len(list1) + len(list2) -2
    for ind, item in enumerate(list1):
        dic[item] = ind
    for ind, item in enumerate(list2):
        if item in dic:
            common.add(item)
            dic[item] += ind
            min_ind_sum = min(min_ind_sum, dic[item])
    #这一步其实还可以优化，如果上述遍历过程中时刻保持最小index和，以及对应的餐馆，那么就可以不用在下面一步再遍历common，其实也就可以不使用common这个中间变量了
    return [item for item in common if dic[item]==min_ind_sum]

if __name__ == "__main__":
    list1 = []
    list2 = []
    print(list1)
    print(list2)
    print(findRestaurant(list1,list2))
