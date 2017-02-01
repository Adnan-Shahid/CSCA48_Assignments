class BTNode(object):
    """A node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        """(BTNode, int, BTNode, BTNode) -> NoneType
        Initialize this node to store value and have children left and right,
        as well as depth 0.
        """
        self.value = value
        self.left = left
        self.right = right
        self.depth = 0  # the depth of this node in a tree
        
    def getval(self):
        return self.value
    def __str__(self):
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BTNode, str) -> str
        Return a "sideways" representation of the subtree rooted at this node,
        with right subtrees above parents above left subtrees and each node on
        its own line, preceded by as many TAB characters as the node's depth.
        """
        ret = ""

        if(self.right is not None):
            ret += self.right._str_helper(indentation + "\t") + "\n"
        ret += indentation + str(self.value) + "\n"
        if(self.left is not None):
            ret += self.left._str_helper(indentation + "\t") + "\n"
        return ret

    def set_depth(self, depth):
        self.depth = depth
        if self.left is not None:
            self.left.set_depth(depth+1)
        if self.right is not None:
            self.right.set_depth(depth+1)

    def leaves_and_internals(self):
        halp = self.leaves_helper()
        return (halp[1], halp[0])

    def leaves_helper(self, internals=set(), leaves=set(), root=0):
        root += 1
        if ((self.left is None) and (self.right is None)):
            leaves.add(self.value)
        if (((self.left is not None) or
             (self.right is not None)) and (root > 1)):
            internals.add(self.value)
        if (self.right is not None):
            self.right.leaves_helper(internals, leaves, root)
        if (self.left is not None):
            self.left.leaves_helper(internals, leaves, root)
        return internals, leaves, root

    def get_height(self):
        if (self.left is None and self.right is None):
            return 1
        else:
            left = right = 0
            if self.right is not None:
                right = self.right.get_height()
            if self.left is not None:
                left = self.left.get_height()
        return max(left, right) + 1

    def sum_to_deepest(self):
        left_height, right_height = 0, 0
        if self.right is None and self.left is None:
            return self.value
        if self.left is not None:
            left_height = self.left.get_height()
        if self.right is not None:
            right_height = self.right.get_height()
        if left_height > right_height and self.left is not None:
            return self.value + self.left.sum_to_deepest()
        if right_height > left_height and self.right is not None:
            return self.value + self.right.sum_to_deepest()
        if (right_height == left_height and
                (self.right is not None) and (self.left is not None)):
            return (max(self.value + self.left.sum_to_deepest(),
                        self.value + self.right.sum_to_deepest()))

if(__name__ == "__main__"):
    # just a simple tree to practice on
    my_tree = (BTNode(10, BTNode(3, BTNode(5), BTNode(2)),
                      BTNode(7, BTNode(4, BTNode(9), BTNode(8)), BTNode(6))))

    print(my_tree)

def pre(node, alist=[], count=0):
    if node == None:
        return None
    else:
        if count < 2:
            alist.append(node.getval())
            pre(node.left, alist, count+1)
            pre(node.right, alist, count+1)
        else:
            val = node.getval()
            if (val >= alist[0] or val >= alist[1]):
                biggest = max(alist[0], alist[1])
                if biggest == alist[0]:
                    alist[1] = val
                else:
                    alist[0] = val
            pre(node.left, alist, count+1)
            pre(node.right, alist, count+1)
    return alist[:2]



        

def post(node, alist=[]):
    if node == None:
        return None
    else:
        post(node.left, alist)
        post(node.right, alist)
        alist.append(node.getval())
    return alist    

def ino(node, alist=[]):
    if node != None:
        ino(node.left, alist)
        alist.append(node.getval())
        ino(node.right, alist)
    return alist
        
def avg(node):
    thing = get_sum(node)
    summ = 0
    for i in thing[0]:
        summ += i
    avg = summ/thing[1]
    return avg

def get_sum(node, alist=[]):
    if node != None:
        alist.append(node.getval())
        get_sum(node.left, alist)
        get_sum(node.right, alist)
    return (alist, len(alist))

        