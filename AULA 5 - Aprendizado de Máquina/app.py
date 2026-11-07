# BIBLIOTECA PARA ALEATORIEDADE
import random

# numero = random.randint(1,10)
# print(numero)

import random
print ('JOGO DA ALEATORIEDADE...')
print('GANHE ATÉ r$ 5K ')
print('Escolha um número de 1 a 20')


numero_maquina = random.randint(1,20)

for chances in range(3):
    numero_usuario = int(input('Escolha o seu número>> '))

    if numero_maquina == numero_usuario:
        print('VOCE GANHOU 5K!!')
        break #sai do jogo
    else:
        print('VOCE ERROU FEIO')
    
print('Fim de jogo')
