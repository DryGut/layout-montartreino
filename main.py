from tkinter import *
from refatorar import *
from dbconfig import *

##### Inicia o App e outras funcionalidades #####

class App():

  def __init__(self, master=None, child=None):
    """inicializa o App"""
    
    self.superior = []
    self.inferior = []
    self.nomedoaluno = []
    
    self.fonte = ("Verdana", "10")
    
    self.master = Frame(master)
    self.master['padx'] = 20
    self.master['pady'] = 10
    self.master.grid()
 
    self.c7 = Frame(master)
    self.c7['pady'] = 15
    self.c7.grid()
    
    
    self.c8 = Frame(master)
    self.c8['pady'] = 15
    self.c8.grid()
 
    self.child = Frame(child)
    self.child['padx'] = 20
    self.child['pady'] = 10
    self.child.grid()

##### Cria o layout do sistema de cadastro #####

  def cadastroAluno(self):
    """Aba Novos Cadastros"""

    self.master.grid()
    self.c7.grid()
    
    self.title = Label(self.master, text='Cadastro de Novos Alunos')
    self.title['pady'] = 10
    self.title['font'] = ('Calibre', '10', 'bold')
    self.title.grid(row=0, column=1)

    self.lblid = Label(self.master, text='Buscar:', font=self.fonte, width=10)
    self.lblid.grid(row=1)
    self.txtid = Entry(self.master)
    self.txtid['width'] = 25
    self.txtid['font'] = self.fonte
    self.txtid.grid(row=1, column=1)

    
    self.lblnome = Label(self.master, text='Nome:', font=self.fonte, width=10)
    self.lblnome.grid(row=2)
    self.txtnome = Entry(self.master)
    self.txtnome['width'] = 25
    self.txtnome['font'] = self.fonte
    self.txtnome.grid(row=2, column=1)

    self.lblidade = Label(self.master, text='Idade:', font=self.fonte, width=10)
    self.lblidade.grid(row=3)
    self.txtidade = Entry(self.master)
    self.txtidade['width'] = 25
    self.txtidade['font'] = self.fonte
    self.txtidade.grid(row=3, column=1)

    self.lblcpf = Label(self.master, text='CPF:', font=self.fonte, width=10)
    self.lblcpf.grid(row=4)
    self.txtcpf = Entry(self.master)
    self.txtcpf['width'] = 25
    self.txtcpf['font'] = self.fonte
    self.txtcpf.grid(row=4, column=1)

    self.lblemail = Label(self.master, text='E-mail:', font=self.fonte, width=10)
    self.lblemail.grid(row=5)
    self.txtemail = Entry(self.master)
    self.txtemail['width'] = 25
    self.txtemail['font'] = self.fonte
    self.txtemail.grid(row=5, column=1)

    self.lblcelular = Label(self.master, text='Celular:', font=self.fonte, width=10)
    self.lblcelular.grid(row=6)
    self.txtcelular = Entry(self.master)
    self.txtcelular['width'] = 25
    self.txtcelular['font'] = self.fonte
    self.txtcelular.grid(row=6, column=1)

    self.lblstatus = Label(self.master, text="")
    self.lblstatus['font'] = 'Verdana', '9', 'italic'
    self.lblstatus.grid(row=7, column=1)
    
##### Bot??es para manipula????o dos cadastros #####
    
    self.btnBuscar = Button(self.c7, text='Buscar', font=self.fonte, width=5)
    self.btnBuscar['command'] = self.localizarCadastro
    self.btnBuscar.grid(column=1, row=7)
    
    self.btnInserir = Button(self.c7, text='Inserir', font=self.fonte, width=5)
    self.btnInserir['command'] = self.fazerCadastro
    self.btnInserir.grid(column=2, row=7)

    self.btnAlterar = Button(self.c7, text='Alterar', font=self.fonte, width=5)
    self.btnAlterar['command'] = self.atualizarCadastro
    self.btnAlterar.grid(column=3, row=7)

    self.btnExcluir = Button(self.c7, text='Excluir', font=self.fonte, fg='red', width=5)
    self.btnExcluir['command'] = self.deletarCadastro
    self.btnExcluir.grid(column=4, row=7)

    self.child.grid_forget()

##### Cria o Layout para montagem dos treinos #####

  def montarTreino(self):
    """Aba Montar Treino"""

    self.child.grid()

    self.lblnomedoaluno = Label(self.child, text='Nome do Aluno:', font=self.fonte, width=15)
    self.lblnomedoaluno.grid(row=0)
    self.txtnomedoaluno = Entry(self.child)
    self.txtnomedoaluno['width'] = 20
    self.txtnomedoaluno['font'] = self.fonte
    self.txtnomedoaluno.grid(row=0, column=1)

    self.btnnomedoaluno = Button(self.child, text='buscar', font=self.fonte, width=5)
    self.btnnomedoaluno['command'] = self.buscarAluno
    self.btnnomedoaluno.grid(row=0, column=3)
    
    self.lblsuperior = Label(self.child, text='Superior:', 
                             font=self.fonte, width=10)
    self.lblsuperior.grid(row=1)
    self.txtsuperior = Entry(self.child)
    self.txtsuperior['width'] = 20
    self.txtsuperior['font'] = self.fonte
    self.txtsuperior.grid(row=1, column=1)

    self.btnsuperior = Button(self.child, text='inserir', 
                              font=self.fonte, width=5)
    self.btnsuperior['command'] = self.montarSuperior
    self.btnsuperior.grid(row=1, column=3)

    
    self.lblinferior = Label(self.child, text='Inferior:', 
                             font=self.fonte, width=10)
    self.lblinferior.grid(row=2)
    self.txtinferior = Entry(self.child)
    self.txtinferior['width'] = 20
    self.txtinferior['font'] = self.fonte
    self.txtinferior.grid(row=2, column=1)
    
    self.btninferior = Button(self.child, text='inserir', 
                              font=self.fonte, width=5)
    self.btninferior['command'] = self.montarInferior
    self.btninferior.grid(row=2, column=3)

    self.btnExibir = Button(self.child, text='Exibir', 
                            font=self.fonte, width=10)
    self.btnExibir['command'] = self.exibirTreino
    self.btnExibir.grid(column=1, row=7)

    
    self.master.grid_forget()
    self.c7.grid_forget()

