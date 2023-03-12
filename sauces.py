import pizzas

class Decorator(pizzas.Pizza):

    def get_cost(self, cost):
        return cost

class Zeytin(Decorator):
    cost = 5

class Mantar(Decorator):
    cost = 11

class KeciPeyniri(Decorator):
    cost = 6

class Et(Decorator):
    cost = 12

class Sogan(Decorator):
    cost = 9

class Misir(Decorator):
    cost = 7            