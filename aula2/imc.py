# Solicitar ao usuário que insira o peso e a altura
peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

# Calcular o IMC
imc = peso / (altura ** 2)

# Imprimir o IMC
print("Seu IMC é:", imc)

# Determinar e imprimir a faixa do IMC
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Seu peso está normal.")
elif imc < 30:
    print("Você está com sobrepeso.")
elif imc < 35:
    print("Você está com obesidade Grau I.")
elif imc < 40:
    print("Você está com obesidade Grau II (severa).")
else:
    print("Você está com obesidade Grau III (mórbida).")