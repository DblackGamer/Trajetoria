print("Bem vindo Sr(a)")
print("--------------")

#Convidado
nome_convidado=input("Digite seu nome:")
idade_convidado=int(input("Digite sua idade:"))

#aqui verifica e inclui na lista de convidados.
def inclusão_na_lista():
        if idade_convidado >= 18:
            print("Você pode entrar")
            convidados_permitidos=[nome_convidado]
            print(convidados_permitidos)
        else:
            print("Você não pode entrar")
inclusão_na_lista()