from typing import List


"""
优先用10元的，5元的留着
遍历列表，按照不同的支付金额维护目前手上有的5元和10元的数量
"""
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for i in range(len(bills)):
            if bills[i] == 5:
                five += 1
            elif bills[i] == 10:
                if five <= 0:
                    return False
                five -= 1
                ten += 1
            elif bills[i] == 20:
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    _bills = [5,5,10,10,20]
    print(s.lemonadeChange(_bills))
