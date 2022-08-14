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
	def __str__(self):
		return f"{self.x},{self.y}"
	def __eq__(self, other):
		return self.x==other.x and self.y==other.y
	def __gt__(self, other):
		return self.x > other.x and self.y>other.y

	def __add__(self, other):
		return Point(self.x + other.x,self.y + other.y)


point = Point.zero()
point2 = Point.zero()
point2.y=100
point2.x=100

point.y=50
point.x=50
print(point)
print(point2)
#
# print(dir(point))

print(point==point2)
print(point<point2)

print(point+point2)