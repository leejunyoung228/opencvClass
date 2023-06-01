class Dog:
    def __init__(self) -> None:
        self.__ownernames = "default name"
    
    @property
    def name(self):
        return self.__ownernames
    
    @name.setter
    def name(self, name):
        self.__ownernames = name

myDog = Dog()
myDog.name = "Happy"
print(myDog.name)