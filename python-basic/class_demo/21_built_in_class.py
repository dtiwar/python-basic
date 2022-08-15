class Text(str):
	def duplicate(self):
		return self + self


# txt=Text("python")
# print(txt.duplicate())
# print(txt.lower())
# print(txt.upper())

class TrcableList(list):
	def append(self, object):
		print("append called")
		super().append(object)



list = TrcableList()
list.append("1")
print(list)
