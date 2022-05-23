from importlib.util import set_loader
from mimetypes import init
from re import T


class HotBeverage():
	def __init__(self, p = 0.30, n = "hot beverage"):
		self.price = p
		self.name = n
	def description(self, st="Just some hot water in a cup"):
		return st
	def __str__(self) -> str:
		return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}"


class Coffe(HotBeverage):
	def __init__(self):
		super().__init__(0.40, "coffee")
	def description(self):
		return super().description("A coffee, to stay awake.")


class Tea(HotBeverage):
	def __init__(self):
		super().__init__(n="tea")


class Chocolate(HotBeverage):
	def __init__(self):
		super().__init__(0.50, "chocolate")
	def description(self):
		return super().description("Chocolate, sweet chocolate...")


class Cappuccino(HotBeverage):
	def __init__(self):
		super().__init__(0.45, "cappuccino")
	def description(self):
		return super().description("Un po' di Italia nella sua tazza!")
	

def main():
	a = HotBeverage()
	b = Coffe()
	c = Tea()
	d = Chocolate()
	e = Cappuccino()

	print(a)
	print(b)
	print(c)
	print(d)
	print(e)

def func(a, b, c ,d=True):
	print (a, b, c, d)

if __name__ == "__main__":
	main()
