import tkinter as tk
from tkinter import colorchooser

class Application(tk.Frame):
    def __init__(janela,master=None, title="My Application"):
        super().__init__(master)
        janela.master = master
        janela.master.title(title)
        janela.pack()
        janela.widget1()

    def widget1(janela):
        janela.bem_vindo = tk.Button(janela)
        janela.bem_vindo["text"] = "Bem-Vindo!\n(clique aqui)"
        janela.bem_vindo["font"] = ("Times New Roman", "16", "italic", "bold")
        janela.bem_vindo["command"] = janela.prova
        janela.bem_vindo.pack(side="top")

        janela.color_button = tk.Button(janela)
        janela.color_button["text"] = "Escolher Cor"
        janela.color_button["font"] = ("Times New Roman", "16", "italic", "bold")
        janela.color_button["command"] = janela.mudar_cor
        janela.color_button.pack(side="top")

        janela.sair = tk.Button(janela, text="SAIR", fg="red", command=janela.master.destroy)
        janela.sair["font"] = ("Times New Roman", "12", "italic", "bold")
        janela.sair["width"] = 20
        janela.sair["height"] = 3
        janela.sair.pack(side="bottom")

    def prova(janela):
        print("Olá!")

    def mudar_cor(janela):
        cor = colorchooser.askcolor(title="Escolher Cor")
        if cor[1] is not None:
            janela.bem_vindo.configure(fg=cor[1])
            janela.color_button.configure(fg=cor[1])
            janela.sair.configure(fg=cor[1])


root = tk.Tk()
app = Application(master=root, title="Hi!")
app.mainloop()










