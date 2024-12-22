from abc import ABC,abstractmethod
class student(ABC):
    def in_tro(self):
        print("I am a student")
    
    @abstractmethod
    def grade(self):
        pass

class senior(student):
    def display(self):
        print("I am in grade 9")
    def grade(self):
        print("I am a senior")


s1=senior()
s1.in_tro()
s1.display()