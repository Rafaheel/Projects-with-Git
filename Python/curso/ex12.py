preco = float(input('Por gentileza informe o preço do produto: '))
desconto = (preco * 5) / 100
novo_preco = preco - desconto
print(f'O preço do produto desejado é de R${preco}, porém com a nova promoção hoje é de R${novo_preco :.2f}')