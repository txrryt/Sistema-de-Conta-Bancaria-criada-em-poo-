# Sistema de Conta Bancária em POO (Python)

Este projeto é um sistema simples de banco desenvolvido em **Python**, utilizando os conceitos de **Programação Orientada a Objetos (POO)**. Feito como uma atividade avaliativa aplicada pelo professor Glestiano

## Funcionalidades do sistema

* Cadastro de cliente
* Criação de conta corrente
* Depósito de valores
* Saque com verificação de saldo e limite
* Consulta de saldo
* Listagem de contas criadas
* Menu interativo no terminal

---

## Conceitos utilizados

* Classes e Objetos
* Herança
* Encapsulamento
* Métodos especiais (`__init__`, `__str__`)
* Estruturas de repetição (`while`)
* Condicionais (`if/else`)

---

## Estrutura do código

### Classe Cliente

Responsável por armazenar os dados do cliente:

* Nome
* CPF

---

### Classe Conta

Classe base para contas bancárias:

* Número da conta
* Cliente vinculado
* Saldo

**Métodos:**

* `depositar()`
* `sacar()`
* `exibir_saldo()`

---

### Classe ContaCorrente

Herda de `Conta` e adiciona:

* Limite extra para saque

---

### Classe Banco

Gerencia todo o sistema:

* Lista de clientes
* Lista de contas
* Criação de contas
* Cadastro de clientes

---

## Executar: como?

1. Certifique-se de ter o Python instalado
2. Salve o arquivo com extensão `.py`
3. Execute no terminal:

```bash
python nome_do_arquivo.py
```

---

## Exemplo de uso do sistema

```
Nome do cliente: João
CPF do cliente: 12345678900

--- MENU ---
1 - Depositar
2 - Sacar
3 - Ver saldo
4 - Listar contas
5 - Sair
```

---

## Observações

* O sistema é simples e não utiliza banco de dados (dados ficam apenas em memória)
* Não há validação avançada de CPF

---

## Possíveis melhorias

* Implementar validação de CPF
* Criar interface gráfica
* Salvar dados em arquivo ou banco de dados
* Adicionar conta poupança
* Sistema de login

---

*

Projeto desenvolvido para estudo de **Programação Orientada a Objetos em Python**.
