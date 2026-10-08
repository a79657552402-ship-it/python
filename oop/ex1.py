# Создайте класс BasicShape.
# Данный класс представляет из себя многогранник с любым количеством точек,
# переданных при инициализации в формате [(x1, y1), (x2, y2), (x3, y3), …].
#
# Для класса BasicShape напишите методы perimeter и square,
# вычисляющие периметр и площадь фигуры соответственно
# (считаем, что две последовательно идущие точки, переданные при инициализации объекта, образуют грань,
# а последняя точка образует грань с первой в списке). Для вычисления площади используется Формула площади Гаусса.
#
# Создайте новый класс Quadrilateral (четырехугольник), который наследуется от BasicShapes.
# Убедитесь, что он верно отрабатывает методы perimeter и square, определенные в родительском классе.
# Добавьте в новый класс методы is_rectangle и is_square, проверяющие,
# является ли четырехугольник прямоугольником (противоположные стороны и диагонали равны) и квадратом (все стороны и диагонали равны) соответственно.
#
# Добавьте статический метод, вычисляющий длину ребра фигуры, и используйте его для методов, имплементированных в предыдущем задании.
#
# Добавьте в класс BasicShape метод add(coordinate: tuple[float, float]), который добавляет новую точку в многоугольник.
# Сделайте так, чтобы он не работал в классе Quadrilateral.
# Сделайте так, чтобы методы perimeter, square, is_rectangle и is_square вели себя как поля

# Реализуйте поведение класса, при котором использование его объектов в арифметических выражениях будет выполнять сложение,
# вычитание, умножение или деление их площадей: object1 + object2 == object1.square + object2.square

# Создайте класс Shapes и имплементируйте в нем методы:
# add_shape – добавляет фигуру класса BasicShape в класс Shapes.
# square – находит суммарную площадь фигур, добавленных в Shapes (без учета наложения фигур).
# perimeter – находит суммарный периметр фигур, добавленных в Shapes (без учета наложения фигур).
# remove_shape – удаляет фигуру из класса Shapes.
# Добавьте в класс Shapes метод add, который добавляет новую точку в одну из фигур. Сделайте так,
# чтобы добавить точку можно было только через метод Shapes.add(),
# исключив возможность использования метода BasicShapes.add() фигуры, содержащейся внутри Shapes.
# Превратите класс Shapes в контекстный менеджер. Его поведение должно быть следующим:
# внутри управляющей конструкции with вы будете добавлять в Shapes новые фигуры,
# а при выходе из нее – выводить в терминал информацию о суммарной площади всех фигур, добавленных в Shapes.
# Создайте свой контекстный менеджер (творческое задание).

import math


