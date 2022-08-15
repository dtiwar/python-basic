class Point:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __eq__(self, other):
		return self.x==other.x and self.y==other.y

p1= Point(1,2)
p2= Point(1,2)
print(p1==p2)

from collections import namedtuple

Point2=namedtuple("Point2",["x","y"])

p3 = Point2(x=1,y=2)
p4 = Point2(x=1,y=2)

print(p3==p4)

