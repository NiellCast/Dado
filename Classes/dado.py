from random import randint


class Dado:
	def __init__(self) -> None:
		self.valor_minimo = 1
		self.valor_maximo = 6
	
	def sortear(self) -> int:
		"""
		:return: Retorna um número aleatório de 1 a 6.
		"""
		
		return randint(self.valor_minimo, self.valor_maximo)