class BasicShape:

    def __init__(self, points):

        self._points = [tuple(p) for p in points]  # принимаем список кординат

    # длина одной стороны по координатом двух точек
    @staticmethod
    def _line(p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    # расчёт пириметра
    @property
    def perimeter(self):
        n = len(self._points)
        total = 0
        for i in range(n):
            total += self._line(self._points[i], self._points[
                (i + 1) % n])  # остаток от деления нужен что б замкнуть последнюю точку с первой
        return total

    """Пример расчёта
Найдём площадь пятиугольника с вершинами A(3;4),B(5;6),C(9;4),D(12;8),E(5;11):
Сумма произведений «вниз» (xᵢ·yᵢ₊₁): 
3⋅6+5⋅4+9⋅8+12⋅11+5⋅4=262.
Сумма произведений «вверх» (xᵢ₊₁·yᵢ): 
6⋅5+4⋅9+4⋅12+8⋅5+11⋅3=195.
Площадь: S=0.5⋅∣262−195∣=33,5."""

    @property
    def square(self):
        n = len(self._points)
        s = 0
        for i in range(n):
            x1, y1 = self._points[i]
            x2, y2 = self._points[(i + 1) % n]
            s += x1 * y2 - x2 * y1
        return abs(s) / 2

    def add(self, coordinate: tuple[float, float]):
        self._points.append(tuple(coordinate))

    def __add__(self, other):
        return self.square + other.square

    def __sub__(self, other):
        return self.square - other.square

    def __mul__(self, other):
        return self.square * other.square

    def __truediv__(self, other):
        return self.square / other.square

    def __repr__(self):
        return f"{type(self).__name__}({self._points})"


# проверяем прямоугольник
c = BasicShape([(0, 0), (4, 0), (4, 3), (0, 3)])
c.add((6, 7))
print(f"Пиреметр многоугольника {c.perimeter}")
print(f"Площадь многоугольника {c.square}")

basic_shape = BasicShape([(0, 0), (0, 1), (1, 0), (1, 1)])
print(f"basic_shape: {basic_shape.square}")


class Quadrilateral(BasicShape):
    """AB==CD, BD==AC, AD==BC"""

    @property
    def is_rectangle(self):
        p = self._points
        return (
                self._line(p[0], p[1]) == self._line(p[2], p[3])
                and self._line(p[1], p[2]) == self._line(p[3], p[0])
                and self._line(p[0], p[2]) == self._line(p[1], p[3])
        )

    """AB==CD==BD==AC, AD==BC"""

    @property
    def is_square(self):
        p = self._points
        return (
                self._line(p[0], p[1]) == self._line(p[1], p[2])
                == self._line(p[2], p[3]) == self._line(p[3], p[0])
                and self._line(p[0], p[2]) == self._line(p[1], p[3])
        )

    def add(self, coordinate: tuple[float, float]):
        raise AttributeError("Нельзя добавлять новых точек к квадрату")


# проверяем квадрат
c = Quadrilateral([(2, 3), (7, 3), (7, 8), (2, 8)])
d = Quadrilateral([(2, 3), (7, 3), (7, 8), (2, 8)])

print(f"Пиреметр квадрата {c.perimeter}")
print(f"Площадь квадрата {c.square}")
print(c.is_rectangle)
print(c.is_square)
# c.add((6, 7))

print(c + d)
print(c - d)
print(c * d)
print(c / d)


# Создайте класс Shapes и имплементируйте в нем методы:
# add_shape – добавляет фигуру класса BasicShape в класс Shapes.
# square – находит суммарную площадь фигур, добавленных в Shapes (без учета наложения фигур).
# perimeter – находит суммарный периметр фигур, добавленных в Shapes (без учета наложения фигур).
# remove_shape – удаляет фигуру из класса Shapes.

class Shapes:
    def __init__(self):
        self._shapes = []

    def add_new(self, shape):
        return self._shapes.append(shape)

    @property
    def square(self):
        return sum(shape.square for shape in self._shapes)

    @property
    def perimeter(self):
        return sum(shape.perimeter for shape in self._shapes)

    def remove_shape(self, shape):
        return self._shapes.remove(shape)

# Добавьте в класс Shapes метод add, который добавляет новую точку в одну из фигур. Сделайте так,
# чтобы добавить точку можно было только через метод Shapes.add(),
# исключив возможность использования метода BasicShapes.add() фигуры, содержащейся внутри Shapes.

c = Quadrilateral([(2, 3), (7, 3), (7, 8), (2, 8)])
d = Quadrilateral([(2, 3), (7, 3), (7, 8), (2, 8)])
r = Quadrilateral([(2, 3), (7, 3), (7, 8), (2, 8)])

new_shape = Shapes()
new_shape.add_new(c)
new_shape.add_new(d)
print(f"Сумма площадей shape {new_shape.square}")
print(f"Сумма периметров shape {new_shape.perimeter}")
new_shape.add_new(r)
print(f"Сумма площадей shape {new_shape.square}")
print(f"Сумма периметров shape {new_shape.perimeter}")
new_shape.remove_shape(r)
print(f"Сумма площадей shape {new_shape.square}")
print(f"Сумма периметров shape {new_shape.perimeter}")

