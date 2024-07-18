class House:
    def __init__(self, name, number_of_floors):
        pass

    def go_to(self, new_floor):
        pass


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)


print(h1, h2)