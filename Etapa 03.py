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

# ETAPA 3 - Adicionar funções para adicionar tarefas - Parte 1

frame_em_edicao = None

def adicionar_tarefa():
    global frame_em_edicao
    tarefa = entrada_tarefa.get().strip()
    if tarefa and tarefa != "Escreva sua tarefa aqui":
        if frame_em_edicao is not None:
            atualizar_tarefa(tarefa)
            frame_em_edicao = None
        else:
            adicionar_item_tarefa(tarefa)
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Inválida", "Por favor, insira uma tarefa válida.")

def adicionar_item_tarefa(tarefa):
    frame_tarefa = tk.Frame(canvas_interior, bg="white", bd=1, relief=tk.SOLID)

    label_tarefa = tk.Label(frame_tarefa, text=tarefa, font=("Garamond", 16), bg="white", width=25, height=2, anchor="w")
    label_tarefa.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=5)

    botao_editar = tk.Button(frame_tarefa, image=icon_editar, command=lambda f=frame_tarefa, l=label_tarefa: preparar_edicao(f, l), bg="white", relief=tk.FLAT)
    botao_editar.pack(side=tk.RIGHT, padx=5)

    botao_deletar = tk.Button(frame_tarefa, image=icon_deletar, command=lambda f=frame_tarefa: deletar_tarefa(f), bg="white", relief=tk.FLAT)
    botao_deletar.pack(side=tk.RIGHT, padx=5)

    frame_tarefa.pack(fill=tk.X, padx=5, pady=5)

    checkbutton = ttk.Checkbutton(frame_tarefa, command=lambda label=label_tarefa: alternar_sublinhado(label))
    checkbutton.pack(side=tk.RIGHT, padx=5)

    canvas_interior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# Carregar ícones (assegure-se que os arquivos estão na mesma pasta que o script)
icon_editar = PhotoImage(file="edit.png").subsample(20, 20)  # Ajuste conforme necessário
icon_deletar = PhotoImage(file="delete.png").subsample(20, 20)  # Ajuste conforme necessário
''' Precisa adicionar a função adicionar tarefa no botao_adicionar (..., command = adicionar_tarefa)'''    

# FIM da ETAPA 3 - Adicionar funções para adicionar tarefas - Parte 1

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
botao_adicionar = tk.Button(frame, command=adicionar_tarefa ,text="Adicionar Tarefa", bg="#4CAF50", fg="white", height=1, width=15, font=("Roboto", 11), relief=tk.FLAT)
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