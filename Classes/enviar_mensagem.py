from os import getenv
from telepot import Bot
from time import sleep
from dotenv import load_dotenv


class Envio:
	load_dotenv()
	
	def __init__(self) -> None:
		self.__bot = Bot(getenv('TOKEN'))
		
	def enviar_texto(self, id_do_usuario: str, mensagem: str) -> None:
		self.__bot.sendMessage(id_do_usuario, mensagem)
		sleep(0.5)

	def enviar_photo(self, id_do_usuario: str, id_da_photo: int) -> None:
		self.__bot.sendPhoto(id_do_usuario, photo=open(f'imagens/numero_{id_da_photo}.png', 'rb'))
		sleep(0.5)
	
	def enviar_dica(self, id_do_usuario: str):
		self.__bot.sendMessage(id_do_usuario, 'Envie "J" para jogar o dado!')
		sleep(0.5)
