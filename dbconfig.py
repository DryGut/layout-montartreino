import sqlite3
import os
import io
import datetime


class Connect():
  """cria a conexao com o banco de dados"""
    
  def __init__(self):
    #conectando...
    self.conn = sqlite3.connect('clientes.db')
    self.createTable()


  def createTable(self):
    """ Criando a tabela """
      
    c = self.conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS alunos (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
	            nome TEXT,
	            idade INTEGER,
	            cpf	VARCHAR(11),
	            email TEXT,
	            celular TEXT
             )""")
    self.conn.commit()
    c.close()
      