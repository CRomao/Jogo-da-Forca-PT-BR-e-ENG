import os # Método necessário para limpar a tela.
from time import sleep # Método para dar alguns segundos de tempo no jogo.
from random import shuffle # Método para embaralhar os números.
# Matrizes
m = [[1,2,3,4], [5,6,7,8], [1,2,3,4], [5,6,7,8]]
matriz = [['*','*','*','*'], ['*','*','*','*'], ['*','*','*','*'], ['*','*','*','*']]
# Variáveis
escolha = 0 # Escolha do usuario
loop = 1 # vaiavel do while geral
s = 5 # variavel da contagem regressiva
cont = 0 # vaiavel para contar os quadrados preenchidos
tentativas = 0 # variavel para contar as tentativas do usuario

# Embaralhando somente entre as linhas da matriz 'm'.
shuffle(m)
# Embaralhando as linhas e os numeros das linhas da matriz 'm'.
for i in range(len(m)):
    shuffle(m[i])
    for j in range(i):
        shuffle(m[j])
# For para aparecer a contagem regressiva e a matriz já embaralhada.
for i in range(s):
    for i in m:
        for j in i:
            print(j, end=' ')
        print()
    print('Contagem para decorar: {}'.format(s))
    s = s - 1
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear') # vai limpar a tela a cada iteração do For.
os.system('cls' if os.name == 'nt' else 'clear') # Quando o For terminar, vai limpar a tela toda.

# While geral do jogo
while loop == 1:
    for i in matriz: # Vai mostrar a matriz 'matriz e pedir a linha e coluna, sendo informado: 1 2 -- nesse exemplo'.
        for j in i:
            print(j, end=' ')
        print()
    escolha = str(input('Digite a linha e coluna do primeiro: ')).split() # Vai separar os números.
    esc1 = escolha[0] # Vai receber a linha.
    esc2 = escolha[1] # Vai receber a coluna.
    # Aqui ele faz uma verificação se o que foi digitado foi de 0 a 3, se não, ele pede que digite novamente.
    while esc1 !='0' and esc1 !='1' and esc1 != '2' and esc1 != '3':
        while esc2 != '0' and esc2 !='1' and esc2 != '2' and esc2 !='3':
            escolha = str(input('O que foi digitado está inválido!!!\nDigite novamente a linha e coluna do primeiro: ')).split()
            esc1 = escolha[0]
            esc2 = escolha[1]
    esc1 = int(escolha[0])
    esc2 = int(escolha[1])
    # Aqui faz a verificação se a carta já foi virada ou não. Se sim, ele pede que informe outra posição.
    while matriz[esc1][esc2] != '*':
        print('Essa carta encontra-se virada!')
        escolha = str(input('Selecione outra posição:: ')).split()
        esc1 = escolha[0]
        esc2 = escolha[1]
        # Verificação se o que foi digitado é válido, após digitar uma posição já aberta.
        while esc1 !='0' and esc1 !='1' and esc1 != '2' and esc1 != '3' or esc2 != '0' and esc2 !='1' and esc2 != '2' and esc2 !='3':
                escolha = str(input('O que foi digitado está inválido!!!\nDigite novamente a linha e coluna do primeiro: ')).split()
                esc1 = escolha[0]
                esc2 = escolha[1]
        esc1 = int(escolha[0])
        esc2 = int(escolha[1])
    matriz[esc1][esc2] = m[esc1][esc2] # Se estiver tudo OK, a matriz 'matriz' na posição digitada vai receber o que tiver na mastriz 'm' na posição digiada
    os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela e mostra a matriz novamente pedindo o segundo par de números.
    for i in matriz:
        for j in i:
            print(j, end=' ')
        print()
    escolha = str(input('Digite a linha e coluna do segundo: ')).split()
    esc3 = escolha[0]
    esc4 = escolha[1]
    # faz a verificação se o que foi digitado foi de 0 a 3, se não, ele pede que digite novamente.
    while esc3 !='0' and esc3 !='1' and esc3 != '2' and esc3 != '3':
        while esc4 != '0' and esc4 !='1' and esc4 != '2' and esc4 !='3':
            escolha = str(input('O que foi digitado está inválido!!!\nDigite novamente a linha e coluna do segundo: ')).split()
            esc3 = escolha[0]
            esc4 = escolha[1]
    esc3 = int(escolha[0])
    esc4 = int(escolha[1])
    # Verifica também na segunda vez se a carta já foi virada.
    while matriz[esc3][esc4] != '*':
        print('Essa carta encontra-se virada!')
        escolha = str(input('Selecione outra posição: ')).split()
        esc3 = escolha[0]
        esc4 = escolha[1]
        # Verificação se o que foi digitado é válido, após digitar uma posição já aberta.
        while esc3 != '0' and esc3 != '1' and esc3 != '2' and esc3 != '3':
            while esc4 != '0' and esc4 != '1' and esc4 != '2' and esc4 != '3':
                escolha = str(input(
                    'O que foi digitado está inválido!!!\nDigite novamente a linha e coluna do segundo: ')).split()
                esc3 = escolha[0]
                esc4 = escolha[1]
        esc3 = int(escolha[0])
        esc4 = int(escolha[1])
    matriz[esc3][esc4] = m[esc3][esc4]
    # Aqui ele faz a verificação se o usuário digitou as mesmas posições nas duas. EX: 0 0 / 0 0, se for assim, ele pede que digite de novo.
    #while esc1 == esc3 and esc2 == esc4 and esc1 == esc4 and esc1 == esc2:
    #    print('As posições não podem ser iguais a do primeiro!!!')
    #    escolha = str(input('Digite outras posições: ')).split()
    #    esc3 = int(escolha[0])
    #    esc4 = int(escolha[1])  Código Comentado
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in matriz:  # Vai mostrar a matriz e fazer as codições lá embaixo
        for j in i:
            print(j, end=' ')
        print()
    sleep(1)
    # Se o valor da primeira posição for igual ao valor da segunda posição, ele mvai atribuir os dois na mesma posição da matriz 'matriz'
    # E vai acrescentar + 1 na variavel tentativas
    if m[esc1][esc2] == m[esc3][esc4]:
        matriz[esc1][esc2] = m[esc1][esc2]
        matriz[esc3][esc4] = m[esc3][esc4]
        tentativas = tentativas + 1
    else: # Se não for igual as posições, ele coloca o * asterisco de volta na posição. E acrescenta + 1 na tentativa também
        matriz[esc1][esc2] = '*'
        matriz[esc3][esc4] = '*'
        tentativas = tentativas + 1
    for i in matriz:  # Aqui ele faz uma verificação de quantos dos quadrados estão com números já, pra poder saber e finalizar o jogo
        for j in i:
            if j != '*':
                cont = cont + 1
    if cont == 16: # se a todos os quadrados estiverem com numeros (no total 16 quadrados), loop vai receber 2 e parar o loop geral
        loop = 2
    else: # se não for 16, cont vai receber 0 pra ficar zerado, porque se não zerar, vai continuar o valor de antes.
        cont = 0
    os.system('cls' if os.name == 'nt' else 'clear')
# Por fim ele limpa a tela em cima e embaixo mostra a matriz completa, com números e mostra as tentativas que teve.
for i in matriz:
    for j in i:
        print(j, end=' ')
    print()

print('Você tentou {} vezes'.format(tentativas))
sleep(5)