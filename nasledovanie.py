

class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False


class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False


class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Fruit(Plant):
    def __init__(self, name):
        self.edible = True
        super().__init__(name)
        self.edible = True


class Flower(Plant):
    pass


mammal = Mammal('dog')
predator = Predator('lion')
fruit = Fruit('apple')
flower = Flower('rose')

print(mammal.name)
print(predator.name)
print(fruit.name)
print(flower.name)

print(mammal.alive)
print(predator.alive)
print(predator.fed)
print(mammal.fed)

mammal.eat(fruit)
predator.eat(flower)
print(predator.alive)
print(mammal.alive)