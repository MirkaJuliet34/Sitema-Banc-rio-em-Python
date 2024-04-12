menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    try:
        opcao = input(menu).strip().lower()  # Remover espaços em branco e converter para minúsculas

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            if valor <= 0:
                raise ValueError("Valor do depósito deve ser maior que zero.")
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            if valor <= 0:
                raise ValueError("Valor do saque deve ser maior que zero.")
            
            if valor > saldo:
                raise ValueError("Operação falhou! Você não tem saldo suficiente.")
            
            if valor > limite:
                raise ValueError("Operação falhou! O valor do saque excede o limite.")
            
            if numero_saques >= LIMITE_SAQUES:
                raise ValueError("Operação falhou! Número máximo de saques excedido.")

            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
