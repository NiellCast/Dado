from src.telegram_bot.bot import Bot
from dotenv import load_dotenv
from os import getenv
from src.gerador_de_numeros.dado import Dado


def run() -> None:
	"""
	:return: inicia o bot.
	"""

	load_dotenv()
	bot = Bot()

	@bot.message_handler(commands=[getenv('COMANDO_ADM')])
	def responder_adm(mensagem) -> None:
		"""
		:param mensagem: Recebe a mensagem enviada pelo aplicativo.
		:return: Retorna o histórico de quem (nome de usuário) usou o bot.
		"""
		print(mensagem.from_user.username)

	@bot.message_handler(commands=['start', 'jogar'])
	def responder_usuario(mensagem) -> None:
		imagem = Dado.sortear_numero()

		bot.send_photo(mensagem.chat.id, open(f'imagens/numero_{imagem}.png', 'rb'))

	bot.polling()


if __name__ == '__main__':
	run()
