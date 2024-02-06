#Tsygankov_HW7_2

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Функція для знаходження найменшого значення у дереві
def find_min(node):
    if node is None:
        return None
    while node.left:
        node = node.left
    return node.val

if __name__ == '__main__':
    # Створення дерева
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)
    root.left.left.right = Node(7)
    root.right.left = Node(8)
    root.right.right = Node(9)
    root.right.left.left = Node(10)
    root.right.left.left.left = Node(11)
    root.right.left.left.right = Node(12)

    # Знаходження найменшого значення у дереві
    min_val = find_min(root)
    print("Найменше значення у дереві:", min_val)