#Tsygankov_HW7_1
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Функція для знаходження найбільшого значення у дереві
def find_max(node):
    if node is None:
        return None
    while node.right:
        node = node.right
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
    root.right.left.left.left= Node(11)
    root.right.left.left.right= Node(12)

    # Знаходження найбільшого значення у дереві
    max_val = find_max(root)
    print("Найбільше значення у дереві:", max_val)