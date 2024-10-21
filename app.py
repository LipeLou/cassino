from random import randint
import matplotlib.pyplot as plt 
from main import CassaNiquel, Player


maquina1 = CassaNiquel(level=3)

JOGADORES_POR_DIA = 30
APOSTAS_POR_DIA = 5
DIAS = 10
VALOR_MAXIMO = 200

saldo = []

players = [Player() for i in range(JOGADORES_POR_DIA)]

# 30 Jogadores, apostando entre 5-200 reais 5 vezes durante 30 dias.
for i in range(0, DIAS):
    for j in players:
        for k in range(0, randint(1, APOSTAS_POR_DIA)):
            maquina1.play(randint(5, VALOR_MAXIMO), j, display=False)
    saldo.append(maquina1.gain)

# Ganho do Cassino
plt.figure()
x = [i for i in range(1, DIAS+1)]
plt.plot(x,saldo)
plt.show()

# Jogadores
plt.plot([i for i in range(JOGADORES_POR_DIA)], [i.balance for i in players])
plt.grid(True)
plt.show()


