# Faça um procedimento que receba o IMC de uma pessoa e a classifique segundo a tabela abaixo


def classifica_imc(imc):
    # Verifica a condição e imprime a classificação correspondente
    if imc < 18.5:
        print(f"\nIMC: {imc:.2f} -> Abaixo do Peso")
    elif imc <= 25.0:  # Como já passou pelo 'if' anterior, cobre de 18.5 até 25
        print(f"\nIMC: {imc:.2f} -> Peso Normal")
    elif imc <= 30.0:  # Cobre valores acima de 25 até 30
        print(f"\nIMC: {imc:.2f} -> Acima do Peso")
    else:  # Valores maiores que 30
        print(f"\nIMC: {imc:.2f} -> Obeso")


# Programa principal para testar o procedimento
def main():
    print("--- CLASSIFICAÇÃO DE IMC ---")
    imc_usuario = float(input("Digite o valor do IMC da pessoa: "))
    
    # Chamando o procedimento passando o IMC como parâmetro
    classifica_imc(imc_usuario)


# Executa o programa
if __name__ == "__main__":
    main()