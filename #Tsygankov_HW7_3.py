#Tsygankov_HW7_3

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Функція для знаходження суми всіх значень у дереві
def sum_of_values(node):
    if node is None:
        return 0
    return node.val + sum_of_values(node.left) + sum_of_values(node.right)

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

    # Знаходження суми всіх значень у дереві
    total_sum = sum_of_values(root)
    print("Сума всіх значень у дереві:", total_sum)