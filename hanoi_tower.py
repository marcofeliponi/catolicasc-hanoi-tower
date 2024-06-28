def torre_hanoi(numero_pecas, saida, destino, auxiliar):
	if numero_pecas==1:
		print ("Mover peça 1 da pilha", saida, "para a pilha", destino)
		return
	torre_hanoi(numero_pecas-1, saida, auxiliar, destino)
	print ("Mover peça", numero_pecas, "da pilha", saida, "para a pilha", destino)
	torre_hanoi(numero_pecas-1, auxiliar, destino, saida)

numero_pecas = 4
saida = 'A'
destino = 'C'
auxiliar = 'B'
torre_hanoi(numero_pecas, saida, destino, auxiliar)
