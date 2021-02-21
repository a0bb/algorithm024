# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # terminator
        if not preorder and not inorder:
            return
        # process logic in current level
        # 前序遍历的第一个节点就是根节点，根据根节点拆分左子树和右子树
        root = TreeNode(preorder[0])
        # 获取根节点在中序遍历中的索引，根据这个索引即可拆分出左子树和右子树
        middle_index = inorder.index(preorder[0])
        # drill down
        # 递归获取左子节点
        root.left = self.buildTree(preorder[1: middle_index + 1], inorder[:middle_index])
        # 递归获取右子节点
        root.right = self.buildTree(preorder[middle_index + 1:], inorder[middle_index + 1:])

        return root
        # reverse status
