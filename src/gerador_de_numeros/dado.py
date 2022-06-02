from random import randint


class Dado:
	@staticmethod
	def sortear_numero() -> int:
		"""
		:return: Retorna um número de 1 a 6.
		"""
		
		return randint(1, 6)
