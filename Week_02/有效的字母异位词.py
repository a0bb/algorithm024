"""
异位词：长度一样，包含的字母都一样，每个字符出现的频率也一样，只是顺序不同而已
"""

# 排序
def isAnagram_1(s: str, t: str) -> bool:
    # if len(s) != len(t):
    #     return False
    # sort_s, sort_t = sorted(s), sorted(t)
    # if sort_s != sort_t:
    #     return False
    # return True
    return sorted(s) == sorted(t)


import collections


def isAnagram_2(s: str, t: str) -> bool:
    return collections.Counter(s) == collections.Counter(t)


# dict
def isAnagram_3(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = collections.defaultdict(int)
    for c in s:
        count[c] += 1
    for c in t:
        count[c] -= 1
        if count[c] < 0:
            return False
    return True


if __name__ == '__main__':
    s = 'rat'
    t = 'car'
    print(isAnagram_1(s, t))

