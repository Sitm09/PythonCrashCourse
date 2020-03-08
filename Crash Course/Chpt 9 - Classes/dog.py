class Dog():
    """ A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initializes name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
#        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
#        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('tasha', 3)
your_dog.sit()
your_dog.roll_over()
