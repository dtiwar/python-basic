class InvalidOperation(Exception):
	pass


class Stream:
	def open(self):
		if self.opened:
			raise InvalidOperation("The Operation is not valid")
		self.opened = True

	def close(self):
		if not self.opened:
			raise InvalidOperation("The Operation is not valid")
		self.opened = False

	def __init__(self):
		self.opened = False


class FileStream(Stream):
	def read(self):
		print("reading data from file")


class NetworkStream(Stream)
	def read(self):
		print("reading data from network")
