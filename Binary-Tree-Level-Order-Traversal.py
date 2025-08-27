# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:
            innerval = []
            qlen = len(queue)
            for i in range(qlen):
                node = queue.popleft()
                if node:
                    innerval.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if innerval:
                res.append(innerval)
        return res
                


        