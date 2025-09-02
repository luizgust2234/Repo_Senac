# atv1
print('area de um comodo')

while True:  
    try: 
        comprimento = float(input('qual comprimento do comodo? '))
        break 
    except: 
        print('digite um numero valido ')

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
 
print(f'area é de {comprimento} * { largura} = {area}')
input('quer saber qual potecia total de watts para seu comodo? ')

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

print(F'potencia total necessaria de : {watts_por_metro} * {area} = {potencia_total}')
input('quer saber o total de lampadas para iluminacao do seu comodo? ')

while True:  
    try: 
        potencia_lampada = float(input('qual potencia da sua lampada? '))
        break 
    except: 
        print('digite um numero valido: ')

while True:  
    try: 
        total_lampada = (potencia_total) / (potencia_lampada)
        break 
    except: 
        print('digite um numero valido: ')
print(total_lampada)
