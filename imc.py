def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) com base no peso (em kg) e altura (em metros).
    Retorna o valor do IMC.
    """
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    """
    Classifica o IMC em uma faixa específica e retorna uma mensagem correspondente.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade grau 1"
    elif 35 <= imc < 40:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

def main():
    peso = float(input("Digite seu peso (em kg): "))
    altura = float(input("Digite sua altura (em metros): "))

    imc = calcular_imc(peso, altura)
    print("Seu IMC é:", imc)
    print("Você está na faixa de:", classificar_imc(imc))

if __name__ == "__main__":
    main()
