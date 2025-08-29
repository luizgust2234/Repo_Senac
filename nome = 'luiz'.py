'''aluno = input('digite nome do aluno: ')
nota1 = int(input('digite a primeira nota: '))
nota2 = int(input('digite a segunda nota: ')) 
media = (nota1 + nota2) /2
print
if media >=7: 
 print('Aprovado')''',


# usuario informar seu nome
# numero de noites q dseja ficar
# e o tipo de quarto
# programa deve calcular o valor total da estadia e exibir uma confirmacao formatada
print('Bem vindo ao hotel Konoha! ')
print('quantas noites deseja ficar? ')
print('temos quarto genin R$ 120')
print('temos quarto jounin R$ 180')
print('temos quarto hokage R$ 250')




while True:  
    try:
        nome = input('digite seu nome: ')
        break
    except:
        print('digite um nome valido') 
while True:  
    try:
        idade = int(input('digite o numero de dias: '))

        break
    except:
        print('digite um numero valido: ')

while True:  
    try:
        tipo_quarto = input('digite o tipo de quarto: ')
        break 
    except: 
       print('digite um numero valido: ')


