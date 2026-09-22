# Задание 9: Деревья
# Создайте:
# 1. Бинарное дерево поиска
# 2. Методы добавления и поиска элементов
# 3. Обход дерева в разных порядках (in-order, pre-order, post-order)

""" Шаг 1. Создать класс Node. У узла должен быть элемент и два лепистка
    Шаг 2. Создать класс BinaryTree. В дереве должен быть корень
    Шаг 3. Метод добавления элементов
    Шаг 4. Метод поиска элемент
    Шаг 5. Обход дерево"""

# Шаг 1
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Шаг 2
class BinaryTree:
    def __init__(self):
        self.root = None

# Шаг 3
    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj
        s, p, fl_find = self.__find(self.root, None, obj.data)
        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        return obj

# Шаг 4
    def __find(self,node, parent, value):
        if value == node.data:
            return node, parent, True
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)
        return node, parent, False

# Шаг 5
    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)



v = [2,10,6,4,5,9,11]
t = BinaryTree()

for x in v:
    t.append(Node(x))
t.show_tree(t.root)


