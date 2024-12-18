import os
os.system('cls')

class Person:
    species = "Homo sapiens"
    def __init__(self, section, section1, section2):
        self.name = "Kirby"
        self.age = 19
        self.section = section
        self.section1 = section1
        self.section2 = section2

    def display(self, string = "world"):
        print(string, self.name, self.age)

person1 = Person(tuple)
print(person1.display("hello"))