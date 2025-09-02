# atv1 5
# atv1 4.0
# você deve desenvolver um
# programa que receba:
# A potência da lâmpada (em watts),
# As dimensões do cômodo (largura e comprimento, em metros).
# Considere que:
# A potência ideal de iluminação é de 3 watts por metro quadrado.
# A cada 3 m2 deve haver um bocal para uma lâmpada.
# O programa deve calcular:
# A área do cômodo,
# A potência total necessária,
# A quantidade de lâmpadas necessárias (arredondando para cima).

'''print('area de um comodo: ')
        
while True: 
    try: 
       comprimento = float(input('qual comprimento do comodo? '))
       break 
    except: 
        print('digite um numero valido: ')

while True: 
    try: 
        largura = float(input('qual largura do comodo? '))
        break 
    except: 
        print('digite um numero valido: ')

while True: 
    try: 
        area = (comprimento) * (largura)
        break 
    except:
        print('digite um numero valido: ')

print(f'a area e de {comprimento} * {largura} = {area}')

input('quer saber qual potencia total de watts para seu comodo? ')
while True: 
    try: 
        watts_por_metro = float(input('quantos watts por metro? '))
        break 
    except: 
        print('digite um numero valido: ')

while True: 
    try: 
        potencia_total = (watts_por_metro) * (area) 
        break 
    except: 
        print('digite um numero valido: ')
print(f'potencia total necessaria de: {watts_por_metro} * {area} = {potencia_total}')  
print('quer saber total de lampadas para iluminacao completa do comodo? ')
while True: 
    try: 
        potencia_lampada = float(input('qual potencia da sua lampada? '))
        break 
    except: 
        print('digite um numero valido: ')
while True: 
    try: 
        total_lampada = (potencia_total) / ( potencia_lampada) 
        break 
    except: 
        print('digite um numero valido: ')
print(f'serao necessarias {potencia_total} / {potencia_lampada} = {total_lampada} lampadas')'''



while True: 
    try: 
        comprimento = float(input('digite o comprimento: '))
        break 
    except: 
        print('digite um numero valido: ')


while True: 
    try: 
        largura = float(input('digite a largura: '))
        break 
    except: 
        print('digite um numero valido: ')
        
while True:
    try: 
        altura = float(input('digite um numero valido: '))
        break 
    except: 
        print('digite um numero valido: ')
 
while True: 
    try: 
        area_parede = 2 *(comprimento) * (altura) + 2 * (largura) * (altura)
        break 
    except: 
        print('digite um numero valido: ')
        
