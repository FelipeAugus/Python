def exibir(loops):
	pos = 1
	for x in range(-loops+1, loops):
		# Define a quantia de espaços a serem inseridos antes do #
		if x<0: 
			ant = x*-1;  
		else: 
			ant = x
		if (x != -loops+1) and (x != loops-1): 
			# Printa se não for o 1 ou ultimo
			print(ant*" "+"#"+pos*" "+"#") 
			# Atualiza a quantidade de caracter após o #
			if x<0: 
				pos += 2;
			else: 
				pos -= 2;
		else: 
			# printa se for o 1 ou ultimo
			print(ant*" "+"#")

L = int(input('Quantas hashtags? '))
exibir(L)
