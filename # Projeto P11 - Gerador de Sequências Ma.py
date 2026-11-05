# Projeto P11 - Gerador de Sequências Matemáticas
# Aluno: Eitor Gabriel da Silva

def fibonacci(n):
    sequencia = []
    a = 0
    b = 1

    for i in range(n):
        sequencia.append(a)

        proximo = a + b
        a = b
        b = proximo

    return sequencia

def eh_primo(numero):
    if numero < 2:
        return False

    primo = True

    for divisor in range(2, numero):
        if numero % divisor == 0:
            primo = False
            break

    return primo

def primos_ate(n):
    primos = []

    for numero in range(2, n + 1):
        if eh_primo(numero):
            primos.append(numero)

    return primos

def tabuada(n):
    resultados = []

    for multiplicador in range(1, 11):
        resultado = n * multiplicador
        resultados.append(resultado)

    return resultados

def somar_lista(lista):
    total = 0

    for numero in lista:
        total = total + numero

    return total

def media_lista(lista):
    # se for vazia não tem média
    if len(lista) == 0:
        return None

    return somar_lista(lista) / len(lista)

def adicionar_historico(historico, sequencia):
    # Add sequência à lista recebida
    historico.append(sequencia)

historico = []

while True:
    print("\nGERADOR DE SEQUÊNCIAS")
    print("1 - Fibonacci")
    print("2 - Números primos")
    print("3 - Tabuada")
    print("4 - Ver histórico")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Programa encerrado.")
        break

    elif opcao == "4":
        if len(historico) == 0:
            print("O histórico está vazio.")
        else:
            for sequencia in historico:
                print(sequencia)

    elif opcao == "1" or opcao == "2" or opcao == "3":
        if opcao == "1":
            entrada = input("Quantos termos de Fibonacci? ")
        elif opcao == "2":
            entrada = input("Mostrar primos até qual número? ")
        else:
            entrada = input("Tabuada de qual número? ")

        # Conta os dígito
        digitos = 0

        for caractere in entrada:
            if caractere in "0123456789":
                digitos = digitos + 1

        # A entrada so pode ter dígitos e não ser vazia
        if len(entrada) > 0 and digitos == len(entrada):
            n = int(entrada)

            if n == 0:
                print("Digite um número inteiro maior que zero.")

            else:
                if opcao == "1":
                    lista = fibonacci(n)
                elif opcao == "2":
                    lista = primos_ate(n)
                else:
                    lista = tabuada(n)

                if len(lista) == 0:
                    print("Não foram encontrados números primos.")
                    print("A lista está vazia; não há média.")

                else:
                    if opcao == "3":
                        for i in range(len(lista)):
                            print(n, "x", i + 1, "=", lista[i])
                    else:
                        print("Sequência:", lista)

                    print("Soma:", somar_lista(lista))
                    print("Média:", media_lista(lista))

                    adicionar_historico(historico, lista)

        else:
            print("Entrada inválida. Digite um inteiro positivo.")

    else:
        print("Opção inválida.")
