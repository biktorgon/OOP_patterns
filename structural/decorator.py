class Man:
    def __init__(self, name):
        self._name = name

    def say(self):
        print('My name is %s' % self._name)


class Jetpack:
    def __init__(self, man):
        self._man = man

    def __getattr__(self, item):
        return getattr(self._man, item)

    def fly(self):
        print('%s fly on jetpack' % self._man._name)


man = Man('Alex')
man_jetpack = Jetpack(man)
man_jetpack.say()
man_jetpack.fly()
