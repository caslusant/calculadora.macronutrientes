nome = str(input('Digite seu nome: '))
peso = float(input('Digite seu peso: '))
agua = peso * 40
print(f'{nome} pelo seu peso seu consumo de água diário deve ser de {agua} litros, me fale mais algumas informações')
altura = int(input('Digite sua altura em CM: '))
idade = int(input('Digite sua idade: '))
taxaMetabolica = (13.75 * peso) + (5 * altura) - (6.75 * idade) + 66.5
print(f'{nome} seu corpo para se manter vivo por dia consome {taxaMetabolica:.2f}kcal, me fale mais algumas informações')
atividadeFisica = int(input('Você pratica alguma atividade física? Digite 1 para sim e 2 para não: '))
if atividadeFisica == 1:
    tmt =  taxaMetabolica * 1.7
    print(f'{nome} seu gasto calórico diário é de {tmt:.2f}kcal por dia')
else:
    tmt = taxaMetabolica * 1.5
    print(f'{nome} seu gasto cálorico diário é de {tmt:.2f}kcal por dia')
objetivo = int(input('Seu objetivo é ganhar massa ou perder gordura? \nDigite 1 para ganhar massa e 2 para perder gordura: '))
if objetivo == 1:
    ganhar = tmt + 400
    print(f'{nome} para ganhar massa muscular você precisa fazer um superávit cálorico, você gasta {tmt:.2f}kcal e precisa consumir {ganhar:.2f}kcal por dia')
    print('O superávit cálorico consiste em consumir mais kcal do que o corpo gasta e por consequência faz você ganhar massa muscular')
    print('Agora iremos calcular seus macronutrientes')
    proteina = peso * 2
    print(f'{nome} seu consumo diário de proteína deve ser de {proteina}g')
    gordura = peso * 1
    print(f'{nome} seu consumo diário de gordura deve ser de {gordura}g')
    kcal = ganhar - ((proteina * 4) + (gordura * 9 ))  
    carbo = kcal / 4 
    print(f'{nome} seu consumo diário de carboidratos deve ser de {carbo}g')
else:
    perder = tmt - 400
    print(f'{nome} para perder gordura você precisa fazer um défict cálorico, você gasta {tmt:.2f}kcal e precisa consumir {perder:.2f}kcal por dia')
    print('O défict cálorico consiste em cosumir menos kcal do que o corpo gasta e por consequência faz você perder gordura')
    print('Agora iremos calcular seus macronutrientes')
    proteina = peso * 2
    print(f'{nome} seu consumo diário de proteína deve ser de {proteina:.2f}g')
    gordura = peso * 1
    print(f'{nome} seu consumo diário de gordura deve ser de {gordura:.2f}g')
    kcal = perder - ((proteina * 4) + (gordura * 9 ))
    carbo = kcal / 4 
    print(f'{nome} seu consumo diário de carboidratos deve ser de {carbo:.2f}g')