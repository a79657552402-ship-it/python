# Задание 8: Связанные списки
# Реализуйте:
# 1. Простой односвязный список
# 2. Методы добавления и удаления элементов
# 3. Поиск элемента в списке
# 4. Сравните производительность с обычным списком Python

"""Алгоритм:
   Шаг 1: сделать класс с двумя перемеными, последний элемент списка и длина всего списка.
   Шаг 2: нужно сделать ноду.
   Шаг 3: нужно сделать список.
   Шаг 4: метод добавления.
   Шаг 5: метод удаления.
   Шаг 6: метод поиска элемента в списке.
   Шаг 7: сделать list.
   Шаг 8: Сравнить производительность."""

# Шаг 1
class LinkedList:
    head = None
    length = 0
    # Шаг 2
    class Node:
        element = None
        next_node = None

        # Шаг 3
        def __init__(self, element, next_node=None):   # мы создаём ноду, поэтому следуюещего элементы нет.
            self.element = element
            self.next_node = next_node

    # Шаг 4
    def append(self, element):
        if not self.head:  # если нет элементов в списке
            self.head = self.Node(element)
            self.length +=1
            return element

        node = self.head  # если в списке есть элементы
        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)
        self.length += 1
        return element

    # Шаг 5
    def __delitem__(self, key):
        # если удаляем с нулевого элмента
        if key == 0:
            self.head = self.head.next_node
            self.length -= 1
            return

        i = 0
        node = self.head
        while i < key - 1:
            node = node.next_node
            i += 1

        node.next_node = node.next_node.next_node
        self.length -= 1

    # Шаг 6
    def __getitem__(self, item):
        i = 0
        node = self.head
        while i < item:
            node = node.next_node
            i +=1
        return node.element

    def __str__(self):  # переопределяем метод str что б выводить элементы в line
        node = self.head
        line = '['
        while node.next_node:
            line += str(node.element) + ', '
            node = node.next_node
        line += str(node.element) + ']'
        return line

new_linked_list = LinkedList()
new_linked_list.append(4)
new_linked_list.append(6)
new_linked_list.append(1)
new_linked_list.append(7)
new_linked_list.append(9)
new_linked_list.append(0)
new_linked_list.append(2)
new_linked_list.append(8)
print(new_linked_list)
print(new_linked_list[2])
del new_linked_list[2]
print(new_linked_list)