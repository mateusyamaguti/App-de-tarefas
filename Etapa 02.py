# Aqui é feito o import da biblioteca inteira
import tkinter as tk
# Aqui é feito i import apenas dos métodos que desejo usar
# messagebox é importante para dar retorno de mensagens na tela
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage

# Criar janela
janela = tk.Tk()
'''Título'''
janela.title("Meu app de tarefas")
'''Cor de fundo'''
janela.config(bg = '#F0F0F0')
'''Dimensões da janela'''
janela.geometry("600x800")

# Criar cabeçalho do aplicativo
fonte_cabecalho = font.Font(family="Garamond", size=24, weight="bold")
'''Criar o rótulo do cabeçalho, onde ele vai ficar'''
rotulo_cabecalho = tk.Label(janela, text="Meu app de tarefa", font=fonte_cabecalho, bg="#F0F0F0", fg="#333").pack(pady=20)

# Criar um frame que será o campo de entrada
frame = tk.Frame(janela, bg="#F0F0F0")
frame.pack(padx=10)
'''Criar local de entrada dentro do frame'''
entrada_tarefa = tk.Entry(frame, font=("Garamound", 14), relief=tk.FLAT, bg="white", fg="gray", width=30)
'''Posicionar o campo de tarefa'''
entrada_tarefa.pack(side=tk.LEFT, padx=10)

# Criar botão de entrada
botao_adicionar = tk.Button(frame, text="Adicionar Tarefa", bg="#4CAF50", fg="white", height=1, width=15, font=("Roboto", 11), relief=tk.FLAT)
botao_adicionar.pack(side=tk.LEFT, padx=10)
# FIM ETAPA 1

# COMEÇO ETAPA 2
# Criar um frame para lista de tarefas com rolagem (scroll)
frame_lista_tarefas = tk.Frame(janela, bg="white")
frame_lista_tarefas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
'''Criar canvas de tarefas'''
canvas = tk.Canvas(frame_lista_tarefas, bg="white")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
'''Criar scrollbar'''
scrollbar = ttk.Scrollbar(frame_lista_tarefas, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
'''Configurar o scrollbar para que ele possa aparecer com melhor aparência'''
canvas.configure(yscrollcommand=scrollbar.set)

# Criar um canvas que será a parte interior do canvas principal que receberá as tarefas
canvas_interior = tk.Frame(canvas, bg="white")
'''Configurar janela para que o scrollbar funcione melhor'''
canvas.create_window((0, 0), window=canvas_interior, anchor="nw")
canvas_interior.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
# FIM DA ETAPA 2




# Executar aplicativo
janela.mainloop()