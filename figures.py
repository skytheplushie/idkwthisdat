class Figures:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = list(sides)
        self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for val in [r, g, b]:
            if not isinstance(val, int) or val < 0 or val > 255:
                return False
            else:
                return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print('invalid color, using previous one')

    def __is_valid_sides(self, *sides):
        if isinstance(sides, tuple) and len(sides) == self.sides_count:
            return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figures):
    sides_count = 1

    def __init__(self, color, radius, *sides):
        super().__init__(color, *sides)
        self.__radius = radius

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figures):
    sides_count = 3

    def __init__(self, color, *sides, height):
        super().__init__(color, *sides)
        self.__height = height

    def get_square(self):
        return 0.5 * self.__height * sum(self.__sides)


class Cube(Figures):
    sides_count = 12

    def __init__(self, color, side):
        super().__init__(color, side)
        self.__side = side

    def get_volume(self):
        return self.__side ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15) 
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())