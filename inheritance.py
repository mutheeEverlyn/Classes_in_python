class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def introduce(self):
        return f"Hi, my name is {self.name}. I am {self.age} years old and I work as a {self.occupation}."

#Student inheriting from  class Person
class Student(Person):
    def __init__(self, name, age, occupation, grade, school):
        super().__init__(name, age, occupation) # Calling the parent class constructor
        self.grade = grade
        self.school = school

    def study(self):
        return f"{self.name} is studying in grade {self.grade} at {self.school} ."

# Creating objects
person1 = Person("Everlyn", 30, "Software Engineer")
student1 = Student("Kamau", 16, "Student", 10, "Nanyuki High")


print(person1.introduce())   # Output: Hi, my name is Everlyn. I am 30 years old and I work as a Software Engineer.
print(student1.introduce())  # Output: Hi, my name is Kamau. I am 16 years old and I work as a Student.
print(student1.study())      #output: Kamau is studying in grade 10 at Nanyuki High .
