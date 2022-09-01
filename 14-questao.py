x = float(input("Digite a quantidade de peixes em quilos: "))
if x<50: 
    y=0
    m=0
else: 
    y = x-50
    m = 4*y
format(m,".0f")
print(f"\nvocê pegou {x}Kg de peixe. \nO peso excedente foi de {y}Kg. \nA multa será de {m} reais.\n")
