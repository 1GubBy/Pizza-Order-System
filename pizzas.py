class Pizza():
    
    def get_description(self, description):
        return description

    def get_cost(self, cost):
        return cost

class ClassicPizza(Pizza):

    description = "Klasik Pizza, ince hamur üzerine domates ve kaşar peynirinin kombin edilmesiyle yapılan fiyat performans bir üründür. "
    cost = 50
    
class MargheritaPizza(Pizza):

    description = "Margherita Pizza domates, mozarella, fesleğen, zeytinyağı ve tuzla yapılan Napoli menşeili pizzadır. Bu arkadaşa bayılmamak elde değil, ağzınızın tadını bilen birisine benziyorsunuz."
    cost = 55
    
class TurkPizza(Pizza):

    description = "Türk Pizzası, damak zevkinize göre hamur üzerine kaşar, sucuk, pastırma gibi malzemelerinden yapılır ve sizlere tam anlamıyla bir lezzet şöleni yaşatır. "
    cost = 59.90

class SadePizza(Pizza):

    description = "Sade Pizza, salça ekmek misali hamur üzerine sade domates sosundan oluşur, çocukların favori pizzasıdır."
    cost = 45
