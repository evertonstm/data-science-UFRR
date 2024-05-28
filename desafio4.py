notas = [7, 8, 9, 10, 15, 74, 52, 100, 58, 60]
def calcular_media(notas):
    soma=sum(notas)
    media=soma/len(notas)
    print("Media",media)
    print("Soma",soma)
    return media

calcular_media(notas)
