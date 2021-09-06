class Gerenciamento:
	def __init__(self) -> None:
		self.__mensagens_validas = ['J', '/START']
		self.__mensagens_padroes = ['Jogando o dado...', 'Envie "J" para jogar de novo!']
		
	def validar(self, msg: str) -> bool:
		"""
		:param msg: Recebe a mensagem enviada pelo usuário.
		:return: retorna True se a mensagens se encontra na lista de mensagens válidas para resposta.
		"""
		
		return True if msg in self.__mensagens_validas else False
	
	def mensagens(self, x: int) -> str:
		"""
		:param x: índice para buscar uma mensagem na lista de mensagens padrões.
		:return: retorna a mensagem da lista requisitada com o índice X indicado.
		"""
		
		return self.__mensagens_padroes[x]
