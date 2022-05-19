from beverages import HotBeverage

class CoffeMachine:
	def __init__(self):
		class EmptyCup(HotBeverage):
			def __init__(self, p=0.90, n="An emptycup?! Gimme my money back!"):
				super().__init__(p, n)