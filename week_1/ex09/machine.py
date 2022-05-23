from beverages import HotBeverage, Coffe, Tea, Chocolate, Cappuccino 
import random


class CoffeMachine:
	def __init__(self):
		self.damage = 0
	class EmptyCup(HotBeverage):
		def __init__(self, p=0.90, n="empty cup"):
			super().__init__(p, n)
		def description(self, st="An emptycup?! Gimme my money back!"):
			return super().description(st)
	class BrokenMachineExcpeion(Exception):
		def __init__(self, *args) -> None:
			super().__init__(*args)
	def repair(self):
		self.damage = 0
	def serve(self, beverage):
		if not isinstance(beverage, HotBeverage):
			raise ValueError()
		if self.damage < 10:
			if random.choice([0, 1]) == 1:
				self.damage += 1
				return type(beverage)()
			else:
				self.damage += 1
				return self.EmptyCup()
		else:
			raise BrokenPipeError("This coffee machine has to be repaired.")
		

def main():
	l = [Coffe(), Tea(), Chocolate(), Cappuccino()]
	a = CoffeMachine()
	for i in range(0, 22):
		try:
			print(a.serve(random.choice(l)).description())
		except Exception as e:
			print(e)
			a.repair()


if __name__ == "__main__":
	main()