#     _    ____ _____     _____ _   _ _   _    _    
#    / \  |  _ \_ _\ \   / /_ _| \ | | | | |  / \   
#   / _ \ | | | | | \ \ / / | ||  \| | |_| | / _ \  
#  / ___ \| |_| | |  \ V /  | || |\  |  _  |/ ___ \ 
# /_/___\_\____/___| _\_/__|___|_| \_|_| |_/_/   \_\
#  / ___|  / \  |  \/  | ____|                      
# | |  _  / _ \ | |\/| |  _|                        
# | |_| |/ ___ \| |  | | |___                       
#  \____/_/   \_\_|  |_|_____|                      

#AUTOR: Nicole Beatriz Arguelles
#VERSÃO: 1.0.0
#LICENÇA: OPEN SOURCE

from random import randint

random = randint(1, 100)
chute = 101
chances = 10

while chute != random : 
    chute = input('chute um número de 0 a 100:')
    if chute.isnumeric() :
        chute = int(chute)
        chances = chances - 1
        if chute == random :
            print('')
            print ('Parabéns!:D Você acertou, o número secreto era {} e você ainda {} chances.'.format(random, chances))
            print('')
            break
        else:
             print('')
             if chute > random:
                 print('Você errou! Dica: É um número menor')
             else:
                 print('Você errou! Dica: É um número maior')    
             print('Você ainda tem {} chances,'.format(chances))
             print('')
        if chances == 0:
             print('')
             print('Suas chances acabaram, você perdeu, o número era: {}'.format(random)) 
             print('')
             break
print('GAME OVER')         