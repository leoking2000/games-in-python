class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Cell(Point):
    def __init__(self, x, y, block_size, color):
        super().__init__(x,y)
        self.block_size = block_size
        self.color = color

    def draw(self, gameDisplay):
        from pygame import draw
        draw.rect(gameDisplay, self.color, [self.x, self.y, self.block_size, self.block_size])


class Apple(Cell):

    def __init__(self, block_size, color, display_width, display_height):
        super().__init__(0, 0, block_size, color)
        self.display_width = display_width
        self.display_height = display_height
        self.update()

    def update(self):
        import random
        self.x = round(random.randrange(0, self.display_width - self.block_size) / self.block_size) * self.block_size
        self.y = round(random.randrange(0, self.display_height - self.block_size) / self.block_size) * self.block_size

class MovingCell(Cell):

    def __init__(self, x, y, block_size, color):
        super().__init__(x,y, block_size, color)
        self.speedX = self.block_size
        self.speedY = 0

    def update(self):
        self.x += self.speedX
        self.y += self.speedY

    def go_down(self):
        if self.speedY == 0:
            self.speedY = self.block_size
            self.speedX = 0
    def go_up(self):
        if self.speedY == 0:
            self.speedY = -self.block_size
            self.speedX = 0
    def go_right(self):
        if self.speedX == 0:
            self.speedX = self.block_size
            self.speedY = 0
    def go_left(self):
        if self.speedX == 0:
            self.speedX = -self.block_size
            self.speedY = 0

class Snake():

    snake_list = []
    snake_length = 3

    def __init__(self, x, y, block_size, color, display_width, display_height):
        self.leadCell = MovingCell(x, y, block_size, color)
        self.display_width = display_width
        self.display_height = display_height

    def update(self):
        x = self.leadCell.x
        y = self.leadCell.y
        self.leadCell.update()
        self.snake_list.append(Cell(x, y, self.leadCell.block_size, self.leadCell.color))
        if len(self.snake_list) > self.snake_length:
            del self.snake_list[0]

    def draw(self, gameDisplay):
        self.leadCell.draw(gameDisplay)
        for cell in self.snake_list:
            cell.draw(gameDisplay)
    def go_down(self):
        self.leadCell.go_down()
    def go_up(self):
        self.leadCell.go_up()
    def go_right(self):
        self.leadCell.go_right()
    def go_left(self):
        self.leadCell.go_left()
    def reset(self):
        self.leadCell.x = self.display_width // 2
        self.leadCell.y = self.display_height // 2
        self.snake_length = 3
        self.snake_list = []

    def outside_the_boundaries(self):
       return self.leadCell.x >= self.display_width or self.leadCell.x < 0 \
           or self.leadCell.y >= self.display_height or self.leadCell.y < 0
    def eat_itself(self):
        for cell in self.snake_list:
            if cell.x == self.leadCell.x and cell.y == self.leadCell.y:
                return True
        return False
    def found_Apple(self, apple):
        return apple.x == self.leadCell.x and apple.y == self.leadCell.y
    def eat_aplle(self, apple):
        apple.update()
        self.snake_length +=1

