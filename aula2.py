#Aqui aprenderemos sobre o looping, utilizando o For e While
#For serve para, geralmente printar tudo que há numa lista
x= [1,2,3,4,5,6]
for i in x:
    print(i)
#While tem uma função um pouco diferente

y= 10
while y <= 20 :
    print (y)
    y+=1

#Agora aqui é for com range
for i in range(6):
    print(f"Valor de `I` é:{i}")

#Agora algo mais complexo

# Exemplo de 'while' com condição de saída
soma = 0
numero = 1

while soma < 10:
    soma += numero  # adiciona o valor de 'numero' a 'soma'
    print("Soma atual:", soma)
    numero += 2  # aumenta o valor de 'numero' a cada iteração
#For, tentar fazer aparecer um número primo
for numero in range(1, 10):
    if numero == 10:
        break  # para o loop quando numero é 5
    elif numero % 2 == 0:
        continue  # pula números pares
    print("Número ímpar:", numero)

# Lista de dados de exemplo
dados = [10, 20, 30]
soma_total = 0

for valor in dados:
    soma_total = (soma_total+valor)/2

print("Media total dos dados:", soma_total)
