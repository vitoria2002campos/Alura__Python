import forca
import adivinhacao

print('Escolha o seu jogo')
print('[1]forca [2] adivinhação')

jogo = int(input('Insira o numero do jogo desejado: '))

if(jogo == 1):
    print('jogando forca')
    forca.jogo_forca() #pega o modulo .py e chama a funcao jogo_forca
elif(jogo == 2):
    print('jogando adivinhacao')
    adivinhacao.jogar_adivinhacao()