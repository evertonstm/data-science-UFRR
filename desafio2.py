idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 18:
    print("jovem")
elif idade >= 19 and idade <= 24:
    print("Jovem")
elif idade >= 25 and idade <= 40:
    print("Adulto")
elif idade >= 41 and idade <= 60:
    print("Meia Idade")
elif idade > 60:
    print("Idoso")