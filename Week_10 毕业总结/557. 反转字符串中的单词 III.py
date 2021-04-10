

class Solution:
    def reverseWords(self, s: str) -> str:
        # 字符串反转 s[::-1]
        return ' '.join(i[:: -1] for i in s.split())


if __name__ == '__main__':
    solution = Solution()
    _s = "Let's take LeetCode contest"
    print(solution.reverseWords(_s))
