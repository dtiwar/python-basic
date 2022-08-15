from abc import ABC, abstractmethod


class InvalidOperation(Exception):
	pass


class Stream(ABC):
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

	@abstractmethod
	def read(self):
		pass


class FileStream(Stream):
	def read(self):
		print("reading data from file")


class NetworkStream(Stream):
	def read(self):
		print("reading data from network")

class MemoryTream(Stream):
	def read(self):
		pass



stream = MemoryTream()

