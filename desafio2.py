import uuid

class ContaBancaria:
    def __init__(self, nome, saldo_inicial=0):
        """
        Inicializa uma conta bancária com um nome, saldo inicial e número de conta único.
        """
        self.nome = nome
        self._saldo = saldo_inicial
        self.numero_conta = uuid.uuid4().hex  # Gerar um número de conta único
    
    def deposito(self, valor):
        """
        Realiza um depósito na conta bancária.
        """
        if valor > 0:
            self._saldo += valor
            print(f'Depósito de R${valor} realizado. Saldo atual: R${self._saldo}')
        else:
            print("O valor do depósito deve ser maior que zero.")
    
    def saque(self, valor):
        """
        Realiza um saque na conta bancária.
        """
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f'Saque de R${valor} realizado. Saldo atual: R${self._saldo}')
        else:
            print("Saldo insuficiente para realizar o saque ou valor inválido.")
    
    def saldo_disponivel(self):
        """
        Retorna o saldo disponível na conta bancária.
        """
        print(f'Saldo disponível: R${self._saldo}')


class Banco:
    def __init__(self):
        """
        Inicializa um banco com um dicionário vazio para armazenar as contas.
        """
        self._contas = {}
    
    def criar_conta(self, nome, saldo_inicial=0):
        """
        Cria uma nova conta bancária e a adiciona ao banco.
        """
        nova_conta = ContaBancaria(nome, saldo_inicial)
        self._contas[nova_conta.numero_conta] = nova_conta
        print(f'Conta criada para {nome} com sucesso. Número da conta: {nova_conta.numero_conta}')
    
    def obter_conta(self, numero_conta):
        """
        Retorna a conta bancária correspondente ao número da conta fornecido.
        """
        return self._contas.get(numero_conta)
    
    def realizar_transferencia(self, conta_origem, conta_destino, valor):
        """
        Realiza uma transferência entre duas contas bancárias.
        """
        if valor <= 0:
            print("O valor da transferência deve ser maior que zero.")
            return
        
        if not conta_origem or not conta_destino:
            print("Conta de origem ou conta de destino inválida.")
            return
        
        if conta_origem._saldo < valor:
            print("Saldo insuficiente para realizar a transferência.")
            return
        
        conta_origem.saque(valor)
        conta_destino.deposito(valor)
        print("Transferência realizada com sucesso.")

# Testando o funcionamento do sistema com o banco de dados
banco = Banco()
banco.criar_conta("Fulano", 1000)
banco.criar_conta("Ciclano", 500)

conta_fulano = banco.obter_conta("Número da conta de Fulano")  # Você precisará do número real da conta
conta_ciclano = banco.obter_conta("Número da conta de Ciclano")  # Você precisará do número real da conta

banco.realizar_transferencia(conta_fulano, conta_ciclano, 200)
