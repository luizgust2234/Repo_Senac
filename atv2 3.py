# atv2 3.0

while True: 
    try: 
       comprimento = float(input('digite o comprimento: ')) 
       break 
    except: 
       print('digite um numero valido')
    
while True: 
    try: 
       largura = float(input('digite a largura: ')) 
       break 
    except: 
       print('digite um numero valido')

while True: 
    try: 
        altura = float(input('digite a altura ')) 
        break 
    except:
        print('digite um numero valido')

while True: 
    try: 
        area_parede = 2 * (comprimento * altura) + 2 * (largura * altura)
        break 
    except: 
        print('digite um numero valido')

print(f'a area total da parede é {area_parede} m²')

while True: 
    try: 
        rendimento_caixa = float(input('digite o rendimento da caixa: '))
        break 
    except:
        print('digite um numero valido')

while True: 
    try: 
        quantidade_de_caixas =(area_parede) / (rendimento_caixa)
        break  
    except: 
        print('digite um numero valido: ')
        
print(f'serao necessarias {quantidade_de_caixas} caixas ')

        
