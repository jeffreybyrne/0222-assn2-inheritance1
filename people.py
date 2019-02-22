# 1. Let's start by creating two classes: one called Student and another
# called Instructor.
# 2. The student class has an instance method called learn that returns
# "I get it!".
# 3. The instructor class has an instance method called teach that returns
# "An object is an instance of a class".
# 4. Both the instructor and the student have names. We know that instructors
# and students are both people. Create a parent Person class that contains the
# attribute name and an __init__() method to set the name.
# 5. Both the instructor and the student should also be able to do a greeting,
# like "Hi, my name is so-and-so". Where's the best place to put this
# common method?
# 6. Create an instance of instructor whose name is "Nadia" and call
# their greeting.
# 7. Create an instance of student whose name is "Chris" and call
# their greeting.
# 8. Call the teach method on your instructor instance and call the learn
# method on your student. Next, call the teach method on your student instance.
# What happens? Why doesn't that work? Leave a comment in your program
# explaining why.


class People:

    def __init__(self, new_name):
        self.name = new_name

    def greet(self):
        return "Hi, my name is {}.".format(self.name)


class Student(People):

    def learn(self):
        return "I get it!"


class Instructor(People):

    def teach(self):
        return "An object is an instance of a class."


nadia = Instructor("Nadia")
print(nadia.greet())
chris = Student("Chris")
print(chris.greet())
print(nadia.teach())
print(chris.learn())
# print(chris.teach()) This won't work because the Student inherits from the
# People class, but the teach method is for the Instructor class only
