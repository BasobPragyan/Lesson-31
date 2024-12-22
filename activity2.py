from abc import ABC
class animalia(ABC):
    def move(self):
        pass

class human(animalia):
    def move(self):
        print("I can walk!")

class kangaroo(animalia):
    def move(self):
        print("I can jump!")

class snake(animalia):
    def move(self):
        print("I can crawl!")

class monkey(animalia):
    def move(self):
        print("I can move through branches!")


a1=human()
a1.move()
a2=kangaroo()
a2.move()
a3=snake()
a3.move()
a4=monkey()
a4.move()