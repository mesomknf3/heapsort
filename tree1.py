class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def getlevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def printt(self):
        prefix = (" " * 4 * self.getlevel()) + ("|--" if self.parent else "")
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printt()


def build_tree():
    root = TreeNode("Food")

    italy = TreeNode("Italy")
    italy.add_child(TreeNode("Pizza"))
    italy.add_child(TreeNode("Lasgna"))
    italy.add_child(TreeNode("Pistacho Ice"))

    chinese = TreeNode("Chineese")
    chinese.add_child(TreeNode("Noodles"))
    chinese.add_child(TreeNode("Rice balls"))
    chinese.add_child(TreeNode("Fried Rice"))

    mexican = TreeNode("Mexican")
    mexican.add_child(TreeNode('Tacos'))
    mexican.add_child(TreeNode('Gyro'))
    mexican.add_child(TreeNode('Shawarma'))

    root.add_child(italy)
    root.add_child(chinese)
    root.add_child(mexican)

    return root

    # mexican.printt()


if __name__ == "__main__":
    root = build_tree()
    root.printt()
