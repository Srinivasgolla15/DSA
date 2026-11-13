# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        res=[]
        if root is None:
            return []
        q=deque([root])
        while q:
            level =[] 
            size =len(q)
            for _ in range(size):
               node= q.popleft()
               level.append(node.val)
               if node.left:
                q.append(node.left)
               if node.right:
                q.append(node.right)
            res.append(level)
        return res

# time and space O(n)


        
       

        