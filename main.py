from tkinter import *
from refatorar import *
from dbconfig import *

# inicia o App e outras funcionalidades

class App():

  def __init__(self, master=None, slave=None):
    """inicializa o App"""

   
    self.fonte = ("Verdana", "10")
    
    self.master = Frame(master)
    self.master['padx'] = 20
    self.master['pady'] = 10
    self.master.grid()
    
    self.c8 = Frame(master)
    self.c8['pady'] = 15
    self.c8.grid()
    
    self.lblstatus = Label(self.c8, text="")
    self.lblstatus['font'] = 'Verdana', '9', 'italic'
    self.lblstatus.grid(row=7)
    
    self.slave = Frame(slave)
    self.slave['padx'] = 20
    self.slave['pady'] = 5
    self.slave.grid()

    

  def cadastroAluno(self):
    """Aba Novos Cadastros"""
    
    self.master.grid()
    
    self.title = Label(self.master, text='Cadastro de Novos Alunos')
    self.title['font'] = ('Calibre', '10', 'bold')
    self.title.grid(row=0, column=1)

    self.lblnome = Label(self.master, text='Nome:', font=self.fonte, width=10)
    self.lblnome.grid(row=1)
    self.txtnome = Entry(self.master)
    self.txtnome['width'] = 25
    self.txtnome['font'] = self.fonte
    self.txtnome.grid(row=1, column=1)

    self.lblidade = Label(self.master, text='Idade:', font=self.fonte, width=10)
    self.lblidade.grid(row=2)
    self.txtidade = Entry(self.master)
    self.txtidade['width'] = 25
    self.txtidade['font'] = self.fonte
    self.txtidade.grid(row=2, column=1)

    self.lblcpf = Label(self.master, text='CPF:', font=self.fonte, width=10)
    self.lblcpf.grid(row=3)
    self.txtcpf = Entry(self.master)
    self.txtcpf['width'] = 25
    self.txtcpf['font'] = self.fonte
    self.txtcpf.grid(row=3, column=1)

    self.lblemail = Label(self.master, text='E-mail:', font=self.fonte, width=10)
    self.lblemail.grid(row=4)
    self.txtemail = Entry(self.master)
    self.txtemail['width'] = 25
    self.txtemail['font'] = self.fonte
    self.txtemail.grid(row=4, column=1)

    self.lblcelular = Label(self.master, text='Celular:', font=self.fonte, width=10)
    self.lblcelular.grid(row=5)
    self.txtcelular = Entry(self.master)
    self.txtcelular['width'] = 25
    self.txtcelular['font'] = self.fonte
    self.txtcelular.grid(row=5, column=1)

    self.bntInserir = Button(self.master, text='Inserir', font=self.fonte, width=5)
    self.bntInserir['command'] = self.fazerCadastro
    self.bntInserir.grid(column=1, row=6)

    self.btnAlterar = Button(self.master, text='Alterar', font=self.fonte, width=5)
    self.btnAlterar['command'] = self.atualizarCadastro
    self.btnAlterar.grid(column=2, row=6)

    self.btnExcluir = Button(self.master, text='Excluir', font=self.fonte, width=5)
    self.btnExcluir['command'] = self.deletarCadastro
    self.btnExcluir.grid(column=3, row=6)

    self.slave.grid_forget()

  def montarTreino(self):
    """Aba Montar Treino"""

    self.slave.grid()
    
    self.lblsuperior = Label(self.slave, text='Superior:', font=self.fonte, width=10)
    self.lblsuperior.grid(row=0)
    self.txtsuperior = Entry(self.slave)
    self.txtsuperior['width'] = 25
    self.txtsuperior['font'] = self.fonte
    self.txtsuperior.grid(row=0, column=1)

    self.lblinferior = Label(self.slave, text='Inferior:', font=self.fonte, width=10)
    self.lblinferior.grid(row=1)
    self.txtinferior = Entry(self.slave)
    self.txtinferior['width'] = 25
    self.txtinferior['font'] = self.fonte
    self.txtinferior.grid(row=1, column=1)
    
    self.master.grid_forget()

  def fazerCadastro(self):

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

    c = ClientesDb()

    c.nome = self.txtnome.get()

    self.lblstatus["text"] = c.deletarDados()

    self.txtnome.delete(0, END)
    self.txtidade.delete(0, END)
    self.txtcpf.delete(0, END)
    self.txtemail.delete(0, END)
    self.txtcelular.delete(0, END)
    
    
root = Tk()
app = App(root)
root.title("Personal Trainer App")
root.geometry('520x300')

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