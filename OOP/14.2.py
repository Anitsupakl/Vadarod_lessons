class Dog:

    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f'{self.name}, Jump!!!')

    def run(self):
        print(f'{self.name}, Run!!!')

    def bark(self):
        print(f'{self.name}, Bark!!!')

    def change_name(self, new_name):
        self.name = new_name





rax = Dog(1.2, 43, 'Rax', 2)
print(rax.height)
print(rax.weight)
print(rax.name)
print(rax.age)
rax.jump()
rax.bark()
rax.run()
rax.change_name('Felix')
print(rax.name)
