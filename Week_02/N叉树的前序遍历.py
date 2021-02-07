
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root: Node):
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])

        return output


if __name__ == '__main__':
    s: Solution = Solution()
    # 不明白这里的传参应该如何进行？
