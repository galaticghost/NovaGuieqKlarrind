import sqlite3

def database():
    conexao = sqlite3.connect("gremio.db")
    
    conexao.execute("""CREATE TABLE IF NOT EXISTS usuario(
                    id INTEGER PRIMARY KEY NOT NULL,
                    nome VARCHAR NOT NULL
                    email VARCHAR NOT NULL
                    senha VARCHAR NOT NULL
                    lider BOOLEAN DEFAULT 0);""")
    
    conexao.execute("""CREATE TABLE if not exists solicitacao (
    protocolo INTEGER PRIMARY KEY NOT NULL,
    nome VARCHAR NOT NULL,
    cpf VARCHAR NOT NULL,
    telefone VARCHAR NOT NULL,
    endereco TEXT,
    descricao TEXT,
    situacao VARCHAR,
    profissional_responsavel INTEGER REFERENCES usuario DEFAULT NULL,
    problema TEXT DEFAULT NULL,
    custo NUMERIC DEFAULT NULL
);""")
    
    conexao.execute("""CREATE TABLE IF NOT EXISTS mensagens(
                    id INTEGER PRIMARY KEY NOT NULL,
                    mensagem TEXT DEFAULT ' ',
                    lider REFERENCES usuario NOT NULL,
                    solicitante REFERENCES usuario NOT NULL,
                    mensagem_anteiror INTEGER DEFAULT NULL,
                    mensagem_sucessor INTEGER DEFAULT NULL);""")
    conexao.commit()
    return conexao

def menu():
    banco = database()
    while True:
        print()
        print('1. Criar nova solicitação.')
        print('2. Buscar solicitações "Em Aberto".')
        print('3. Buscar solicitações "Em Atendimento".')
        print('4. Buscar solicitações "Encerradas".')
        print('5. Buscar relatório de atendimento.')
        print('6. Sair.')
        print()
        x = input('Insira o número desejado: ')
        match x:
            case '1':
                nova_solicitacao(banco)
            case '2':
                buscar_solitacoes_em_aberto(banco)
            case '3':
                buscar_solitacoes_em_atendimento(banco)
            case '4':
                buscar_solitacoes_encerradas(banco)
            case '5':
                relatorios(banco)
            case '6':
                break
            case _:
                continue
    print()
    print('Programa encerrado.')

def nova_solicitacao(banco):
    print('Caso queira encerrar a solicitação, digite "f".')
    nome = input('\nNome completo do solicitante: ')
    if nome =='f':
        return None
    cpf = input('CPF: ')
    telefone = input('Número de telefone para o contato: ')
    endereco = input('Endereço (bairro, rua, número e complemento): ')
    descricao = input('Descrição da solicitação: ')
    situacao = 'Em Aberto'
    sql = f"Insert into solicitacao(nome, cpf, telefone, endereco, descricao, situacao) values(?,?,?,?,?,?)"
    banco.execute(sql, (nome,cpf,telefone,endereco,descricao,situacao))
    banco.commit()

def buscar_solitacoes_em_aberto(banco):
    w = False
    sql = "SELECT * FROM solicitacao s WHERE s.situacao = 'Em Aberto'"
    resultado = banco.execute(sql)
    resultado = resultado.fetchall()
    for solicitacao in resultado:
        print(solicitacao)
        w = True
    print()
    if w == True:
        while True:
            print('\nDeseja atender alguma solitação? \n1: Atender Solicitalção,\n2: Excluir Solicitação, \n3: Voltar ')
            y = input('\nDigite o número correspondente: ')
            match y:
                case '1':
                    z = int(input('Insira o número do protocolo da solicitação para ser atendida: '))
                    nome_responsavel = input('Insira o nome do responsável pelo atendimento: ')
                    sql = "UPDATE solicitacao SET profissional_responsavel = ?, situacao = 'Em Atendimento' WHERE protocolo = ? AND situacao = 'Em Aberto'"
                    banco.execute(sql, (nome_responsavel, z))
                    banco.commit()
                    return
                case '2':
                    z = int(input('Insira o número do protocolo da solicitação para ser excluída: '))
                    sql = "DELETE from solicitacao WHERE protocolo = ? AND situacao = 'Em Aberto'"
                    banco.execute(sql, (z,))
                    banco.commit()
                case '3':
                    break

    else:
        print('Nenhuma solicitação "Em Aberto" registrada.')

