nome = input('Digite o seu nome: ')
print(f'Olá {nome}, seja bem vindo(a)!\n')

n1 = int(input(f'{nome}, digite a nota que você tirou na primeira prova: '))
n2 = int(input('\nAgora, digite a nota que você ganhou no trabalho: '))
n3 = int(input('\nDigite a nota da segunda prova: '))

soma = (n1 + n2 + n3) / 2

print(f'{nome}, sua média é {soma}.')

input('\nAperte enter para fechar esta janela ')