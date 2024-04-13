<h1 align="center">
 💡 Melhorando Sistema Bancário com Python
 
</h1>
  


## Melhorias

- **Tratamento de exceções:** Adicionei tratamento de exceções para lidar com possíveis erros de entrada do usuário, como inserir uma letra em vez de um número ao solicitar um valor.
- **Refatoração de código:** Evitei as repetições de código, especialmente ao exibir mensagens de erro.
- **Melhoria na legibilidade:** Usei constantes em maiúsculas para os valores que não mudam, para tornar o código mais legível e fácil de manter.
- **Adição de comentários:** Adicionei comentários para explicar o que cada parte do código faz, especialmente se for complexo.

## Explicando...

**Classe ContaBancaria:**

- Esta classe representa uma conta bancária individual.
- No método __init__, inicializamos os atributos da conta, como nome do titular, saldo inicial e número de conta único, gerado através da biblioteca uuid.
- Os métodos deposito, saque e saldo_disponivel permitem realizar operações comuns em uma conta bancária, como depósito, saque e verificação de saldo.

**Classe Banco:**

- Esta classe gerencia várias contas bancárias.
- No método __init__, inicializamos um dicionário vazio para armazenar as contas bancárias.
- O método criar_conta permite criar uma nova conta bancária e armazená-la no dicionário de contas do banco.
- O método obter_conta permite obter uma conta bancária com base no número da conta.
- O método realizar_transferencia permite transferir fundos entre duas contas bancárias diferentes.

**Teste do sistema:**

- Criamos uma instância da classe Banco.
- Utilizamos o método criar_conta para criar duas contas bancárias de teste para "Fulano" e "Ciclano".
- Em seguida, obtivemos referências às contas de "Fulano" e "Ciclano" usando o método obter_conta.
- Finalmente, testamos o método realizar_transferencia transferindo fundos da conta de "Fulano" para a conta de "Ciclano".

**Modelando o Sistema Bancário em POO com Python:**

A classe **BancoDados** é usada para simular o banco de dados de contas bancárias. As contas são armazenadas em um dicionário, onde a chave é o número da conta e o valor é a instância da classe ContaBancaria. As operações de criação de conta, obtenção de conta e realização de transferência são adaptadas para interagir com esse banco de dados simulado.


<br />


<p align="left">
  <a href="https://github.com/MirkaJuliet34"><img alt="Youtube" title="Youtube" src="https://img.shields.io/badge/-GitHub-red?style=for-the-badge&logo=github&logoColor=white"/></a>
  <a href="https://www.linkedin.com/in/mirka-juliet-9bb590148/"><img alt="Twitter" title="Twitter" src="https://img.shields.io/badge/-Linkedin-1DA1F2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
</p>


