class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrrr'
        super.__init__()

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'Chirp-chirp'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Eagle, Horse):
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)
