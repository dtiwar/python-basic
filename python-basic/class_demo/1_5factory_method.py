class Point:
	default_color ="red"
	def __init__(self,x,y):
		self.x=x
		self.y=y

	@classmethod
	def zero(cls):
		return cls(0,0)

	def draw(self):
		print(f"draw at {self.x} and {self.y}")
		print(self.default_color)

point = Point.zero()
point.draw()