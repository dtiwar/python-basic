# class Product:
# 	def __init__(self,__price):
# 		self.set_price(__price)
# 	def get_price(self):
# 		return self.__price
# 	def set_price(self,value):
# 		if value < 0:
# 			raise ValueError("__price can't be negative")
# 		self.__price=value

# product = Product(50)

# class Product:
# 	def __init__(self,__price):
# 		self.set_price(__price)
# 	def get_price(self):
# 		return self.__price
# 	def set_price(self,value):
# 		if value < 0:
# 			raise ValueError("__price can't be negative")
# 		self.__price=value
#
#
# product = Product(10)
# print(product.get_price())

# class Product:
# 	def __init__(self, price):
# 		self.__price = price
#
#
# 	def get_price(self):
# 		return self.__price
#
# 	def set_price(self, value):
# 		if value < 0:
# 			raise ValueError("price can't be negative")
#
# 	price = property(fget=get_price, fset=set_price)
#
# product = Product(50)

# final and better solution

# This is how we do getter and setters
# class Product:
# 	def __init__(self, price):
# 		self.price = price
# 	@property
# 	def price(self):
# 		return self.__price
# 	@price.setter
# 	def price(self, value):
# 		if value < 0:
# 			raise ValueError("price can't be negative")
# 		self.price=value
#
# product = Product(1)

class Point:
	def __init__(self,x):
		self.x=x
	@property
	def x(self):
		print("getter function has been cllaed")
		return self.__x
	@x.setter
	def x(self,value):
		print("the setter function has been called")
		self.__x=value

point = Point(10)
print("----")
print(point.x)
