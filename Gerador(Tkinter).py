import string
import secrets
import tkinter as tk
from tkinter import messagebox


#Função para gerar a senha, definir o tamanho, letras, numeros e caracteres
def gerar_senha(entry_tamanho, var_letra, var_numeros, var_caracteres, entry_resultado):
    try:
        tamanho = int(entry_tamanho.get())
        letra = var_letra.get()
        num = var_numeros.get()
        caracteres = var_caracteres.get()

        senha = ''
        senha_final = ''

        if letra == 1:
            senha += string.ascii_letters
        if num == 1:
            senha += string.digits
        if caracteres == 1:
            senha += string.punctuation


        if not senha:
            messagebox.showwarning('Aviso', 'Por favor, escolha ao menos uma das opções acima.')
            return
        
        for _ in range(tamanho):
            senha_final += secrets.choice(senha)

        senha_lista = list(senha_final)
        secrets.SystemRandom().shuffle(senha_lista)
        senha_final = ''.join(senha_lista)

        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, senha_final)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico.")

#Função para copiar a senha
def copiar_senha(root, entry_resultado):
    senha = entry_resultado.get()

    if senha:
        root.clipboard_clear()
        root.clipboard_append(senha)
        messagebox.showinfo("Senha Copiada", "Senha copiada para a área de transferência!")
    else:
        messagebox.showwarning("Aviso", "Senha não identificada!")
    

#Função para criar a interface
def criar_interface():
    root = tk.Tk()
    root.title("Gerador de Senhas Seguras")
    
    root.geometry("450x450")
    root.resizable(False, False)
    root.configure(bg="black")

    tema_atual = tk.StringVar(value = "dark")
    def alternar_tema():
        if tema_atual.get() == "dark":
            root.configure(bg="white")
            label_tamanho.configure(bg="white", fg="black")
            label_title.configure(bg="white", fg="black")
            label_resultado.configure(bg="white", fg="black")
            botao_tema.configure(text="Tema Escuro", bg="black", fg="white")
            botao_senha.configure(bg="white", fg="black")
            botao_copiar.configure(bg="white", fg="black")
            botao_mostrar.configure(bg="white", fg="black")
            check_letras.configure(bg="white", fg="black", selectcolor="white", activebackground="white")
            check_numeros.configure(bg="white", fg="black", selectcolor="white", activebackground="white")
            check_caracteres.configure(bg="white", fg="black", selectcolor="white", activebackground="white")
            frame_senha.configure(bg="white")
            tema_atual.set("light")
        else:
            root.configure(bg="black")
            label_tamanho.configure(bg="black", fg="white")
            label_title.configure(bg= "black", fg="white")
            label_resultado.configure(bg="black", fg="white")
            botao_tema.configure(text="Tema Claro", bg="white", fg="black")
            botao_senha.configure(bg="black", fg="white")
            botao_copiar.configure(bg="black", fg="white")
            botao_mostrar.configure(bg="black", fg="white")
            check_letras.configure(bg="black", fg="white", selectcolor="black", activebackground="black")
            check_numeros.configure(bg="black", fg="white", selectcolor="black", activebackground="black")
            check_caracteres.configure(bg="black", fg="white", selectcolor="black", activebackground="black")
            frame_senha.configure(bg="black")
            tema_atual.set("dark")
        

    #----Panel Titulo----#
    label_title = tk.Label(root, text="Gerador de Senhas Seguras", bg="black", fg="white", font= ("serif bold italic", 15, "bold")) 
    label_title.pack(pady=4)    


    #----Panel Tamanho----#
    label_tamanho = tk.Label(root, text="Qual o tamanho da senha?", bg="black", fg="white", font= ("serif bold italic", 10, "bold"))
    label_tamanho.pack(pady=4, padx=10)

    entry_tamanho = tk.Entry(root, justify="center")    
    entry_tamanho.pack()

    #----Variaveis Checkbox----#
    var_letra = tk.IntVar()
    var_numeros = tk.IntVar()
    var_caracteres = tk.IntVar()

    #----Checkbox Letras----#
    check_letras = tk.Checkbutton(
    root,
    text="Letras",
    variable=var_letra,
    bg="black",
    fg="white",
    selectcolor="black",
    activebackground="black",
    )
    check_letras.pack(pady=3)
    
    #----Checkbox Numeros----#
    check_numeros = tk.Checkbutton(
    root,
    text="Números",
    variable=var_numeros,
    bg="black",
    fg="white",
    selectcolor="black",
    activebackground="black",
    )
    check_numeros.pack(pady=3)

    #----Checkbox Caracteres----#
    check_caracteres = tk.Checkbutton(
    root,
    text = "Caracteres especiais",
    variable=var_caracteres,
    bg="black",
    fg="white",
    selectcolor="black",
    activebackground="black",
    )
    check_caracteres.pack(pady=3)

    #----Button Senha----#
    senha_visivel = tk.BooleanVar(value=False)
    botao_senha = tk.Button(
        root,
        text="Gerar Senha",
        bg="black",
        fg="white",
        font= ("serif bold italic", 10, "bold"),
        command=lambda: gerar_senha(entry_tamanho, var_letra, var_numeros, var_caracteres, entry_resultado)
    )
    botao_senha.pack(pady=(30, 5))

    #----Panel Resultado----#
    label_resultado = tk.Label(root, text="Senha gerada:", bg="black", fg="white", font= ("serif bold italic", 10, "bold"))
    label_resultado.pack(pady=5)

    frame_senha = tk.Frame(root, bg="black")
    frame_senha.pack()

    entry_resultado = tk.Entry(
        frame_senha, 
        justify="center", 
        width=30, 
        font=("serif bold italic", 10, "bold"), 
        show="*"
    )
    entry_resultado.pack(side="left")

    #Função para mostrar senha
    def visibilidade_senha():
        if senha_visivel.get():
            entry_resultado.configure(show="*")
            botao_mostrar.configure(text="👁")
            senha_visivel.set(False)
        else:
            entry_resultado.configure(show="")
            botao_mostrar.configure(text="🙈")
            senha_visivel.set(True)

    #----Button Mostrar----#
    botao_mostrar = tk.Button(
        frame_senha,
        text="👁",
        bg="black",
        fg="white",
        command=visibilidade_senha
    )
    botao_mostrar.pack(side="right")
    

    #----Button Copiar----#
    botao_copiar = tk.Button(
        root,
        text="Copiar Senha",
        bg="black",
        fg="white",
        font= ("serif bold italic", 10, "bold"),
        command= lambda: copiar_senha(root, entry_resultado)
    )
    botao_copiar.pack(pady=15)

    #----Buttton Tema----#
    botao_tema = tk.Button(
        root,
        text="Tema Claro",
        bg="white",
        fg="black",
        font= ("serif bold italic", 10, "bold"),
        command=alternar_tema
    )
    botao_tema.pack(side="right", pady=20, padx=10)


    root.mainloop()



if __name__ == "__main__":
    criar_interface()


