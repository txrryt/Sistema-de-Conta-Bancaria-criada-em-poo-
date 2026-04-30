# Fazer um sistema de banco com cadastro

# começando com uma classe cliente
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome  
        self.cpf = cpf    

    # aq so para exibir o cliente
    def __str__(self):
        return f"Cliente: {self.nome} | CPF: {self.cpf}"


# classe sendo base para contas bancárias
class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero      # número da conta como um id
        self.cliente = cliente    
        self.saldo = 0.0          


    def depositar(self, valor):
        if valor > 0:  
            self.saldo += valor  
            print(f"Depósito de R${valor:.2f} realizado.")
        else:
            print("Valor inválido.")

    
    def sacar(self, valor):
        if valor <= 0:  
            print("Valor inválido.")
        elif valor > self.saldo: 
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor 
            print(f"Saque de R${valor:.2f} realizado.")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

    # mostrar conta tb igual 
    def __str__(self):
        return f"Conta {self.numero} | {self.cliente.nome}"


# classe contacorrente herdando da classe conta
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500):
        super().__init__(numero, cliente)  # serve para nao repetir tudo novamente
        self.limite = limite              

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
        elif valor <= (self.saldo + self.limite):  #(caso ele ter o limite extra em conta poder sacar também)
            self.saldo -= valor
            print(f"Saque (CC) de R${valor:.2f} realizado.")
        else:
            print("Limite excedido.")


# aqui a classe banco para gerenciar os (clientes e contas)
class Banco:
    def __init__(self):
        self.clientes = []       # lista para clientes cadastrados
        self.contas = []         # lista para contas criadas
        self.numero_conta = 1    # contador para as contas

#cadastro
    def cadastrar_cliente(self, nome, cpf):
        cliente = Cliente(nome, cpf)  # cria um objeto Cliente
        self.clientes.append(cliente) # adiciona na lista
        print("Cliente cadastrado.")
        return cliente

#contacorrente
    def criar_conta_corrente(self, cliente):
        conta = ContaCorrente(self.numero_conta, cliente)  # cria conta
        self.contas.append(conta)  # adiciona na lista de contas
        self.numero_conta += 1     # incrementa o número da próxima conta
        print("Conta corrente criada.")
        return conta

#mostrar as contas criadas
    def listar_contas(self):
        for conta in self.contas:
            print(conta)



# criar o banco para usarmos (objeto)
banco = Banco()

# entrada de dados do usuário
nome = input("Nome do cliente: ")
cpf = input("CPF do cliente: ")

# cadastra cliente e cria conta
cliente = banco.cadastrar_cliente(nome, cpf)
conta = banco.criar_conta_corrente(cliente)

# menu simples para executar as funções criadas
while True:
    print("\n--- MENU ---")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Listar contas")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        valor = float(input("Valor do depósito: "))
        conta.depositar(valor)  

    elif opcao == "2":
        valor = float(input("Valor do saque: "))
        conta.sacar(valor)

    elif opcao == "3":
        conta.exibir_saldo()

    elif opcao == "4":
        banco.listar_contas()

    elif opcao == "5":
        print("Saindo...")
        break  # encerra o sistema aq

    else:
        print("Opção inválida.")