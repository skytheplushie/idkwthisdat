from random import choice
first = 'Мама мыла раму'
second = 'Рамена мало было'

r = list(map(lambda x, y: x == y, first, second))

print(r)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(*data_set, 'W', encoding='utf-8') as f:
            for item in data_set:
                f.write(str(item) + '\n')

    return write_everything


class Mysticball:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = Mysticball('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
