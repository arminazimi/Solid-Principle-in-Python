'''

Interface Segregation Principle: استفاده از چند رابط که هر کدام، فقط یک وظیفه را بر عهده دارد بهتر از استفاده از یک رابط چند منظوره است

'''
# it is not good
# from abc import ABC

# class Shape(ABC):
#     def Circle(self):
#         pass
#     def Square(self):
#         pass
#     def Rectangle(self):
#         pass

# class Circle(Shape):
#     def Circle(self):
#         pass
#     def Square(self):
#         pass
#     def Rectangle(self):
#         pass


# class Square(Shape):
#     def Circle(self):
#         pass
#     def Square(self):
#         pass
#     def Rectangle(self):
#         pass







# it is better
from abc import ABC
class Shape(ABC):
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        pass

class Square(Shape):
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        pass