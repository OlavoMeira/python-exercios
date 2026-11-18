def pagamento_a_vista(total):
    valor_final = total * 0.90
    print(f"\nPagamento à vista com 10% de desconto.")
    print(f"Valor total a pagar: R$ {valor_final:.2f}")


def pagamento_duas_vezes(total):
    valor_parcela = total / 2
    print(f"\nParcelado em 2x (preço da etiqueta).")
    print(f"2 parcelas de R$ {valor_parcela:.2f} | Total: R$ {total:.2f}")

def pagamento_juros(total):
    if total > 100.00:
        parcelas = int(input("Digite a quantidade de vezes (de 3 a 10): "))
        
        if 3 <= parcelas <= 10:
            taxa_juros = 0.03
            valor_total = total * ((1 + taxa_juros) ** parcelas)
            valor_parcela = valor_total / parcelas
            
            print(f"\nParcelado em {parcelas}x com 3% de juros ao mês.")
            print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
            print(f"Valor total com juros: R$ {valor_total:.2f}")
        else:
            print("Erro: A quantidade de parcelas deve ser entre 3 e 10.")
    else:
        print("\nErro: Opção disponível apenas para compras acima de R$ 100,00.")


def menu_pagamento(total):
    print("\n" + "=" * 30)
    print("FORMA DE PAGAMENTO")
    print("=" * 30)
    print("a) À vista com 10% de desconto")
    print("b) Em duas vezes (preço da etiqueta)")
    
    
    if total > 100.00:
        print("c) De 3 até 10 vezes com 3% de juros ao mês")
    
    opcao = input("Escolha a opção desejada (a, b ou c): ").strip().lower()
    return opcao


def main():
    total = 0  

    while True:
        print("=" * 30)
        print("WELCOME TO MY SHOP")
        print("=" * 30)
        print(f"Carrinho atual: R$ {total:.2f}\n")
        
        print("1 - Shirt $40")
        print("2 - Pants $70")
        print("3 - Shoes $100")
        print("4 - Terminar compra (Ir para pagamento)")
        print("0 - Sair da loja")

        produto = int(input("Digite o número de 0 a 4: "))

        if produto == 0:
            print("Saindo da loja. Até logo!")
            break
            
        elif produto == 1:
            total += 40
            print("-> Shirt adicionada!\n")
            
        elif produto == 2:
            total += 70
            print("-> Pants adicionadas!\n")
            
        elif produto == 3:
            total += 100
            print("-> Shoes adicionados!\n")
            
        elif produto == 4:
            if total > 0:
                
                escolha = menu_pagamento(total)

                
                if escolha == 'a':
                    pagamento_a_vista(total)
                elif escolha == 'b':
                    pagamento_duas_vezes(total)
                elif escolha == 'c':
                    pagamento_juros(total)
                else:
                    print("\nOpção de pagamento inválida!")
                
                break  
            else:
                print("\nSeu carrinho está vazio! Adicione algum produto antes de pagar.\n")
                
        else:
            print("Opção inválida! Escolha entre 0, 1, 2, 3 e 4.\n")

if __name__ == "__main__":
    main()