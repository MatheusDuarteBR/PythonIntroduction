
# Tkinter module
import random
import pyperclip
from tkinter import *
from tkinter.ttk import *
 
def low():
    entry.delete(0, END)
 
    length = var1.get()
 
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""
 
    # força selecionada baixa
    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password
 
    # força selecionada media
    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password
 
    # força selecionada forte
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    else:
        print("Por favor selecione uma opção")
 
 
# função que gera a senha
def generate():
    password1 = low()
    entry.insert(10, password1)
 

def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)
 
 
# Main Function
 
# janela GUI
root = Tk()
var = IntVar()
var1 = IntVar()
 
# Título do GUI
root.title("Gerador de Senha")
 
# senha gerada
Random_password = Label(root, text="Senha ")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)
 
c_label = Label(root, text="Tamanho ")
c_label.grid(row=1)
 
# cria o botão copiar
# gera a pasta e copia 
copy_button = Button(root, text="Copy", command=copy1)
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3)
 
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')
combo = Combobox(root, textvariable=var1)
 
# Tamanhos de senha 
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)
 
# Start no GUI
root.mainloop()