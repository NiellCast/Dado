from sqlite3 import connect
from dotenv import load_dotenv
from os import getenv
from typing import List


class Conector:
    load_dotenv()

    def __init__(self) -> None:
        self.__conexao = connect(getenv("DATABASE_NAME"), check_same_thread=False)
        self.__cursor = self.__conexao.cursor()

    def create(self, username: str) -> None:
        with self.__conexao:
            self.__cursor.execute(
                f'INSERT INTO {getenv("TABLE")} ({getenv("COLUMN")}) VALUES (?)',
                (username,)

            )
            self.__conexao.commit()

    def read(self) -> List:
        with self.__conexao:
            self.__cursor.execute(
                f'SELECT * FROM {getenv("TABLE")}'
            )

            return self.__cursor.fetchall()
