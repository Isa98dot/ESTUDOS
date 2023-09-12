# faça um programa que leia um  número inteiro e mostre o seu sucessor e seu antecessor
n = int(input('Digite um número: '))
print('Número', n, '\n O sucessor é:', n+1, '\n O antecessor é:', n-1)

# explicação da aula, pode ser usado com .format também
print('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(n, n-1, n+1))
