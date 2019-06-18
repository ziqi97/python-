def dog3(cls, *args, **kw):
    instances = {}

    def _dog():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@dog3
class Create3:
    s = 1

    def __init__(self, x=0):
        self.x = x

a = Create3()
b = Create3()
b.s = 3
print(a is b, a.s)