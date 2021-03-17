import json
from pathlib import Path


'''
Cores ANSII:
Vermelha \u001b[31m
Amarela \u001b[33m
Azul \u001b[34m
Verde \u001b[32m
'''


''' 1º METODO
Metodo que cria uma apresentação visual da aplicação no terminal
'''


def separar_por_linha():
    print('-' * 82)


def vermelho(palavra):
    print(f'\u001b[31m {palavra}\u001b[0m')


def amarelo(palavra):
    print(f'\u001b[33m {palavra}\u001b[0m')


def azul(palavra):
    print(f'\u001b[34m {palavra}\u001b[0m')


def verde(palavra):
    print(f'\u001b[32m {palavra}\u001b[0m')


def apresentar_programa():
    separar_por_linha()
    print("\u001b[32m Invista-me\u001b[0m")
    print(" " * 35 + "\u001b[32m Pronto para investir?\u001b[0m")
    separar_por_linha()


''' 2º METODO
Metodo que cria o arquvo JSON dos investimentos
'''


def criar_investimentos_iniciais():
    lista_de_investimentos_json = [
        {
            "id": 1,
            "nome": "Celular",
            "valor": 1500
        },
        {
            "id": 2,
            "nome": "Geladeira",
            "valor": 1300
        },
        {
            "id": 3,
            "nome": "Notebook",
            "valor": 3500
        },
        {
            "id": 4,
            "nome": "Iphone",
            "valor": 7000
        },
        {
            "id": 5,
            "nome": "Placa de video",
            "valor": 2000
        },
        {
            "id": 6,
            "nome": "Ps5",
            "valor": 4999
        },
    ]
    investimentos_json = json.dumps(lista_de_investimentos_json)
    Path('investimentos.json').write_text(investimentos_json)

    '''3º METODO
    Metodo que le o arquivo json criado
    '''


def ler_investimentos_existentes():
    investimentos_json = Path('investimentos.json').read_text()
    investimentos = json.loads(investimentos_json)
    return investimentos    

'''4º METODO
   Metodo que apresenta o valor investido até o momento
'''
def exibir_investimento_total():
    investimentos = ler_investimentos_existentes()
    total = 0
    for investimento in investimentos:
        total = investimento['valor'] + total
    verde('O total investido até o momento é ' + 'R$ ' + str(total))


'''5º METODO
   Metodo que lista os 5 primeiros investimentos até o momento
'''


def listar_investimentos(exibir_todos=False):
    print('Em Manutenção')
    '''
    from tabulate import tabulate
    investimentos = ler_investimentos_existentes()
    lista_de_investimentos = []
    if exibir_todos == False:
        for investimento in investimentos[0:5]:
            lista_de_investimentos.append(
                [investimento['id'], investimento['nome'], investimento['valor']])
        print(tabulate(lista_de_investimentos,
                       headers=['id', 'nome', 'valor']))
    else:
        for investimento in investimentos:
            lista_de_investimentos.append(
                [investimento['id'], investimento['nome'], investimento['valor']])
        print(tabulate(lista_de_investimentos,
                       headers=['id', 'nome', 'valor']))
                       '''
    



'''6º METODO
   Metodo que cria o menu para o usuario
'''
def apresentar_menu():
    separar_por_linha()
    verde('1 - Listar todos os investimentos')
    amarelo('2 - Editar investimentos existente')
    vermelho('3 - Excluir um investimento')
    azul('4 - Criar investimento')
    opcao = input('Escolha uma opção: ')
    separar_por_linha()
    return opcao


def editar_investimentos_existentes(investimento_id):
    investimentos = ler_investimentos_existentes()
    nome = input('digite o novo nome: ')
    valor = input('Digite o novo valor: ')
    for investimento in investimentos:
        if investimento['id'] == int(investimento_id):
            if nome != '':
                investimento.update({'nome':nome})
            if valor != '':
                investimento.update({'valor': int(valor)})
            investimento_json = json.dumps(investimentos)
            Path('investimentos.json').write_text(investimento_json)
            print(investimento)
            
