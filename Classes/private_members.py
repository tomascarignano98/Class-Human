class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("PYthon")
cloud.add("PythON")
cloud.add("pyTHon")
cloud.add("Pirata")
cloud.add("PiratA")
cloud.add("Josefa")
cloud.add("JoSeFa")


"""
self.__attributename = 

This is how we create private members, that is to say, 
members that are not reachable from the outside. 

Now, this is not quite true, they can still be reached from the
outside but it's harder. 

This isn't about privacy, per se, but it's more of a convention 
to prevent accidental access to this private members.


An example would be this:
print(cloud.tags["PYTHON"])

Here, our programm would crash, because it would not find any key named "PYTHON", 
since all the keys inside the dictionary were stored in lower case.


Another example is when we have methods that only serve their 
purpose under the hood, but we don't want them to appear in the surface.
These methods would be polluting the interface of our object, and it 
would be liek having a TV remote control with 100 buttons.

we want our objects and classes to have the minimum number of 
methods exposed to the outside

"""
