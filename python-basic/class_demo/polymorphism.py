from abc import ABC, abstractmethod


class A:
	@abstractmethod
	def a(self):
		pass


class B(A):
	def a(self):
		print("in B class")


class C(A):
	def a(self):
		print("in C class")


def a(control):
	for i in control:
		i.a()


b = B()
# a(b)

c = C()
# a(c)
a([b, c])

from abc import ABC, abstractmethod


#  second example
class UiControl:
	@abstractmethod
	def draw(self):
		pass


class DropDownList(UiControl):
	def draw(self):
		print("Drop down list")


class TextBoxList(UiControl):
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

