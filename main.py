# EXERCÍCIO 4

# Lista e dicionário vazios para receber os valores posteriores
lista = []
dici = {}


# Laço de repetição para inserir dados na lista e dicionário
while True:
    sair = int(input('Deseja cadastrar novo produto? 1-sim, 0-não:')) # Opção para cadastro ou encerramento
    if(sair != 1 and sair != 0): # condição para fazer com que o usuário use somente 1 ou 0 para iniciar ou encerrar o programa
        print('Ooops, você digitou um número inválido.')
    elif(sair == 1):# condiçao para após satisfeita ser inseridos os dados no dicionário
        dici['Código'] = int(input('Digite o código:'))
        dici['Estoque'] = int(input('Digite a quantidade em estoque:'))
        dici['Mínimo'] = int(input('Digite o estoque mínimo:'))
        lista.append(dici.copy()) #Função para inseir o dicionário na lista
        continue
    elif (sair == 0):#Condição para encerrar o programa
        print('Você optou por não cadastrar um novo item, o programa será encerrado!')
        break
print()

# Ordenando a lista em ordem crescente
lista_or = sorted(lista, key= lambda item: item['Código'])
print(lista_or)
print()
print()
if len(lista_or) > 0: # Condição para ajustar a lista em forma de tabela
    print('Código'.center(10), end='')
    print('Estoque'.center(10), end='')
    print('Mínimo'.center(10),)

    for x in lista_or: # Condição para ajustar os dados em tabela
        print(str(x['Código']).center(10), end='')
        print(str(x['Estoque']).center(10), end='')
        print(str(x['Mínimo']).center(10),)
