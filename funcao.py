def soma():
      
    n1=float(input("Digite um numero: "))
    n2=float(input("Digite um numero: "))
    soma=n1+n2
    print(f"Resultado é {soma}")

def multiplicacao():
    n1=float(input("Digite um numero: "))
    n2=float(input("Digite um numero: "))
    multi=n1*n2
    print(f"Resultado é {multi}")

def subtracao():
    n1=float(input("Digite um numero: "))
    n2=float(input("Digite um numero: "))
    sub=n1-n2
    print(f"Resultado é {sub}")

def divisao():
    n1=float(input("Digite um numero: "))
    n2=float(input("Digite um numero: "))
    div=n1/n2
    print(f"Resultado é {div}")

def menu():
    while True:
        print("Escolha uma operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")
        
        escolha = input("Digite o número da operação desejada: ")
        
        if escolha == '1':
            soma()
        elif escolha == '2':
            subtracao()
        elif escolha == '3':
            multiplicacao()
        elif escolha == '4':
            divisao()
        elif escolha == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
