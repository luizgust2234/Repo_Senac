#atv_aula4

qtdd = int(input('quantos produtos deseja cadastrar? '))
print('digite o nome e o valor de cada produto! ')
 
nomes = []
valores = []

for i in range(qtdd):
    nome = input(f'digite o nome do {i+1} produto: ')
    valor = float(input(f'digite o valor do {i+1} produto: R$ ')) 
    nomes.append(nome)
    valores.append(valor)

    print('\n===== relatorio de produtos =====')
    for i in range(qtdd):
        print(f'{i+1}. {nomes[i]} - R$ {valores[i]:}')
        


