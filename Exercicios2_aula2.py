dados = [12, 18, 25, 30, 16, 10]

media= sum(dados) / len(dados)

maior=0
menor=0

for valor in dados:
    if valor > media:
        maior +=1
    elif valor < media:
        menor +=1

print(f'Média: {media}')
print(f'Acima da média: {maior}')
print(f'Abaixo da média: {menor}')
