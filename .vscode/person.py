#define person class
class Person:

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

#inheritance
class Student(Person):
    def __init__(self, name, mark):
        super(Student, self).__init__(name)
        self.mark = mark

#use student class
person = Student("Diego", 10)
print(person.getName())