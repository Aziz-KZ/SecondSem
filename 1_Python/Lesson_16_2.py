class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x  # начальная позиция по оси X
        self.y = y  # начальная позиция по оси Y
        self.s = s  # шаг, на который черепашка двигается за ход

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError("Шаг не может быть меньше или равен 0!")

    def count_moves(self, x2, y2):
        dx = abs(self.x - x2)
        dy = abs(self.y - y2)
        moves_x = (dx + self.s - 1) // self.s
        moves_y = (dy + self.s - 1) // self.s
        return moves_x + moves_y

# Пример использования:
turtle = Turtle()  # стартовая позиция (0, 0), шаг 1

turtle.go_up()    # (0, 1)
turtle.go_right() # (1, 1)
turtle.evolve()   # шаг увеличен до 2
turtle.go_up()    # (1, 3)
turtle.go_left()  # (-1, 3)

# Подсчет шагов до точки (2, 2)
print(turtle.count_moves(2, 2))

# Попробуем уменьшить шаг
turtle.degrade()
print(turtle.s)
