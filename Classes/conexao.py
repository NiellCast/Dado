from os import getenv
from telepot import Bot
from time import sleep
from dotenv import load_dotenv
from Classes.mensagens import Gerenciamento
from Classes.enviar_mensagem import Envio
from src.gerador_de_numeros.dado import Dado


class MsgRequest:
	load_dotenv()
	
	def __init__(self) -> None:
		self.__bot = Bot(getenv('TOKEN'))
		self.__gerenciamento = Gerenciamento()
		self.__mensagem = Envio()
		self.num = Dado()
		
	def mensagens(self, msg: int or slice) -> None:
		"""
		:param msg: Recebe o que o usuário digitou e se a mensagem estiver entre as esperadas, sorteia um número.
		:return: Envia uuma imagem com o número sorteado para o usuário.
		"""
		
		id_do_usuario = msg['from']['id']  # Guarda o ID do usuário que está utilizando o Bot.
		
		if not msg['from']['is_bot']:  # Verifica se o usuário não é um robô.
			if self.__gerenciamento.validar(msg['text'].upper()):
				self.__mensagem.enviar_texto(id_do_usuario, self.__gerenciamento.mensagens(0))
				self.__mensagem.enviar_photo(id_do_usuario, self.num.sortear_numero())
				sleep(0.5)
				self.__mensagem.enviar_texto(id_do_usuario, self.__gerenciamento.mensagens(1))
			
			else:
				self.__mensagem.enviar_dica(id_do_usuario)
			
	def conectar(self) -> None:
		"""
		:return: Mantém a conexão com o telegram sem interrupções.
		"""
		self.__bot.message_loop(self.mensagens)
		while True:
			pass
