class Singleton:
    def __new__(cls):
        # cover create class object
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print(id(s))
print(s)

b = Singleton()
print(id(b))
print(b)

print(s is b)
