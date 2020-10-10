'''

هر کلاس یا فانکشن باید فقط و فقط مسئول انجام دادن یک کار باشه

'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f'{self.name} is {self.age} years old'

    # def db_save(self):   its wrong
    #     pass


# its better
class Db:
    def db_save(self):
        pass