# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
      def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

          def traverse(node, visited = None):          # 1. no 'tree' parameter: the node IS the tree
              if visited is None:
                  visited = []                         # 2. list instead of set, so order stays
              if node is None:                         # 3. record empty spots too
                  visited.append(None)
                  return visited
              visited.append(node.val)                 # 4. store the value, not the node object
              traverse(node.left, visited)             #    children are .left and .right
              traverse(node.right, visited)
              return visited

          tree_p = traverse(p)
          tree_q = traverse(q)

          if tree_p == tree_q:
              return True
          else:
              return False


        