class Student:
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return sum(self.marks) / len(self.marks) > 50

student1 = Student("Edyta", [60, 70, 75])
print(student1.name, student1.is_passed())

student2 = Student("Milena", [30, 40, 50])
print(student2.name, student2.is_passed())