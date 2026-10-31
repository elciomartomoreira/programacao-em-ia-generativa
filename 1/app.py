# print('olá mundo')


# # palavra() 



# # tipos  de dados primitivos 


# 10
# 'texto'
# 5.9
# True
# False


# # tipos de estruturas de dados


# variaveis  = 10


# listas = [10,20,30,60,60]
# listas.append(100)
# print(listas)


# #         0  1  2  3  4
# tuplas = (10,30,60,6)
# tuplas += (150,20)
# print(tuplas)


# tupla = 1,2,3,6
# tupla3 = tuple(range(1,11))
# #         0  1  2  3  4
# conjuntos  = {10,30,20}
# dicionarios  = {
# 'endereco':"rua x",
# 'curso':'python'
# }

# escola
# cadastro

#exe.





acesso = input('Deseja acessar o sistema? s/n-- ')

while  acesso == 's':
    print('SISTEMA ESCOLA XYZ')
    nome = input('NOME ALUNO>> 😊') # variável
    nota_1 = float(input('Nota 1>>✔ '))
    nota_2 = float(input('Nota 2>>✔ '))
    nota_3 = float(input('Nota 3>>✔ '))

    #media

    lista = []
    lista.append(nota_1)
    lista.append(nota_2)
    lista.append(nota_3)

    media = sum(lista)/len(lista)

    print('O aluno(a)', nome, 'possui a média', media)

    if media >= 7:
        print(f'O {nome} Passou de ano👍')
    elif media >= 5 and media <7:
        print(f'O {nome} Está em recuperação😢')
    else:
        print(f'O {nome} não passou de ano🤦‍♀️')
    acesso = input('Deseja continuar? s/n>> ')

print('Até logo...')
input('clique enter para sair')