##### Cria as fun????es para manipula????o dos cadastros #####
    
  def fazerCadastro(self):
    """Realiza o Cadastro"""
    
    c = ClientesDb()

    c.nome = self.txtnome.get()
    c.idade = self.txtidade.get()
    c.cpf = self.txtcpf.get()
    c.email = self.txtemail.get()
    c.celular = self.txtcelular.get()

    self.lblstatus['text'] = c.inserirDados()
    
    self.txtnome.delete(0, END)
    self.txtidade.delete(0, END)
    self.txtcpf.delete(0, END)
    self.txtemail.delete(0, END)
    self.txtcelular.delete(0, END)

  def atualizarCadastro(self):
    """Atualiza o Cadastro"""

    c = ClientesDb()

    c.nome = self.txtnome.get()
    c.idade = self.txtidade.get()
    c.cpf = self.txtcpf.get()
    c.email = self.txtemail.get()
    c.celular = self.txtcelular.get()
    

    self.lblstatus["text"] = c.atualizarDados()

    self.txtnome.delete(0, END)
    self.txtidade.delete(0, END)
    self.txtcpf.delete(0, END)
    self.txtemail.delete(0, END)
    self.txtcelular.delete(0, END)
    
  def deletarCadastro(self):
    """Deleta Registro Existente"""

    c = ClientesDb()

    c.nome = self.txtnome.get()

    self.lblstatus["text"] = c.deletarDados()

    self.txtnome.delete(0, END)
    self.txtidade.delete(0, END)
    self.txtcpf.delete(0, END)
    self.txtemail.delete(0, END)
    self.txtcelular.delete(0, END)

  def localizarCadastro(self):
    
    c = ClientesDb()

    id = self.txtid.get()

    self.lblstatus["text"] = c.localizarDados(id)

    self.txtid.delete(0, END)
    self.txtid.insert(INSERT, c.id)
    
    self.txtnome.delete(0, END)
    self.txtnome.insert(INSERT, c.nome)

    self.txtidade.delete(0, END)
    self.txtidade.insert(INSERT,c.idade)

    self.txtcpf.delete(0, END)
    self.txtcpf.insert(INSERT, c.cpf)

    self.txtemail.delete(0, END)
    self.txtemail.insert(INSERT, c.email)

    self.txtcelular.delete(0, END)
    self.txtcelular.insert(INSERT,c.celular)

##### Funcoes para exibi????o dos treinos #####
    
  def montarInferior(self):
    """montagem do treino"""

    inserir = True
    while inserir:
      i = self.txtinferior.get()
      self.inferior.append(i)
      self.txtinferior.delete(0, END)
      inserir = False
  
  def montarSuperior(self):
    """montagem do treino"""

    inserir = True
    while inserir:
      s = self.txtsuperior.get()
      self.superior.append(s)
      self.txtsuperior.delete(0, END)
      inserir = False

  def exibirTreino(self):
    """exibir o treino"""
    
    c = ClientesDb()
    
    top = Toplevel()
    top.title('Treino do Dia')
    top.geometry('250x250')
    
    for i in self.nomedoaluno:
      if i in c.novo_cadastro(i):
        print(c.novo_cadastro(i))
    
    label1 = Label(top, text="-" * 30 + "\nSuperior:\n")
    label1.grid(row=1, column=2)
    
    for item in self.superior:
      label2 = Label(top, text=item)
      label2.grid(row=2, column=2)

    label3 = Label(top, text="-" * 30 + "\nInferior:\n")
    label3.grid(row=3, column=2)
    
    for item in self.inferior:
      label4 = Label(top, text=item)
      label4.grid(row=4, column=2)
    
    label5 = Label(top, text="-" * 30)
    label5.grid(row=5, column=2)

  def buscarAluno(self):
    """formatar treino com nome do aluno"""

    n = self.txtnomedoaluno.get()
    self.nomedoaluno.append(n)
    self.txtnomedoaluno.delete(0, END)

##### Pagina inicial do App #####

root = Tk()
app = App(root)
root.title("Personal Trainer App")
root.geometry('450x290')

##### Cria o menu de navega????o do Sistema #####

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Novo Cadastro', command=app.cadastroAluno)
filemenu.add_command(label='Montar Treino', command=app.montarTreino)

filemenu.add_separator()
filemenu.add_command(label='Sair', command=root.quit)

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')


root.mainloop()