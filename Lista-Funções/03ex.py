# 3. Faça uma função que recebe três valores e retorna o menor. 

def menor_valor(n1, n2,n3):
    if n1 <= n2 and n1 <= n3:
        return n1
    elif n2 <= n1 and n2 <= n3:
        return n2
    else:
        return n3

def menor_de_tres(n1,n2,n3):
    return min(n1,n2,n3)