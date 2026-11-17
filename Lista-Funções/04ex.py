''' 4. Criar  uma  função  que  receba  um  caractere  como  parâmetro  e  retorne  1  (um)  caso  seja  uma 
vogal e zero caso não seja. '''

def vogal(caractere):

    caractere = caractere.lower()

    if caractere in "aeiou":
        return 1
    else:
        return 0
    