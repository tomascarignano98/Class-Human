"""
We're trying to build a custom container, or a data structure.
Just like lists and dictionaries.

"""


class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud.add("PYthon")
cloud.add("PythON")
cloud.add("pyTHon")
cloud.add("Pirata")
cloud.add("PiratA")
cloud.add("Josefa")
cloud.add("JoSeFa")
print(cloud.tags)
