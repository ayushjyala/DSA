# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root==None:
            return TreeNode(val)
        cur=root
        while True:
            if cur.val<=val:
                if cur.right is not None:
                    cur=cur.right
                else:
                    cur.right=TreeNode(val)
                    break
            else:
                if cur.left is not None:
                    cur=cur.left
                else:
                    cur.left=TreeNode(val)
                    break
        return root