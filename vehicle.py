
class Vehicle:
    __COLOR_VARIANTS = ['black', 'white', 'red']
    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self._model = model
        self.__engine_powewr = engine_power
        self.__color = color
    def get_model(self):
        return f'Модель: {self._model}'
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_powewr}'
    def get_color(self):
        return f'Цвет: {self.__color}'
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')
    def set_color(self, new_color):
        if new_color.lower() in (color.lower() for color in self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")





class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle = Sedan('Stefan', 'Buggati Chiron', '1200', 'Black')
vehicle.print_info()
print()
vehicle.set_color('pink')
print()
vehicle.print_info()
print()
vehicle.set_color('white')
vehicle.print_info()
print()
vehicle.owner = 'Kate'
vehicle.print_info()

