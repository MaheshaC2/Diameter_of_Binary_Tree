#Diameter of Binary Tree

def diameter(root):
    ans = 0

    def height(node):
        nonlocal ans
        if not node:
            return 0

        left = height(node.left)
        right = height(node.right)

        ans = max(ans, left + right)

        return 1 + max(left, right)

    height(root)
    return ans
