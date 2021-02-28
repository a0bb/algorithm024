from typing import List


"""
贪心
在连续的交易日，第一天买，最后一天卖收益最大；等价于每天都做买卖
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        profit = 0
        # 当天与前一天做比较，所以从索引1开始，可以自然的避免数组溢出
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0:
                profit += tmp
        return profit


if __name__ == '__main__':
    s = Solution()
    _price = [7,1,5,3,6,4]
    print(s.maxProfit(_price))
