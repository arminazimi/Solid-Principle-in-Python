'''

Liskov substitution principle : یعنی تو هر کلاس اگه جای ابجکت ها رو عوض کردیم مشکلی پیش نیاد

'''

# its wrong becuase penguin cant fly 
# class Bird:
#     def __init__(self, name):
#         self.name = name
#     def fly(self):
#         print(f'{self.name} is flying')

# a1 = Bird('eagle')
# a2 = Bird('penguin')

# it is better
class Bird:
    def __init__(self, name):
        self.name = name
    
class FlyingBird(Bird):
    def fly(self):
        print(f'{self.name} is flying')

a2 = Bird('penguin') 

a1 = FlyingBird('eagle')
a1.fly()