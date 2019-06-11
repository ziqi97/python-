import abc
class Pet(metaclass=abc.ABCMeta):
    def __init__(self,name):
        self.__name=name
    @abc.abstractmethod
    def eat(self):
        print('宠物在吃')
    @property
    def getname(self):
        return self.__name
    @getname.setter
    def setname(self,newname):
        self.__name=newname
class Cat(Pet):
    def __init__(self, getname,type):
      super().__init__(getname)
      self.__type=type
    @property
    def gettype(self):
        return self.__type

    @gettype.setter
    def setname(self, newtype):
        self.__name = newtype
    def eat(self):
        print('猫在吃')
cat=Cat('猫猫','cat')

class Pig(Pet):
    def __init__(self, getname,type):
      super().__init__(getname)
      self.__type=type
    @property
    def gettype(self):
        return self.__type

    @gettype.setter
    def setname(self, newtype):
        self.__name = newtype
    def eat(self):
        print('猪在吃')
pig=Pig('猪猪','pig')



class Dog(Pet):
    def __init__(self, getname,type):
      super().__init__(getname)
      self.__type=type
    @property
    def gettype(self):
        return self.__type

    @gettype.setter
    def setname(self, newtype):
        self.__name = newtype
    def eat(self):
        print('狗在吃')
dog=Dog('狗狗','dog')



class Master:
    def __init__(self,name,pet):
        self.__name=name
        self.__pet=pet

    @property
    def getname(self):
        return self.__name

    @property
    def getpet(self):
        return self.__pet
    def feed(self):
        print(self.getname,'准备好食物')
        print(self.getpet,'正在进食')
        self.siyang.eat()
mas1=Master('aa','dog')
mas2=Master('bb','Pet')
mas3=Master('cc','cat')

mas1.siyang=dog
mas2.siyang=pig
mas3.siyang=cat


mas1.feed()
mas2.feed()
mas3.feed()