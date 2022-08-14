class TagCloud:
	def __init__(self):
		self.__tags = {}
	# 	Tag is now private member of the class using __{attribute_name}

	def add(self, tag):
		self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

	def __getitem__(self, item: str):
		return self.__tags.get(item.lower(), 0)

	def __getitem__(self, item: str):
		return self.__tags.get(item.lower(), 0)

	def __len__(self):
		return len(self.__tags)


cloud = TagCloud()

cloud.add("python")
cloud.add("python")
cloud.add("Python")

# print(cloud.tag["python"])

# get the private members of the class

print(cloud.__dict__)
print(cloud._TagCloud__tags)