from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(animal):
    def sound(self):
        print("bow bow")
class cat(animal):
    def sound(self):
        print("meow")
# d1=dog()
# c1=cat()
# d1.sound()
# c1.sound()
animals = [dog(), cat()]
for a in animals:
    a.sound()


# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# # Example usage
# if __name__ == "__main__":
#     circle = Circle(5)
#     rectangle = Rectangle(4, 6)
    
#     print(f"Area of the circle: {circle.area()}")
#     print(f"Area of the rectangle: {rectangle.area()}")