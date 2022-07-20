class Rectangle(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def whoami(self):
        return 'rectangle'

    def area(self):
        return self.w * self.h


class Box(Rectangle):
    def __init__(self, w, h, d):
        super().__init__(w, h)
        self.d = d

    def whoami(self):
        return 'box'

    def volume(self):
        return self.w * self.h * self.d

if __name__ == '__main__':
    w = 3
    h = 4
    shape1 = Rectangle(w, h)
    print("It's a {}.".format(shape1.whoami()))
    print("Its area is {}.".format(shape1.area()))
    d = 5
    shape2 = Box(w, h, d)
    print("It's a {}.".format(shape2.whoami()))
    print("Its volume is {}.".format(shape2.volume()))
