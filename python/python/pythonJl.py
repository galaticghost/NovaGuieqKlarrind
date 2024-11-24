def solicitacao(lista):
    

    print()
    print(lista)

protocolo = 1
solicitacoes = []
x = 1
y = 1
z = 1
w = 1
while True:
    lista = []
    solicitacao(lista)
    solicitacoes.append(lista)
    protocolo += 1
    x = int(input('\nDeseja continuar inserindo demandas de manuteção? (Digite 0 para parar ou 1 para continuar) '))
    if x==0:
        break
print()
while y!=0:
    nmr = int(input('\nDigite o número do protocolo da solicitação que deve ser acessada (Digite 0 para parar): '))
    if nmr == 0:
        break
    elif solicitacoes[nmr-1][5] == 'Situação: Em atendimento':
        print('A solicitação já está sendo atendida.')
    elif solicitacoes[nmr-1][5] == 'Situação: Em aberto':
        print(solicitacoes[nmr-1][5])
        print(solicitacoes[nmr-1][4])
        z = int(input('\nDeseja atender a solicitação? (Digite 1 para atender e 0 para não atender) '))
        if z == 1:
            nomeprofissional = input('Insira o nome do profissional responsável pela solicitação: ')
            solicitacoes[nmr].append(nomeprofissional)
            solicitacoes[nmr-1][5] = 'Situação: Em atendimento'
        elif z == 0:
            w = int(input('Deseja acessar outra solicitação? (Digite 0 para parar) '))
            if w == 0:
                break
        elif z!=0 and z!=1:
            continue

def nova_solicitacao():
    nome = input('\nNome completo do solicitante: ')
    cpf = input('CPF: ')
    telefone = input('Número de telefone para o contato: ')
    endereco = input('Endereço (bairro, rua, número e complemento): ')
    descricao = input('Descrição da solicitação: ')
    situacao = 'Em aberto'
    
    solicitacao = { 
        'nome':nome,
        'cpf':cpf,
        'telefone':telefone,
        'endereco':endereco,
        'descricao':descricao,
        'situacao':situacao
    }

    return solicitacao