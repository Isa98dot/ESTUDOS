# crie um programa que leia quanto dinheiro uma pessoa tem  na carteira e mostre quantos dólares ela pode comprar
# considere US$1,00 = R$4,87
d = float(input('Digite um valor em reais, R$'))
print('Você pode comprar', d/(4.87), 'dólares')

print('Você pode comprar: {:.2f} dólares'.format(d/(4.87)))
