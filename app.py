menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar
[5] Listar Contas
[6] Sair
=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios={}
contas_correntes={}

def deposito(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def saque(saldo=saldo, extrato=extrato, numero_saques=numero_saques, limite=limite, LIMITE_SAQUES=LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo=saldo, extrato=extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(nome,data_nascimento,cpf,endereco):
    if cpf in usuarios:
        print("Usuario já cadastrado com esse cpf")
    else: 
        usuarios[cpf]={'nome':nome,'data_nascimento':data_nascimento,'cpf':cpf,'endereco':endereco}
        print(f"Usuário {nome} criado com sucesso.")
   
def criar_conta_corrente(cpf):     
     if cpf not in usuarios:
        print("Usuário não encontrado.")
     else:
        # Gerar um número de conta sequencial baseado na quantidade de contas do usuário
        numero_conta = len([conta for conta in contas_correntes if conta.startswith(cpf)]) + 1
        conta_id = f"{cpf}-{numero_conta}"
        contas_correntes[conta_id] = {'cpf':cpf}
        
def exibir_contas():
    for conta_id, detalhes in contas_correntes.items():
        cpf = detalhes['cpf']
        nome_usuario = usuarios[cpf]['nome']
        print(f"Conta: {conta_id}, Usuário: {nome_usuario}, Saldo: {saldo}")
while True:
    opcao = input(menu)

    if opcao == "1":
        saldo, extrato = deposito(saldo, extrato)
    elif opcao == "2":
        saldo, extrato, numero_saques = saque(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)
    elif opcao == "3":
        exibir_extrato(saldo, extrato)
    elif opcao =="4":
        
        cpf=input("Digite seu cpf : ")
        nome =input("Digite seu nome completo : ")
        data_nascimento=input("Sua data de nascimento : ")
        endereco=input("Informe seu endereço : "  )
        
        criar_usuario(nome,data_nascimento,cpf,endereco)
        criar_conta_corrente(cpf=cpf)
    elif opcao == "5":
         exibir_contas()
    elif opcao == "6":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
