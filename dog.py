from typing import Type


class Dog:

    def __init__(self,name,age):
        self.age=age
        self.name=name
    def sit(self):
        print("dog is now sitting")
    def showAge(self):
        print('it is',self.age,'years old')
class oldDog(Dog):
    def __init__(self,name,age):
        super().__init__(name,age)
myDog=oldDog("mi",6)
myDog.sit()
