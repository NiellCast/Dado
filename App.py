from Classes.conexao import MsgRequest


def run() -> None:
	"""
	:return: inicia o bot.
	"""
	
	bot = MsgRequest()
	
	bot.conectar()


if __name__ == '__main__':
	run()

