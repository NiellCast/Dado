class Gerenciamento:
	def __init__(self) -> None:
		self.__mensagens_validas = ['J', '/START']
		self.__mensagens_padroes = ['Jogando o dado...', 'Envie "J" para jogar de novo!']
		
	def validar(self, msg: str) -> bool:
		return True if msg in self.__mensagens_validas else False
	
	def mensagens(self, x: int) -> str:
		return self.__mensagens_padroes[x]
