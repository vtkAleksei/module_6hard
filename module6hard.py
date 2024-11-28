import math

class Figure:
    sides_count = 0 #количество сторон

    def __init__(self, sides, color, filled):
        self.__sides = sides # (список размеров сторон (целые числа))
        self.__color = color # (список цветов в формате RGB)
        self.filled = filled # (закрашенный, bool)

    def get_color(self):
        return self.__color

    def __is_valid_color (self, r, g, b):
        if 0 < r < 255 and 0 < g < 255 and 0 < b < 255:
            return True
        else:
            print('Параметры цвета указаны неверно.')
            return False

    def set_color (self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b

    def __is_valid_sides (self, *new_sides):
        list_sides = list(new_sides)
        if len(list_sides) == self.sides_count and all(map(lambda x: x > 0, list_sides)):
            return True
        else:
            print(f'Неправильно указано количество сторон. Должно быть {self.sides_count}')
            return False

    def get_sides (self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
            return self.__sides




class Circle (Figure):
    sides_count = 1

    def __init__(self, sides, color, filled, radius):
        super().__init__(sides, color, filled)
        self.__radius = round(self.get_sides()[0] / (2 * math.pi), 2)

    def get_square(self):
        print(self.__radius)
        return round(math.pi * self.__radius ** 2, 2)



class Triangle (Figure):
    sides_count = 3

    def get_square(self):
        p = 1/2 * (len(self))
        return round(math.sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])), 2)



class Cube (Figure):
    sides_count = 12

    def __init__(self, sides, color, filled ):
        list_sides = []
        for i in range (1, 13):
            list_sides.append(sides)
        super().__init__(list_sides, color, filled)

    def get_volume(self):
        return self.get_sides()[0] ** 3



f1 = Figure([],[255,255,255], True)
c1 = Circle([9],[0,0,0], False, 0.0)
t1 = Triangle([3,3,3],[200,200,200], True)
cube1 = Cube(6,[100,100,100], True)

print(c1.get_color())
c1.set_color(55, 66, 77) # Изменится
print(c1.get_color())

print(cube1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

print(cube1.get_sides())
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())

print(c1.get_sides())
c1.set_sides(15) # Изменится
print(c1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(c1))
# Проверка объёма (куба):
print(cube1.get_volume())
