from dbconfig import Connect

class ClientesDb(object):

  def __init__(self, id = 0, nome = "", idade = "", cpf = "", email = "", celular = ""):

    self.info = {}
    self.id = id
    self.nome = nome
    self.idade = idade
    self.cpf = cpf
    self.email = email
    self.celular = celular
    

  def inserirDados(self):
        """inserindo dados dos alunos"""

        banco = Connect()
        try:
          c = banco.conn.cursor()
          c.execute("INSERT INTO alunos (nome, idade, cpf, email, celular) VALUES ('" + self.nome + "', '" + self.idade + "', '" + self.cpf + "', '" + self.email + "', '" + self.celular + "')")
          
          banco.conn.commit()
          c.close()
          
          return "Cliente Cadastrado com Sucesso"
        except:
          return "Cliente ja Cadastrado"


  def atualizarDados(self):
    """atualiza os dados dos alunos cadastrados"""

    banco = Connect()
    try:
      c = banco.conn.cursor()
      c.execute("UPDATE alunos SET nome = '" + self.nome + "', idade = '" + self.idade + "', email = '" + self.email + "', celular = '" + self.celular + "' WHERE id = " + self.id + " ")
      banco.conn.commit()
      c.close()

      return "Cadastro Atualizado com Sucesso"
    except:
      return "Atualizacao nao Realizada"


  def deletarDados(self):
    """deleta os dados existentes"""

    banco = Connect()
    try:
      c = banco.conn.cursor()
      c.execute("DELETE FROM alunos WHERE id = " + self.id + " ")
      banco.conn.commit()
      c.close()

      return "Cadastro removido com Sucesso"
    except:
      return "Remocao nao Realizada"

  def localizarDados(self, id):
    """ buscando dados no BD"""
    
    banco = Connect()
    try:
      c = banco.conn.cursor()
      c.execute("SELECT * FROM alunos WHERE id = " + id + " ")

      for linha in c:
        self.id = linha[0]
        self.nome = linha[1]
        self.idade = linha[2]
        self.cpf = linha[3]
        self.email = linha[4]
        self.celular = linha[5]
      banco.conn.commit()
      c.close()

      return "Busca Realizada"
    except:
      return "Cliente nao Encontrado"

  def novo_cadastro(self, nome):
    """localiza cadastro"""
    
    banco = Connect()
    try:
      n = banco.conn.cursor()
      n.execute("SELECT * FROM alunos WHERE nome = " + nome + " ")
      banco.conn.commit()
      n.close()
      return list(n.fetchone())
    except:
      return "deu merda"