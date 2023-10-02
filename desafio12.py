# faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto
preço = float(input('Preço do produto: '))
print('O produto com preço {}, está na promoção de 5%, por {}'.format(preço, preço-preço*5/100))

