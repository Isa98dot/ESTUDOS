# faça um programa que leia a largura e a altura de uma parede em metros
# calcule sua área e a quantidade de tinta necessária para pinta-la
# sabendo que cada litro de tinta, pinta uma área de 2m²

l = float(input('Digite a largura: '))
a = float(input('Digite a altura: '))
area = l * a
print('A área é: {} metros quadrados'.format(area))

tinta = area / 2
print('Será necessário {}l de tinta'.format(tinta))
