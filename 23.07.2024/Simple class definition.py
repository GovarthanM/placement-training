class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof!")

    def print_name(self):
        print(f"My name is {self.name}")

dog_name = input("Enter the name of your dog: ")

my_dog = Dog(dog_name)

my_dog.bark()
my_dog.print_name()
