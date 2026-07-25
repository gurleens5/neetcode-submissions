# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        q = deque([(root, float("-inf"))])

        while q:
            node, biggest = q.popleft()

            if biggest <= node.val:
                count += 1
            
            if node.left:
                q.append((node.left, max(node.val, biggest)))
            if node.right:
                q.append((node.right, max(node.val, biggest)))
        
        return count

           


