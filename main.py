nome = input('Digite o seu nome: ')
print(f'Olá {nome}, seja bem vindo(a)!')

n1 = int(input(f'{nome}, digite a nota que você tirou na primeira prova: '))
n2 = int(input('Agora, digite a nota que você tirou na segunda prova: '))
n3 = int(input('Digite a nota que você ganhou no trabalho: '))

média = n1 + n2 + n3 / 3 

if média > 6:
    print(f'{nome}, sua média é {média}, parabéns, você está aprovado(a)!')
else:
    print(f'{nome}, sua média é {média}, infelizmente você está reprovado...')