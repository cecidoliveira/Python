def menu():
    menu = """
         ======= MENU =======
        | [d] Depositar      |
        |--------------------|
        | [s] Sacar          |
        |--------------------|
        | [e] Extrato        |
        |--------------------|
        | [c] Criar Conta    |
        |--------------------|
        | [l] Listar Contas  |
        |--------------------|
        | [u] Criar Usuário  |
        |--------------------|
        | [q] Sair           |
         ====================
    >> """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    # verificar se o valor e negativo ou não
    if valor > 0:
        saldo += valor
        extrato += f"deposito: R$ {valor:.2f}\n"
        print("operação realizada!")
        return saldo, extrato
    else:
        print("operação falhou! o valor informado não é valido")

def sacar(*, saldo, valor, extrato, limite, num_saques, max_saques):
    # condições para que o saldo seja realizado
    if valor > limite:
        print("operação falhou! o valor excede o limite maximo por saque que é de 500")
    elif valor > saldo:
        print("operação falhou! Sem saldo suficiente...")
    elif num_saques >= max_saques:
        print("operação falhou! Numero maximo de saques diarios ja atingido")

    # realiza o saque
    elif valor > 0:
        saldo -= valor
        extrato += f"saque: R${valor:.2f}\n"
        num_saques += 1
        print("operação realizada!")

    else:
        print("operação falhou! o valor informado não é valido")

    return saldo, extrato

def exibirExtrato(saldo, /, *, extrato):
    print("\n========== extrato ==========\n")
    print("Não foram realizadas movimentações..." if not extrato else extrato)
    print("\n-----------------------------")
    print(f"saldo: {saldo:.2f}")
    print("=============================\n")

def criarUser(users):
    try:
        cpf = int(input("informe o seu cpf (somente numeros):"))
    except ValueError:
        print("operação falhou! o valor informado não é valido")
        main()
        
    user = filtrarUser(cpf, users)

    if user:
        print("usuario já existe com o cpf informado!")

    else:
        nome = input("informe seu nome completo: ")
        dt_nascimento = input("informe sua data de nascimento (dd-mm-aaaa): ")
        endereco = input("informe o endereço (logradouro,nro - bairro - cidade/sigla estado): ")

        users.append({"nome": nome, "data_nascimento": dt_nascimento, "cpf": cpf, "endereco":endereco})
        print("usuario criado com sucesso!")

def filtrarUser(cpf, users):
    users_filtrados = [user for user in users if user["cpf"] == cpf]
    return users_filtrados[0] if users_filtrados else None

def listContas(contas):
    for conta in contas:
        linha = f"""
         =============================================
        |Agencia: {conta['agencia']}
        |Conta/corrente: {conta['numero_conta']}
        |Titular: {conta['user']['nome']}
         =============================================
        
        """
        print(linha)
def criarConta(agencia, num_conta, users):
    cpf = input("informe o cpf do usuario: ")
    user = filtrarUser(cpf, users)

    if user:
        print("conta foi criada!")
        return {"agencia": agencia, "numero_conta": num_conta, "user": user}
    else:
        print("operação falhou! o usuario não foi encontrado, crie um usuario antes de criar uma conta.")

def main():
    max_saques = 3
    agencia = "0001"
    limite = 500

    saldo = 0
    extrato = ""
    num_saques = 0
    num_conta = 1
    users = []
    contas = []

    while True:
        opc = menu()

        if opc.lower() == "d":
            valor = float(input("informe o valor do deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opc.lower() == "s":
            valor = float(input("informe o valor para o saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                num_saques=num_saques,
                max_saques=max_saques)

        elif opc.lower() == "e":
            exibirExtrato(saldo, extrato=extrato)

        elif opc.lower() == "u":
            criarUser(users)

        elif opc.lower() == "c":
            conta = criarConta(agencia, num_conta, users)

            if conta:
                contas.append(conta)
                num_conta += 1

        elif opc.lower() == "l":
            listContas(contas)

        elif opc.lower() == "q":
            exit()
        else:
            print("operação invalida! selecione uma das opções informadas.")

main()