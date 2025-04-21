#Isso é uma lista, onde pode ser alterada.
x=[2,5,6,123,5]
print (x)
x.append(29)
print(len(x))

print(x)
#Isto é uma tupla, one não pode ser alterada
y=(2,65,21,3123)
print(y)

#única maneira de alterar uma tupla é transformando em lista
z=list(y)
z[1]='Kiwi'
z.append(254)
y=tuple(z)
print(y)

#Aqui basciamente muda a maneira de chamar o index da 
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

for i in range(len(fruits)):
    print(fruits[i])