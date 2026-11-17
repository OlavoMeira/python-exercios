'''
5. Faça um programa que apresente um menu de opções: 1 para somar, 2 para subtrair e 3 para dividir. 
No  caso  da  divisão  verifique  a  condição  de  erro,  divisão  por  zero.  Faça  uma  função  para  cada 
operação.
'''

def main():
    while True:
        print("=" * 30)
        print("BEM-VINDO AO MEU PROGRAMA")
        print("=" * 30)

        print("1- Somar ")
        print("2- Subtrair ")
        print("3- Dividir ")
        print("0- Sair do programa")
        numero = int(input("Digite o numero: "))
        print()
        
        if numero == 0:
            print("Saindo do programa. Até logo!!!")
            break
        elif numero == 1:
            print("Digite os numeros")
            soma_numero_1 = float(input("Numero1: "))
            soma_numero_2 = float(input("Numero2: "))
            print(f"Resultado: {somar(soma_numero_1, soma_numero_2)}\n")
        elif numero == 2:
            print("Digite os numeros")
            subtrair_numero_1 = float(input("Numero1: "))
            subtrair_numero_2 = float(input("Numero2: "))
            print(f"Resultado: {subtrair(subtrair_numero_1, subtrair_numero_2)}\n")
        elif numero == 3:
            print("Digite os numeros")
            dividir_numero_1 = float(input("Numero1: "))
            dividir_numero_2 = float(input("Numero2: "))
            print(f"Resultado: {dividir(dividir_numero_1, dividir_numero_2)}\n")
        else:
            print("Opção inválida! Por favor, escolha entre 0, 1, 2 ou 3.\n")

    
    

def somar(n1,n2):
    return n1 + n2

def subtrair(n1,n2):
    return n1 - n2

def dividir(n1,n2):
    if n2 == 0:
        return "A divisão por zero não é definida."
    else:
        return n1 / n2



if __name__ == "__main__":
    main()