

# 位运算
class Solution(object):
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res


""" 参考
# bit操作
& 符号，x & y ，会将两个十进制数在二进制下进行与运算
| 符号，x | y ，会将两个十进制数在二进制下进行或运算
^ 符号，x ^ y ，会将两个十进制数在二进制下进行异或运算
<< 符号，x << y 左移操作，最右边用 0 填充
>> 符号，x >> y 右移操作，最左边用 0 填充
~ 符号，~x ，按位取反操作，将 x 在二进制下的每一位取反

# 整数集合set位运算
# 整数集合做标志时，比如回溯时的visited标志数组
vstd 访问 i ：vstd | (1 << i)
vstd 离开 i ：vstd & ~(1 << i)
vstd 不包含 i : not vstd & (1 << i)

并集 ：A | B
交集 ：A & B
全集 ：(1 << n) - 1
补集 ：((1 << n) - 1) ^ A
子集 ：(A & B) == B
判断是否是 2 的幂 ：A & (A - 1) == 0
最低位的 1 变为 0 ：n &= (n - 1)
最低位的 1：A & (-A)，最低位的 1 一般记为 lowbit(A)
"""

