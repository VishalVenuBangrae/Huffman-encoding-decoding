class TreeNode:

    def __init__(self, left, symbols, weight, right):
        self._left = left
        self._symbols = symbols
        self._weight = weight
        self._right = right

    def __str__(self):
        if self._left == None and self._right == None:
            return "TreeNode(None," + str(self._symbols) + "," + str(self._weight) + ",None)"
        elif self._left == None:
            return "TreeNode(None," + str(self._symbols) + "," + str(self._weight) + "," + str(self._right) + ")"
        elif self._right == None:
            return "TreeNode(" + str(self._left) + "," + str(self._symbols) + "," + str(self._weight) + ",None)"
        else:
            return "TreeNode(" + str(self._left) + "," + str(self._symbols) + "," + str(self._weight) + "," + str(
                self._right) + ")"
