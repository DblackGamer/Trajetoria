import random as rd
jogo = ["pedra", "papel", "tesoura"]

jogador = input("Escolha pedra, papel ou tesoura: ").lower()
computador = rd.choice(jogo)
print(f"Você escolheu {jogador} e o computador escolheu {computador}")

if jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") or (jogador == "papel" and computador == "pedra") or (jogador == "tesoura" and computador == "papel"):
    print("Você ganhou!")
else:
    print("Você perdeu!")