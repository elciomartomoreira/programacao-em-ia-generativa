import random
import string

caracteres = string.ascii_letters + string.digits + string.punctuation

# sorteia apenas um caracter aleatório

# um_caracter = random.choices(caracteres)
# print('caracter sorteado>>', um_caracter)

tamanho_senha = 8

senha = " "

for i in range(tamanho_senha):
    caracter_sorteado = random.choice(caracteres)
    senha = senha + caracter_sorteado

print(f"Sua senha gerada é: {senha}")
