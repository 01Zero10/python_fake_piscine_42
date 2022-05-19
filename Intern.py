class Intern():
	def __init__(self, str="My name? I’m nobody, an intern, I have no name."):
		self.Name = str
	def __str__(self):
		return self.Name
	class Coffe():
		def __str__(self) -> str:
			return "This is the worst coffee you evertasted."
	def work(self):
		raise Exception("I’m just an intern, I can’t do that...")
	def make_coffee(self):
		return self.Coffe()

def main():
	a = Intern()
	b = Intern("Mark")

	print(a)
	print(b)

	print(b.make_coffee())
	try:
		a.work()
	except Exception as e:
		print(e)

if __name__ == "__main__":
	main()

