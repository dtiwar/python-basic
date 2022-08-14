class Point:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		print("draw")
	def draw(self):
		print("draw")

mouse=Point(1,1)
print(mouse.x,mouse.y)
mouse.draw()
print(isinstance(mouse,Point))

