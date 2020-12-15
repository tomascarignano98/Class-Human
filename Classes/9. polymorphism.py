from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
draw([textbox, ddl])


# Our draw function doesn't know what kind of control is working 
# with, this is determined at runtime. It simply iterates over the list
# of controls and calls the draw method at each object.

# This is called polymorphism, from poly and morhpism; which means "many forms".

# In this example, our draw method is taking many different forms, and this is determined at runtime. 
# So, depending on the type of control object that we're working with at runtime,
# this draw method, takes a different form. It may be the draw method in a 
# TextBox, or DropDownList, etc.
