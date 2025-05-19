# calculadora de comsumo de combustivel

# solicite o nome do usuario
nome = input("olá qual o seu nome? ")

# entrada de dados
distancia = float(input("informe a distancia percorrida em (km): "))
litros = float(input("informe a quantidade de combustivel que foi gasto (em litros)"))

# calculo de comsumo médio
comsumo_médio = distancia / litros 

# exibe o resultado de duas casas decimais
print(f"\n {nome}, o comsumo médio do seu veiculo foi de {comsumo_médio:.2f} km/1.")

# CLASSIFICAÇÃO COM BASA NO COMSUMO
if comsumo_médio < 8.0:
   print("classificação: alto comsumo ")
   print('recomenda-se verificar o motor ou calibrar os pneus. ')
elif 8.0 <= comsumo_médio <= 12.0:
    print("Classificação: Consumo moderado ⚠️")
else:
    print("Classificação: Econômico! 🚗💨")

