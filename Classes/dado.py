from random import randint


class Dado:
	def __init__(self) -> None:
		self.valor_minimo = 1
		self.valor_maximo = 6
	
	def sortear(self) -> int:
		return randint(self.valor_minimo, self.valor_maximo)
