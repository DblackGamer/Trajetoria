#1Calcular média e Desvio médio
dados= [15,20,30,10,25]
#Aqui é a variavel da soma dos itens da lista
soma_dados= sum(dados)
#aqui é a variavel onde será calculado a media, utilizando a variavel "soma_dados" e len(dados)
media_dados= soma_dados/len(dados)

#aqui vai printar a media 
print(media_dados)

#Diferença absolutas e armazenar numa lista
diferenca=[abs(valor - media_dados) for valor in dados]

#Cacular o Desvio médio
desvio_medio=sum(diferenca)/len(dados)

print(desvio_medio)