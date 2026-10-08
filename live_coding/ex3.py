class Abc:
    def __init__(self, a, b, c):
        self.a = a
        self.__b = b
        self._c = c

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    @b.deleter
    def b(self):
        del self.__b

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, c):
        self._c = c

    @c.deleter
    def c(self):
        del self._c

    def __repr__(self):
        return f"Abc(a={self.a}, b={self.__b}, c={self._c})"

acb = Abc(1,2,3)

acb.c = 5

print(f'результать при создание {acb}')
print(acb.__dict__)
acb.b = 10
acb.c = 5
print(f'результать после создание {acb}')