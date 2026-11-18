'''
7. Escreva um procedimento que recebe as 3 notas de um aluno por parâmetro e uma letra. Se a letra for 
A  o  procedimento  calcula  a  média  aritmética  das  notas  do  aluno  e  se  for P,  a  sua  média  ponderada 
(pesos: 5, 3 e 2). O procedimento deve imprimir a resposta. 
'''

def main():
    print("--- CÁLCULO DE MÉDIAS ---")
    n1 = float(input("Digite a 1 nota: "))
    n2 = float(input("Digite a 2 nota: "))
    n3 = float(input("Digite a 3 nota: "))
    
    letra = input("Digite 'A' para média aritmética ou 'P' para ponderada: ")
    
    
    calcula_media(n1, n2, n3, letra)


def calcula_media(nota1, nota2, nota3, tipo):
    
    tipo = tipo.upper()
    
    if tipo == 'A':
        
        media = (nota1 + nota2 + nota3) / 3
        print(f"\nMédia Aritmética: {media:.2f}")
        
    elif tipo == 'P':

        soma_pesos = 5 + 3 + 2
        media = (nota1 * 5 + nota2 * 3 + nota3 * 2) / soma_pesos
        print(f"\nMédia Ponderada: {media:.2f}")
        
    else:
        print("\nLetra inválida! Use 'A' para aritmética ou 'P' para ponderada.")

if __name__ == "__main__":
    main()