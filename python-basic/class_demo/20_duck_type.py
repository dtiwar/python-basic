
from abc import ABC, abstractmethod

#  second example
# class UiControl:
# 	@abstractmethod
# 	def draw(self):
# 		pass


class DropDownList():
	def draw(self):
		print("Drop down list")


class TextBoxList():
	def draw(self):
		print("Text Box list")



def draw(controls):
	print(controls)
	print(type(controls))
	for control in controls:
		control.draw()


text_box = TextBoxList()
drop_down = DropDownList()
draw([text_box,drop_down])

