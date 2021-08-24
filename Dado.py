from Classes.conexao import MsgRequest


def run() -> None:
	bot = MsgRequest()
	
	bot.conectar()


if __name__ == '__main__':
	run()
