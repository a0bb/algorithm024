

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [i for i in S if i.isalpha()]
        res = []
        for i in S:
            if i.isalpha():
                res.append(letters.pop())
            else:
                res.append(i)
        return ''.join(res)


if __name__ == '__main__':
    solution = Solution()
    _s = "a-bC-dEf-ghIj"
    print(solution.reverseOnlyLetters(_s))
