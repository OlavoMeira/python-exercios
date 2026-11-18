'''
. Escreva  um  procedimento  que  recebes  3  valores  reais  X,  Y  e  Z  e  que  verifique  se  esses  valores 
podem ser os comprimentos dos lados de um triângulo e, neste caso, retornar qual o tipo de triângulo 
formado.  Para  que  X,  Y  e  Z  formem  um  triângulo  é  necessário  que  a  seguinte  propriedade  seja 
satisfeita: o comprimento de cada lado de um triângulo é menor do que a soma do comprimento dos 
outros  dois  lados.  O  procedimento  deve  identificar  o  tipo  de  triângulo  formado  observando  as 
seguintes definições: 
a. Triângulo Equilátero: os comprimentos dos 3 lados são iguais. 
b. Triângulo Isósceles: os comprimentos de 2 lados são iguais. 
c. Triângulo Escaleno: os comprimentos dos 3 lados são diferentes.

'''

def verifica_triangulo(x, y, z):
   
    if (x < y + z) and (y < x + z) and (z < x + y):
        print("\nOs valores formam um triângulo!")
        
        
        if x == y and y == z:
            print("Tipo: Triângulo Equilátero (3 lados iguais)")
        elif x == y or x == z or y == z:
            print("Tipo: Triângulo Isósceles (2 lados iguais)")
        else:
            print("Tipo: Triângulo Escaleno (3 lados diferentes)")
            
    else:
        print("\nOs valores informados NÃO podem formar um triângulo.")



def main():
    print("--- VERIFICADOR DE TRIÂNGULOS ---")
    x = float(input("Digite o valor de X: "))
    y = float(input("Digite o valor de Y: "))
    z = float(input("Digite o valor de Z: "))
    
   
    verifica_triangulo(x, y, z)


# Executa o programa
if __name__ == "__main__":
    main()