class Point:
	default_color ="red"
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def draw(self):
		print(f"draw at {self.x} and {self.y}")
		print(self.default_color)

mouse=Point(1,2)

mouse2=Point(1,2)


# print(mouse.z)
# print(mouse2.z)

# print(mouse.default_color)
# print(mouse2.default_color)

# mouse2.default_color='green'
Point.default_color='yellow'
# print(mouse.default_color)
# print(mouse2.default_color)




print("======")
mouse.draw()
print("----")
mouse2.draw()






