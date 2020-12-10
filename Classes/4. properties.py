"""
class Product:
    def __init__(self, price):
        self.price = price

    def item(self):
        return self.price


chips = Product(20)


# Cool right? we have a product object that we can assign
a price to.

# But what if we accidentally enter a negative price?
How can we avoid such an error?

"""

"""
# Like this:

class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


# Okay cool, but what the hell is properties?
A property is an object that sits in front of an attribute
and allows us to get or set the value of that attribute.
In this case, there's a way to implement the property function
and achieve the same soultion in a cleaner way.

# the built-in property function what does is to take four paramenter:
for getting the value of an attribute, for setting, for deleting, for documentation.
Each parameter is a function for some action.
Now, the property object or also the attribute (the object we assign the function to),
will use the first function for reading the value of that attribute.

price = property(get_price, set_price)

# we have a decorator for creating a property. @property


"""


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


"""
when python interpretor sees this code it will automatically
create a property object called price
"""

"""
the name of our decorator needs to start with
the name of our property price, so that they work together.
"""
"""
the cool thing is that we can use our price property
like a regular attribute.
"""

chips = Product(-20)
print(chips.price)
