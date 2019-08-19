from time import sleep
import os
import random
BONECO = ['''
     ________
    |       |
    |
    |  
    |
    |
    |
            ''',
'''
     ________
    |       |
    |       O
    |       
    |
    |
    |      
            ''',
'''
     ________
    |       |
    |       O
    |       |
    |
    |
    |      
            ''',
'''
     ________
    |       |
    |       O
    |      /|
    |       
    |
    |      
            ''',
'''
     ________
    |       |
    |       O
    |      /|\ 
    |       
    |
    |      
            ''',
'''
     ________
    |       |
    |       O
    |      /|\ 
    |       |
    |
    |      
            ''',
'''
     ________
    |       |
    |       O
    |      /|\ 
    |       |
    |      /
    |      
            ''',
'''
     ________
    |       |
    |       O
    |      /|\ 
    |       |
    |      / \ 
    |      
            ''']
palavras = 0
escolhida = 0

def validarPalavra():
    global escolhida
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Não é uma palavra válida!\n")
    print("OBS: Digite a palavra sem acentos e sem 'Ç'.")
    print("Deve conter no mínimo duas letras - devendo ser realmente uma palavra! -  e não pode ter dígitos!")
    escolhida = str(input("\nDigite a palavra:")).upper()

def mensagem():
    global BONECO, letrasE, escolhida, linhas, letrasT
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BONECO[letrasE])
    for i in range(len(escolhida)):
        print(linhas[i], end=' ')
    print('\n')
    print('Letras erradas: ',end='')
    for i in range(len(letrasT)):

print("-=-=-=-JOGO DA FORCA-=-=-=-\n\n")
print("1 - Player\n")
print("ou\n")
print("2 - Players\n\n")
x = str(input("-=- Escolha uma opção:"))
if x == '1':
    palavras = 'ARROZ FEIJAO CENOURA CEBOLA MAU GATO GENTE PESSOA LOBO CACHORRO SEGUNDO SEGUNDA TERCEIRO JOGO MENOS MAIS FRUTA MELANCIA ARQUIVO NAVEGADOR'.split()
    escolhida = random.choice(palavras)
elif x == '2':
    os.system('cls' if os.name == 'nt' else 'clear')
    print("OBS: Digite a palavra sem acentos e sem 'Ç'.")
    print("Deve conter no mínimo duas letras - devendo ser realmente uma palavra! -  e não pode ter dígitos!")
    escolhida = str(input("\nDigite a palavra:")).upper()
    while len(escolhida) == 1 or escolhida in '1234567890Ç-=+[]()*&¨%$#@!´~/;.,<>:?`''""ÁÀÉÈÍÌÓÒÚÙÃÕÂÊÎÔÛ':
        #'1234567890Ç-=+[]()*&¨%$#@!´~/;.,<>:?`''""ÁÀÉÈÍÌÓÒÚÙÃÕÂÊÎÔÛ'
        validarPalavra()
while x != '1' and x != '2':
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Opção inválida!\n")
    x = str(input("1 - Player\n2 - Players\n\n-=-Escolha uma opção:"))
    if x == '1':
        palavras = 'ARROZ FEIJAO CENOURA CEBOLA MAU GATO GENTE PESSOA LOBO CACHORRO SEGUNDO SEGUNDA TERCEIRO JOGO MENOS MAIS FRUTA MELANCIA ARQUIVO NAVEGADOR'.split()
        escolhida = random.choice(palavras)
    elif x == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("OBS: Digite a palavra sem acentos e sem 'Ç'.")
        print("Deve conter no mínimo duas letras - devendo ser realmente uma palavra! -  e não pode ter dígitos!")
        escolhida = str(input("\nDigite a palavra:")).upper()
        while len(escolhida) == 1 or escolhida in '1234567890Ç-=+[]()*&¨%$#@!´~/;.,<>:?`''""ÁÀÉÈÍÌÓÒÚÙÃÕÂÊÎÔÛ':
            # '1234567890Ç-=+[]()*&¨%$#@!´~/;.,<>:?`''""ÁÀÉÈÍÌÓÒÚÙÃÕÂÊÎÔÛ'
            validarPalavra()
os.system('cls' if os.name == 'nt' else 'clear')
#palavras = 'ARROZ FEIJAO CENOURA CEBOLA MAU GATO GENTE PESSOA LOBO CACHORRO SEGUNDO SEGUNDA TERCEIRO JOGO MENOS MAIS FRUTA MELANCIA ARQUIVO NAVEGADOR'.split()
#escolhida = random.choice(palavras)
letrasE = 0
linhas = (len(escolhida) * '__ ').split()
cont = 0
letrasT = []
print(BONECO[letrasE])
a = 1
for i in range(len(escolhida)):
    print(linhas[i], end=' ')
print('\n')
while a == 1:
    jogador = str(input('Digite uma letra: ')).upper()
    print()
    while len(jogador) != 1 or jogador not in 'ABCDEFGHIJKLMNOPQRSTUVWYXZ' or jogador in letrasT:
        while len(jogador) != 1:
            print('Só é permitido apenas UMA letra!\nTente de novo!')
            jogador = str(input('Digite uma letra: ')).upper()
            print()
        while jogador not in 'ABCDEFGHIJKLMNOPQRSTUVWYXZ':
            print('Só é permitido LETRAS!\nTente de novo!')
            jogador = str(input('Digite uma letra: ')).upper()
            print()
        while jogador in letrasT:
            print('Essa letra já foi digitada!\nTente outra.')
            jogador = str(input('Digite uma letra: ')).upper()
    if jogador in escolhida:
        for i in range(len(escolhida)):
            if jogador == escolhida[i]:
                linhas[i] = jogador
        mensagem()
    else:
        letrasT.append(jogador)
        letrasE = letrasE + 1
        mensagem()
    for i in range(len(linhas)):
        if linhas[i] in 'ABCDEFGHIJKLMNOPQRSTUVWYXZ':
            cont = cont + 1
    if cont < len(escolhida):
        cont = 0
    if cont == len(escolhida):
        print('Parabéns, você terminou!')
        print('Restou {} chance(s).'.format(7 - letrasE))
        break
        sleep(5)
    if letrasE == 7:
        print('Você perdeu!\nA palavra era: {}'.format(escolhida))
        break
        sleep(5)
sleep(5)