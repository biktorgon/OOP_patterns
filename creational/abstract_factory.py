class AbstractFactory:
    def create_drink(self):
        raise NotImplementedError()

    def create_food(self):
        raise NotImplementedError()


class Drink:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Food:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class ConcreteFactory1(AbstractFactory):
    def create_drink(self):
        return Drink('Coca-Cola')

    def crate_food(self):
        return Food('Hamburger')


class ConcreteFactory2(AbstractFactory):
    def create_drink(self):
        return Drink('Pepsi')

    def create_food(self):
        return Food('Cheeseburger')


def get_factory(ident):
    if ident == 0:
        return ConcreteFactory1()
    elif ident == 1:
        return ConcreteFactory2()


factory = get_factory(1)
print(factory.create_drink())
print(factory.create_food())

