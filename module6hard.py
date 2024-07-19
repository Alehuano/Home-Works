from math import pi, sqrt


class Figure():
    sides_count = 0

    def __init__(self, color, *sides, filled=True):
        self.__color = list(color)
        self.__sides = list(sides)
        self.__filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for i in (r, g, b):
            if isinstance(i, int) and 0 <= i <= 255:
                return True
            else:
                return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        for j in sides:
            if isinstance(j, int) and j > 0 and len(sides) == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):
        return [*self.__sides] * self.sides_count

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __radius(self):
        return self.__len__ * (2 / pi)

    def get_square(self):
        return (self.__len__ ** 2) / (4 * pi)


class Triangle(Figure):
    sides_count = 3

    def __height(self):
        half_p = self.__len__ / 2
        h = (2 ** (half_p * (half_p - self.__sides[0])(half_p - self.__sides[1])(half_p - self.__sides[2]))
             ) / 2 * half_p
        return h

    def get_square(self):
        half_p = self.__len__ / 2
        s = sqrt((half_p * (half_p - self.__sides[0])(half_p - self.__sides[1])(half_p - self.__sides[2])))
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides, )
        if len(sides) == 1:
            self.__sides = sides * self.sides_count
        if len(self.get_sides()) != self.sides_count:
            self.set_sides(1 * self.sides_count)

    def get_volume(self):
        return self.__sides[1] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
