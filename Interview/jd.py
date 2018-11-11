# -*- coding: utf-8 -*-

def similar(str1, str2):
    dic = {}
    value_set = set()
    for key, value in zip(str1, str2):
        if key in dic:
            if dic[key] != value:
                return False
        else:
            if value in value_set:
                return False
            dic[key] = value
            value_set.add(value)
    return True

def solve(S, T):
    if len(S) < len(T):
        return 0
    cnt = 0
    n_s, n_t = len(S), len(T)
    for i in range(0, n_s-n_t+1):
        if similar(S[i:i+n_t], T):
            cnt += 1
    return cnt

if __name__ == "__main__":
    print(solve('ababcbbcbcb','xyx'))
