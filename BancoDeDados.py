import uuid

class ContaBancaria:
    def __init__(self, nome, saldo_inicial=0):
        self.nome = nome
        self.saldo = saldo_inicial
        self.numero_conta = uuid.uuid4().hex  # Gerar um número de conta único
    
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor} realizado. Saldo atual: R${self.saldo}')
        else:
            print("O valor do depósito deve ser maior que zero.")
    
    def saque(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado. Saldo atual: R${self.saldo}')
        else:
            print("Saldo insuficiente para realizar o saque ou valor inválido.")
    
    def saldo_disponivel(self):
        print(f'Saldo disponível: R${self.saldo}')

class BancoDados:
    def __init__(self):
        self.contas = {}  # Dicionário para armazenar as contas
    
    def criar_conta(self, nome, saldo_inicial=0):
        nova_conta = ContaBancaria(nome, saldo_inicial)
        self.contas[nova_conta.numero_conta] = nova_conta
        print(f'Conta criada para {nome} com sucesso. Número da conta: {nova_conta.numero_conta}')
    
    def obter_conta(self, numero_conta):
        return self.contas.get(numero_conta)
    
    def realizar_transferencia(self, conta_origem, conta_destino, valor):
        if conta_origem.saldo >= valor:
            conta_origem.saque(valor)
            conta_destino.deposito(valor)
            print("Transferência realizada com sucesso.")
        else:
            print("Saldo insuficiente para realizar a transferência.")

# Testando o funcionamento do sistema com o banco de dados
banco_dados = BancoDados()
banco_dados.criar_conta("Fulano", 1000)
banco_dados.criar_conta("Ciclano", 500)

conta_fulano = banco_dados.obter_conta("Número da conta de Fulano")  # Você precisará do número real da conta
conta_ciclano = banco_dados.obter_conta("Número da conta de Ciclano")  # Você precisará do número real da conta

banco_dados.realizar_transferencia(conta_fulano, conta_ciclano, 200)
