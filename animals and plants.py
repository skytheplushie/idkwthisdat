class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name


class Plants:
    edible = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} ate {food.name}')
        else:
            print(f"{self.name} does not like it, the animal wont eat {food.name}")
            self.alive = False


class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} ate {food.name}')
        else:
            print(f"{self.name} does not like it, the animal wont eat {food.name}")
            self.alive = False


class Flower(Plants):
    pass


class Fruit(Plants):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
