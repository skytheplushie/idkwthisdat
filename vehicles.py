class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.__owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self):
        return f"model: {self.__model}"

    def get_horsepower(self):
        return f"engine power: {self.__engine_power}"

    def get_color(self):
        return f"color: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"owner: {self.__owner}")

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"cant change color on {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)


vehicle1.print_info()


vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'


vehicle1.print_info()

