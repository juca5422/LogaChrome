import tkinter as tk
from tkinter import messagebox
import funcoes as fc

# Função chamada quando uma opção é selecionada
def selecionar_opcao():
    opcao = lista_opcoes.get(tk.ANCHOR)
    if opcao:
        perfil = fc.ListaPerfilsChrome()[opcao]["perfil"]
        messagebox.showinfo("Opção Selecionada", f"Você selecionou: {perfil}")
    else:
        messagebox.showwarning("Seleção", "Nenhuma opção foi selecionada.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Menu de Opções")
janela.geometry("300x200")

# Criar o rótulo (label)
rotulo = tk.Label(janela, text="Selecione uma opção:")
rotulo.pack(pady=10)

# Criar a lista de opções
opcoes = fc.ListaPerfilsChrome()

# Criar o Listbox
lista_opcoes = tk.Listbox(janela, selectmode=tk.SINGLE, height=len(opcoes))
for opcao in opcoes:
    lista_opcoes.insert(tk.END, opcao)
lista_opcoes.pack(pady=10)

# Criar o botão para confirmar a seleção
botao_selecionar = tk.Button(janela, text="Selecionar", command=selecionar_opcao)
botao_selecionar.pack(pady=10)

# Iniciar o loop da interface
janela.mainloop()