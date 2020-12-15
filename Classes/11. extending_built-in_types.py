# Did you know you can also use inheritance with the built-in types?
# And you can add more features than it already has.

class Text(str):
    def duplicate(self):
        return self * 2


class TrackableList(list):
    def append(self, object):
        print("Append method called")
        super().append(object)


list = TrackableList()
list.append(1)
