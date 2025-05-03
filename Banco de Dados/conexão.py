import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)
mycursor = mydb.cursor()

#Aqui ele deleta a tabela convidados caso ela já exista.
mycursor.execute("DROP TABLE IF EXISTS convidados")

#Aqui ele cria a tabela convidados com os campos nome e idade.
mycursor.execute("CREATE TABLE convidados (nome VARCHAR(255), idade int(11))")

#Aqui mostra os convidados que estão na lista.
def lista_convidados():
    mycursor.execute("SELECT * FROM convidados")
    for i in mycursor:
        print(i)
lista_convidados()

#Aqui mostra os convidados que estão na lista.
def lista_convidados():
    mycursor.execute("SELECT * FROM convidados")
    for i in mycursor:
        print(i)
lista_convidados()
#Convidado
nome_convidado=input("Digite seu nome:")
idade_convidado=int(input("Digite sua idade:"))

#aqui verifica e inclui na lista de convidados.
def inclusão_na_lista():
        if idade_convidado >= 18:
            print("Você pode entrar")
            mycursor.execute("INSERT INTO convidados (nome, idade) VALUES (%s, %s)", (nome_convidado, idade_convidado)) 
            mydb.commit()
            print(mycursor.rowcount, "registro(s) inserido(s).")
            
        else:
            print("Você não pode entrar")
inclusão_na_lista()

#Aqui mostra os convidados que estão na lista.
def lista_convidados():
    mycursor.execute("SELECT * FROM convidados")
    for i in mycursor:
        print(i)
lista_convidados()


