# Assignment 1: Design Your Own Class! 🏗️
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.
# Activity 2: Polymorphism Challenge! 🎭

# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).


class Fruits:
    def __init__(self, state, flavor, color):
        self.state = state
        self.flavor = flavor
        self.color = color

    def fresh(self):
        print(f"{self.state} is fresh.")
    def processed(self):
        print(f"{self.state} is processed.")

class Juice(Fruits):
    def __init__(self, state, flavor, color, juice_type):
        super().__init__(state, flavor, color)
        self.juice_type = juice_type

    def fresh(self):
        print(f"{self.state} is fresh juice.")
    def processed(self):
        print(f"{self.state} is processed juice.")