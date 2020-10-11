'''

Open-closed Principle :        اگر برنامه نیاز به گسترش داشت ویژگی جدید رو بدون تغیر کد قبلی      
                           بشه اضاف کرد یعنی کد برای گسترش باز باشه ولی برای تغییر بسته باشه 

'''
# it is wrong
# class Animal:
# 	def __init__(self, name):
# 		self.name = name

# 	def sound(self):
# 		if self.name == 'cat':
# 			print('meow')
# 		elif self.name == 'dog':
# 			print('woof')

# a = Animal('cat')
# b = Animal('dog')

# a.sound()
# b.sound()


# this is better
class Animal:
	def __init__(self, name):
		self.name = name

	def sound(self):
		pass
	
class Cat(Animal):
	def sound(self):
		print('meow')
		
class Dog(Animal):
	def sound(self):
		print('woof')
		
a = Cat('cat')
b = Dog('dog')

a.sound()
b.sound()