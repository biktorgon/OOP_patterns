class Graphic:
    def draw(self):
        raise NotImplementedError()

    def add(self, obj):
        raise NotImplementedError()

    def remove(self, obj):
        raise NotImplementedError()

    def get_child(self, index):
        raise NotImplementedError()


class Line(Graphic):
    def draw(slef):
        print('Line')


class Rectangle(Graphic):
    def draw(self):
        print('Rectangle')


class Text(Graphic):
    def draw(self):
        print('Text')


class Picture(Graphic):
    def __init__(self):
        self._children = []

    def draw(self):
        print('Picture')
        for obj in self._children:
            obj.draw()

    def add(self, obj):
        if isinstance(obj, Graphic) and obj not in self._children:
            self._children.append(obj)

    def remove(self, obj):
        index = self._children.index(obj)
        del self._children[index]

    def get_child(self, index):
        return self._children[index]


pic = Picture()
pic.add(Line())
pic.add(Rectangle())
pic.add(Text())
pic.draw()

line = pic.get_child(0)
line.draw()
