class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
draw([textbox, ddl])


# We don't need a base class called UIControl in order to achieve
# polymorphic behaviour, because Python supports duck typing, or it's dynamically typed.
# Having said that, having that UIControl as an ABC, is a good practice, because
# it enforces a common interface, or a common contract across all its derivatives.
# With this, we'll make sure that every kind of UIControl will have a draw method.
