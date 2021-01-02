originalA = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
originalN = list('0123456789')

proc = int(input('Deseja [1]criptografar ou [0]descriptografar?'))

rotA = int(input('Qual rotacionamento para os valores alfabeticos?'))

rotN = int(input('Qual rotacionamento para os valores numericos?'))

palavra = (input('Palavra: '))

if proc == 1:
	criptoA = originalA[rotA:len(originalA)]+originalA[0:rotA]
	criptoN = originalN[rotN:len(originalN)]+originalN[0:rotN]
else:
	criptoA = originalA[len(originalA)-rotA:len(originalA)]+originalA[0:len(originalA)-rotA]
	criptoN = originalN[len(originalN)-rotN:len(originalN)]+originalN[0:len(originalN)-rotN]

saida = ''
for x in palavra:
	if x == ' ': saida += ' '
	elif x.isnumeric(): saida += criptoN[originalN.index(x)] 
	elif x.isalpha(): saida += criptoA[originalA.index(x)]

print(saida)