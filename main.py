from tkinter import *
from refatorar import *
from dbconfig import *

root = Tk()
root.title("Personal Trainer App")
root.geometry('320x200')



e1 = Label(root, text="Nome:").grid(row=0)
e2 = Label(root, text="Idade:").grid(row=1)
e3 = Label(root, text="Cpf:").grid(row=2)
e4 = Label(root, text="E-mail:").grid(row=3)
e5 = Label(root, text="Celular:").grid(row=4)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
  
def clicked():
  
  banco = Connect()

  c = banco.conn.cursor()
  c.execute("""
            INSERT INTO alunos VALUES(
            :nome, 
            :idade, 
            :cpf, 
            :email, 
            :celular)
            """,
            {
              'nome': e1.get(),
              'idade': e2.get(),
              'cpf': e3.get(),
              'email': e4.get(),
              'celular': e5.get()
            })
          
  banco.conn.commit()
  c.close()
  
  
  e1.delete(0,"end")
  e2.delete(0,"end")
  e3.delete(0,"end")
  e4.delete(0,"end")
  e5.delete(0,"end")

btn = Button(root, text="Cadastrar", command=clicked)
btn.grid(column=1, row=5)


def montarTreino():
  
  f1 = Label(root, text="Superior:").grid(row=0)
  f2 = Label(root, text="Inferior:").grid(row=1)


  f1 = Entry(root)
  f2 = Entry(root)


  f1.grid(row=0, column=1)
  f2.grid(row=1, column=1)


menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Novo Cadastro')
filemenu.add_separator()
filemenu.add_command(label='Montar Treino', command=montarTreino)
filemenu.add_separator()
filemenu.add_command(label='Sair', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

root.mainloop()