def buscar_solitacoes_em_atendimento(banco):
    w = False
    sql = "SELECT * FROM solicitacao s WHERE s.situacao = 'Em Atendimento'"
    resultado = banco.execute(sql)
    resultado = resultado.fetchall()
    for solicitacao in resultado:
        print(solicitacao)
        w = True
    print()
    if w == True:
        print('Deseja encerrar alguma solitação?')
        y = input('Se sim, digite 1, caso contrário ignore: ')
        if y == '1':
            z = int(input('Insira o número do protocolo da solicitação para ser encerrada: '))
            problema = input('Insira o problema relatado durante o atendimento: ')
            custo = float(input('Insira o custo de manutenção em reais: '))
            sql = "UPDATE solicitacao SET situacao = 'Encerrada', problema = ?, custo = ? WHERE protocolo = ? AND situacao = 'Em Atendimento'"
            banco.execute(sql, (problema, custo, z))
            banco.commit()
            print(f'Solicitação encerrada')
    else:
        print('Nenhuma solicitação "Em Atendimento" registrada.')

def buscar_solitacoes_encerradas(banco):
    w = False
    sql = "SELECT * FROM solicitacao s WHERE s.situacao = 'Encerrada'"
    resultado = banco.execute(sql)
    resultado = resultado.fetchall()
    for solicitacao in resultado:
        print(solicitacao)
        w = True
    print()
    if w == False:
        print('Nenhuma solicitação "Encerrada" registrada.')

def percentual_e_status(banco):
    sql = "select * from solicitacao"
    resultado = banco.execute(sql)
    resultado = resultado.fetchall()
    qntd_aberto = qntd_atendimento = qntd_encerrada = total = 0
    for solicitacao in resultado:
        if solicitacao[6] == 'Em Aberto':
            qntd_aberto += 1
        elif solicitacao[6] == 'Em Atendimento':
            qntd_atendimento += 1
        elif solicitacao[6] == 'Encerrada':
            qntd_encerrada += 1
        total += 1
    porcentagem_em_aberto = (qntd_aberto/total)*100
    porcentagem_em_atendimento = (qntd_atendimento/total)*100
    porcentagem_encerradas = (qntd_encerrada/total)*100
    print(f'\nEm Aberto: Quantidade = {qntd_aberto}, Porcentagem = {porcentagem_em_aberto}')
    print(f'Em Atendimento: Quantidade = {qntd_atendimento}, Porcentagem = {porcentagem_em_atendimento}')
    print(f'Encerradas: Quantidade = {qntd_encerrada}, Porcentagem = {porcentagem_encerradas}')

def relatorio_geral(banco):
    sql = "select * from solicitacao"
    resultado = banco.execute(sql)
    resultado = resultado.fetchall()
    for solicitacao in resultado:
        print(solicitacao)

def demanda_por_lider(banco):
    sql = "select * from solicitacao where profissional_responsavel is not null"
    resultado = banco.execute(sql)
    resultado = resultado.fetchall()
    lideres = {}
    for lider in resultado:
        if  lider[7] not in lideres:
            lideres.update({lider[7]: 1})
        else:
            lideres[lider[7]] += 1
    print()
    for lider in lideres:
        print(f'{lider}, quantidade de atendimentos: {lideres[lider]}')

def relatorios(banco):
    print('\n1. Relatório com todas as demandas.')
    print('2. Relatório com quantidade e percentual por status de demanda.')
    print('3. Relatório com a quantidade de demandas atendidas por líder de equipe.')
    print()
    x = int(input('Insira o número desejado: '))
    match x:
        case 1:
            relatorio_geral(banco)
        case 2:
            percentual_e_status(banco)
        case 3:
            demanda_por_lider(banco)

menu()