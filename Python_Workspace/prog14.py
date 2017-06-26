#class structure (parent class)
class Restaurant:
    def __init__(self, owner_name, rating, menu):
        self.ownner_name = owner_name
        self.rating = rating
        self.menu = menu

#class object
KFC = Restaurant('Abhishek',4.5,{})
Dominos = Restaurant('Parmar',4.5,{})

#child class
class VegRestaurant(Restaurant):
    def __init__(self):
        print "constructor"