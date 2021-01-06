def wrap_all(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            print(attr)


class Hello:
    def hello1(self):
        pass

    def hello2(self):
        pass


for attr in Hello.__dict__:
    print(attr)
