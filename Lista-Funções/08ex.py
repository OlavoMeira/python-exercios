# Faça um procedimento que receba o IMC de uma pessoa e a classifique segundo a tabela abaixo


def classifica_imc(imc):
    
    if imc < 18.5:
        print(f"\nIMC: {imc:.2f} -> Abaixo do Peso")
    elif imc <= 25.0:  
        print(f"\nIMC: {imc:.2f} -> Peso Normal")
    elif imc <= 30.0:  
        print(f"\nIMC: {imc:.2f} -> Acima do Peso")
    else:  
        print(f"\nIMC: {imc:.2f} -> Obeso")



def main():
    print("--- CLASSIFICAÇÃO DE IMC ---")
    imc_usuario = float(input("Digite o valor do IMC da pessoa: "))
    
    
    classifica_imc(imc_usuario)



if __name__ == "__main__":
    main()