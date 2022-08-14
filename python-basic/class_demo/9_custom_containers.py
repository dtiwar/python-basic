class TagCloud:
	def __init__(self):
		self.tags = {}

	def add(self, tag):
		self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

	def __getitem__(self, item: str):
		return self.tags.get(item.lower(), 0)

	def __getitem__(self, item: str):
		return self.tags.get(item.lower(), 0)

	def __len__(self):
		return len(self.tags)


cloud = TagCloud()
# cloud["python"]=10
cloud.add("python")
cloud.add("python")
cloud.add("python")
cloud.add("python")
cloud.add("Python")

len(cloud)
print(cloud.tags)
print(cloud["python"])
