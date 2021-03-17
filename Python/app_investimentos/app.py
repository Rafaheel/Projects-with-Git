from utilidades import apresentar_programa, verde, vermelho, azul, amarelo, separar_por_linha
from utilidades import ler_investimentos_existentes
from utilidades import exibir_investimento_total
from utilidades import apresentar_menu
from utilidades import listar_investimentos
from utilidades import editar_investimentos_existentes


# 1º metodo do arquivo utilidades
# apresentar_programa()


# 3º metodo do arquivo utilidades
ler_investimentos_existentes()


# 4º metodo do arquivo utilidades
# exibir_investimento_total()


if __name__ == "__main__":
    apresentar_programa()
    exibir_investimento_total()
    #listar_investimentos()
    while True:
        opcao = apresentar_menu()
        if opcao == '1':
            listar_investimentos(exibir_todos=True)            
        if opcao == '2':
            investimento_id = input('Qaul investimento deseja alterar? ')
            editar_investimentos_existentes(investimento_id)
        if opcao == '3':
            pass
        if opcao == '4':
            pass
        
