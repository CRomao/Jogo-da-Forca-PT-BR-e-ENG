from time import sleep
import os
import random
manDoll = ['''
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
words = 'RICE CARROT ONION WICKED CAT PEOPLE WOLF DOG SECOND THIRD GAME LESSER MORE FRUIT WATERMELON BROWSER FILE'.split()
selected = 0
lettersE = 0
cont = 0
lettersT = []
def restrictions():
    print("It must contain at least two letters - it must be a real word!")

print("-=-=-=-HANGMAN GAME-=-=-=-\n\n")
print("1 - One Player\n")
print("or\n")
print("2 - Two Players\n\n")
x = str(input("-=- Choose an option:"))
if x == '1':
    selected = random.choice(words)
elif x == '2':
    os.system('cls' if os.name == 'nt' else 'clear')
    restrictions()
    selected = str(input("\nEnter the word:")).upper()
    while len(selected) == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Not a valid word!\n")
        restrictions()
        selected = str(input("\nEnter the word:")).upper()
while x != '1' and x != '2':
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Invalid option!\n")
    x = str(input("1 - One Player\n2 - Two Players\n\n-=-Choose an option:"))
    if x == '1':
        selected = random.choice(words)
    elif x == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        restrictions()
        selected = str(input("\nEnter the word:")).upper()
        while len(selected) == 1 or selected in '1234567890Ç-=+[]()*&¨%$#@!´~/;.,<>:?`''""ÁÀÉÈÍÌÓÒÚÙÃÕÂÊÎÔÛ':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Not a valid word!\n")
            restrictions()
            selected = str(input("\nEnter the word:")).upper()
os.system('cls' if os.name == 'nt' else 'clear')

lines = (len(selected) * '__ ').split()
print(manDoll[lettersE])
loop = 1
for i in range(len(selected)):
    print(lines[i], end=' ')
print('\n')

while loop:
    player = str(input('Enter a letter: ')).upper()
    print()
    while len(player) != 1 or player not in 'ABCDEFGHIJKLMNOPQRSTUVWYXZ' or player in lettersT:
        print('Only ONE letter is allowed!\nTry again!')
        player = str(input('Enter a letter: ')).upper()
        print()
        while player not in 'ABCDEFGHIJKLMNOPQRSTUVWYXZ':
            print('Only letters are allowed!\nTry again!')
            player = str(input('Enter a letter: ')).upper()
            print()
        while player in lettersT:
            print('This letter has already been typed!\nTry another.')
            player = str(input('Digite uma letra: ')).upper()
    if player in selected:
        for i in range(len(selected)):
            if player == selected[i]:
                lines[i] = player
        os.system('cls' if os.name == 'nt' else 'clear')
        print(manDoll[lettersE])
        for i in range(len(selected)):
            print(lines[i], end=' ')
        print('\n')
        print('Wrong letters: ',end='')
        for i in range(len(lettersT)):
            print(lettersT[i], end=' ')
        print()
    else:
        lettersT.append(player)
        lettersE = lettersE + 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(manDoll[lettersE])
        for i in range(len(selected)):
            print(lines[i], end=' ')
        print('\n')
        print('Wrong letters: ', end='')
        for i in range(len(lettersT)):
            print(lettersT[i], end=' ')
        print()
    for i in range(len(lines)):
        if lines[i] in 'ABCDEFGHIJKLMNOPQRSTUVWYXZ':
            cont = cont + 1
    if cont < len(selected):
        cont = 0
    if cont == len(selected):
        print('Congratulations, you got it!')
        print('{} chances left.'.format(7 - lettersE))
        break
        sleep(5)
    if lettersE == 7:
        print('You lose!\nThe word was: {}'.format(selected))
        break
        sleep(5)
sleep(5)