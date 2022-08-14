# Example of inheritance

class Animal:
	def __init__(self):
		self.age = 1
		print("Animal constructor")

	def eat(self):
		print("eat")


class Mammal(Animal):
	def __init__(self):
		super().__init__()
		self.weight = 2
		print("Mammal constructor")


	def walk(self):
		print("walk")


m = Mammal()

print(m.weight)
print(m.age)
