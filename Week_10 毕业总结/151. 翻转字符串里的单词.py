

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


if __name__ == '__main__':
    solution = Solution()
    _s = "the sky is blue"
    print(solution.reverseWords(_s))
