# 2. Faça uma função que recebe dois valores e retorna o menor.

def valores(numero1,numero2):
    if numero2 < numero1:
        return numero2
    elif numero1 < numero2:
        return numero1
    else:
        return "Os numeros são iguais" 