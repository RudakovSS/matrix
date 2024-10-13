
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return True

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

my_house = House('Эльбрус', 20)
my_house_2 = House('Эверест', 35)
my_house.go_to(14)
my_house.go_to(45)
print(my_house)
print(len(my_house))
print(my_house == my_house_2)
print(my_house < my_house_2)
print(my_house <= my_house_2)
print(my_house > my_house_2)
print(my_house >= my_house_2)
print(my_house != my_house_2)
my_house += 5
print(my_house)
new_house = my_house + 5
print(new_house)
my_house += 7
print(my_house)
