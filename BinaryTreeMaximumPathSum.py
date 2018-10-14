# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


# ugly!!
def _solve(root):
    if root.left is None and root.right is None:
        return root.val, root.val

    elif root.left is None:
        max_right_tree, max_right_subtree = _solve(root.right)
        return max(max_right_tree, root.val + max_right_subtree,
                   root.val), max(root.val + max_right_subtree, root.val)

    elif root.right is None:
        max_left_tree, max_left_subtree = _solve(root.left)
        return max(max_left_tree, root.val + max_left_subtree, root.val), max(
            root.val + max_left_subtree, root.val)

    else:
        max_left_tree, max_left_subtree = _solve(root.left)
        max_right_tree, max_right_subtree = _solve(root.right)
        max_subtree = root.val + max(0, max_left_subtree, max_right_subtree)
        max_tree = max(max_left_tree, max_right_tree,
                       max_left_subtree + max_right_subtree + root.val,
                       max_left_subtree + root.val,
                       max_right_subtree + root.val, root.val)
        return max_tree, max_subtree


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return _solve(root)[0]


if __name__ == '__main__':
    s = Solution()
    tree = [-1, 5, None, 4, None, None, 2, -4]
    root = TreeNode(-1)
    root.left = TreeNode(5)
    root.left.left = TreeNode(4)
    root.left.left.right = TreeNode(2)
    root.left.left.right.left = TreeNode(-4)

    s.maxPathSum(root)
