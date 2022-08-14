class flayer:
	def fly(self):
		print("fly")


class swimmer:
	def swim(self):
		print("swim")


class flayingFish(flayer, swimmer):
	def eat(self):
		print("eat")


