menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
=> """

#variaveis
saldo = 0
limite = 500
extrato = ""
numeroSaques = 0
limiteSaques = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do deposito: "))

        # verificar se o valor e negativo ou não
        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f}\n"

        else:
            print("operação falhou! o valor informado não é valido")

    elif opcao == "s":
        valor = float(input("informe o valor para o saque: "))

        #verificar se o valor e negativo ou não
        if valor > 0:
            #condições para que o saldo seja realizado
            if valor > limite:
                print("operação falhou! o valor excede o limite maximo por saque que é de 500")
            elif valor > saldo:
                print("operação falhou! Sem saldo suficiente...")
            elif numeroSaques >= limiteSaques:
                print("operação falhou! Numero maximo de saques diarios ja atingido")

            #realiza o saque
            else:
                saldo -= valor
                extrato += f"saque: R${valor:.2f}\n"
                numeroSaques += 1

        else:
            print("operação falhou! o valor informado não é valido")

    elif opcao == "e":
        print("\n========== extrato ==========\n")
        print("Não foram realizadas movimentações..." if not extrato else extrato)
        print("\n-----------------------------")
        print(f"saldo: {saldo:.2f}")
        print("=============================\n")

    elif opcao == "q":
        break

    else:
        print("operação invalida! selecione uma das opções informadas.")