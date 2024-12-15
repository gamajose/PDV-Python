import sqlite3
import sqlite3 as lite

#Criando conexão
try:
    con = lite.connect('bdsystem.db')
    print('')
except sqlite3.Error as e:
    print('Erro ao conectar com o banco de dados: ', e)

#Tabela de Clientes*********************************************************************************************************************************************************
#Criar Cliente(Inserir)
def criar_cliente(i): #inserir dados
    with con:
        cur = con.cursor()
        query = "INSERT INTO cliente (nome_cliente, imagem_cliente, endereco_cliente, bairro_cliente, cidade_cliente,cep_cliente, estado_cliente, cpf_cnpj_cliente, ie_cliente,email_cliente, estado_civil_cliente, telefone_cliente, profissao, nacionalidade, conta_banco) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query, i)
#criar_cliente(['Fernando','','Rua','centro', 'são paulo','38730-000','MG', '123456789', '123456789', 'fernando@omelhor.com.br', 'enrolado'])

#Ver todos os Clientes (Selecionar)
def ver_clientes(): #ver dados
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM cliente"
        cur.execute(query)
        linha = cur.fetchall()
        for i in linha:
            lista.append(i)
    return lista
#print(ver_clientes())

#Atualizar os Cliente (Update)
def atualizar_cliente(i): #Atualizar dados
    with con:
        cur = con.cursor()
        query = "UPDATE cliente SET nome_cliente=?, imagem_cliente=?, endereco_cliente=?, bairro_cliente=?, cidade_cliente=?,cep_cliente=?, estado_cliente=?, cpf_cnpj_cliente=?, ie_cliente=?,email_cliente=?, estado_civil_cliente=?, telefone_cliente=?, profissao=?, nacionalidade=?, conta_banco=? WHERE id_cliente=?"
        cur.execute(query, i)

# Deletar os Clientes (Delete)
def deletar_cliente(i): #deletar dados
    with con:
        cur = con.cursor()
        query = "DELETE FROM cliente WHERE id_cliente=?"
        cur.execute(query, i)


#deletar_cliente([2])
#Fim da Tabela Cliente*********************************************************************************************************************************************************

#Tabela de Fornecedor*********************************************************************************************************************************************************
#Criar fornecedor(Inserir)
def criar_fornecedor(i): #inserir dados
    with con:
        cur = con.cursor()
        query = "INSERT INTO fornecedor (nome_fornecedor, imagem_fornecedor, endereco_fornecedor, bairro_fornecedor, cidade_fornecedor, cep_fornecedor, estado_fornecedor, cpf_cnpj_fornecedor, ie_fornecedor, email_fornecedor, estado_civil_fornecedor, telefone_fornecedor, conta_banco) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query, i)
#criar_fornecedor(['Fernando','','Rua','centro', 'são paulo','38730-000','MG', '123456789', '123456789', 'fernando@omelhor.com.br', 'enrolado'])

#Ver todos os fornecedores (Selecionar)
def ver_fornecedor(): #ver dados
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM fornecedor"
        cur.execute(query)
        linha = cur.fetchall()
        for i in linha:
            lista.append(i)
    return lista
#print(ver_fornecedor())

#Atualizar os fornecedor (Update)
def atualizar_fornecedor(i): #Atualizar dados
    with con:
        cur = con.cursor()
        query = "UPDATE fornecedor SET nome_fornecedor=?, imagem_fornecedor=?, endereco_fornecedor=?, bairro_fornecedor=?, cidade_fornecedor=?, cep_fornecedor=?, estado_fornecedor=?, cpf_cnpj_fornecedor=?, ie_fornecedor=?, email_fornecedor=?, estado_civil_fornecedor=?, telefone_fornecedor=?, conta_banco=? WHERE id_fornecedor=?"
        cur.execute(query, i)

# Deletar os fornecedor (Delete)
def deletar_fornecedor(i): #deletar dados
    with con:
        cur = con.cursor()
        query = "DELETE FROM fornecedor WHERE id_fornecedor=?"
        cur.execute(query, i)
#deletar_fornecedor([7])
#Fim da Tabela Fornecedor*********************************************************************************************************************************************************


#Tabela de Caixa*********************************************************************************************************************************************************
#Criar caixa(Inserir)
def criar_caixa(i): #inserir dados
    with con:
        cur = con.cursor()
        query = "INSERT INTO caixa (data, hora, local, nome, cpf_cnpj, ie, endereco, bairro, cidade, cep, estado, produto, quantidade, valor, desconto, valor_total, tipo_pagamento,  referente, situacao, telefone, status) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query, i)
#criar_caixa(['25/09/2023','13:30','Aqui','Fernando', '123456789','123456789','Rua', 'centro', 'Grande', '38730-000', 'SP','banana', '12', '50', '2', '48', 'dinheiro', 'colheita', 'cancelada'])

#Ver todos os caixa (Selecionar)
def ver_caixa(): #ver dados
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM caixa"
        cur.execute(query)
        linha = cur.fetchall()
        for i in linha:
            lista.append(i)
    return lista
#print(ver_caixa())

#Atualizar os caixa (Update)
def atualizar_caixa(i): #Atualizar dados
    with con:
        cur = con.cursor()
        query = "UPDATE caixa SET data=?, hora=?, local=?, nome=?, cpf_cnpj=?, ie=?, endereco=?, bairro=?, cidade=?, cep=?, estado=?, produto=?, quantidade=?, valor=?, desconto=?, valor_total=?, tipo_pagamento=?,  referente=?, situacao=?, telefone=?, status=? WHERE id=?"
        cur.execute(query, i)

# Deletar os caixa (Delete)
def deletar_caixa(i): #deletar dados
    with con:
        cur = con.cursor()
        query = "DELETE FROM caixa WHERE id=?"
        cur.execute(query, i)
#deletar_caixa([6])
#Fim da Tabela Caixa*********************************************************************************************************************************************************


#Tabela de Contrato*********************************************************************************************************************************************************
#Criar Contratos(Inserir)
def criar_contrato(i): #inserir dados
    with con:
        cur = con.cursor()
        query = "INSERT INTO contrato (numero , vencimento, objeto, fornecedor_contrato, cliente_contrato, cep, parcelas, valor,data_inicio, data_final, iptu, condominio, luz, agua, outros, status) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query, i)

#Ver todos os Contratos (Selecionar)
def ver_contratos(): #ver dados
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM contrato WHERE status='ABERTO'"
        cur.execute(query)
        linha = cur.fetchall()
        for i in linha:
            lista.append(i)
    return lista
#print(ver_contratos())

def ver_baixas(): #ver dados
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM contrato WHERE status='FECHADO'"
        cur.execute(query)
        linha = cur.fetchall()
        for i in linha:
            lista.append(i)
    return lista
#print(ver_contratos())

#Atualizar os Contrato (Update)
def atualizar_contrato(i): #Atualizar dados
    with con:
        cur = con.cursor()
        query = "UPDATE contrato SET numero=?, vencimento=?, objeto=?, fornecedor_contrato=?, cliente_contrato=?, cep=?, parcelas=?, valor=?,data_inicio=?, data_final=?, iptu=?, condominio=?, luz=?, agua=?, outros=?, status=? WHERE id_contrato=?"
        cur.execute(query, i)

# Deletar os Contrato (Delete)
def deletar_contrato(i): #deletar dados
    with con:
        cur = con.cursor()
        query = "DELETE FROM contrato WHERE id_contrato=?"
        cur.execute(query, i)


#deletar_contrato([4])
#Fim da Tabela Contrato*********************************************************************************************************************************************************

#Tabela de Produto*********************************************************************************************************************************************************
#Criar Produto(Inserir)
def criar_produto(i): #inserir dados
    with con:
        cur = con.cursor()
        query = "INSERT INTO produto (codigo, quantidade, descricao, localizacao, referencia, classe, imagem, valor, reserva, pedido, status, unidade) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query, i)
#criar_produto(['Ferro de Passar','Rua','Patrocinio','Contrato 01', 'venda',''])

#Ver todos os Produto (Selecionar)
def ver_produto(): #ver dados
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM produto"
        cur.execute(query)
        linha = cur.fetchall()
        for i in linha:
            lista.append(i)
    return lista
#print(ver_produto())

#Atualizar os Produto (Update)
def atualizar_produto(i): #Atualizar dados
    with con:
        cur = con.cursor()
        query = "UPDATE produto SET codigo=?, quantidade=?,descricao=?, localizacao=?, referencia=?, classe=?, imagem=?, valor=?, reserva=?, pedido=?, status=?, unidade=? WHERE id_produto=?"
        cur.execute(query, i)

# Deletar os Produto (Delete)
def deletar_produto(i): #deletar dados
    with con:
        cur = con.cursor()
        query = "DELETE FROM produto WHERE id_produto=?"
        cur.execute(query, i)


#deletar_produto([1])
#Fim da Tabela Produto*********************************************************************************************************************************************************

#Tabela de Password*********************************************************************************************************************************************************
#Criar Senha(Inserir)
def criar_senha(i): #inserir dados
    with con:
        cur = con.cursor()
        query = "INSERT INTO password (nome, senha, chave, tipo) VALUES(?,?,?,?)"
        cur.execute(query, i)
#criar_senha(["admin","admin", "azul", "Administrador"])
#Ver todos as senhas (Selecionar)
def ver_senha(): #ver dados
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM password"
        cur.execute(query)
        linha = cur.fetchall()
        for i in linha:
            lista.append(i)
    return lista

#Atualizar as senhas (Update)
def atualizar_senha(i): #Atualizar dados
    with con:
        cur = con.cursor()
        query = "UPDATE password SET nome=?, senha=?, chave=? , tipo=? WHERE id_senha=?"
        cur.execute(query, i)
#atualizar_senha(["admin", "admin", "azul", 1])
# Deletar as senhas (Delete)
def deletar_senha(i): #deletar dados
    with con:
        cur = con.cursor()
        query = "DELETE FROM password WHERE id_senha=?"
        cur.execute(query, i)


#Tabela de notas*********************************************************************************************************************************************************
#Criar notas(Inserir)
def criar_notas(i): #inserir dados
    with con:
        cur = con.cursor()
        query = "INSERT INTO notas (banco, data_emissao, fatura_numero, fatura_valor, ordem, ordem_valor, data_vencimento,data_aceite, fornecedor_notas, cliente_notas) VALUES(?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query, i)
#Ver todos as notas (Selecionar)
def ver_notas(): #ver dados
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM notas"
        cur.execute(query)
        linha = cur.fetchall()
        for i in linha:
            lista.append(i)
    return lista
#print(ver_contratos())

#Atualizar as notas (Update)
def atualizar_notas(i): #Atualizar dados
    with con:
        cur = con.cursor()
        query = "UPDATE notas SET banco=?, data_emissao=?, fatura_numero=?, fatura_valor=?, ordem=?, ordem_valor=?, data_vencimento=?,data_aceite=?, fornecedor_notas=?, cliente_notas=? WHERE id_notas=?"
        cur.execute(query, i)

    # Deletar as notas (Delete)
def deletar_notas(i): #deletar dados
    with con:
        cur = con.cursor()
        query = "DELETE FROM notas WHERE id_notas=?"
        cur.execute(query, i)
#deletar_contrato([4])
#Fim da Tabela Notas*********************************************************************************************************************************************************


#Criar Lembrar(Inserir)
def criar_lembrar(i): #inserir dados
    with con:
        cur = con.cursor()
        query = "INSERT INTO lembrar (nome, senha) VALUES(?,?)"
        cur.execute(query, i)
#criar_lembrar(['admin', 'admin'])
#Ver todos as senhas (Selecionar)
def ver_lembrar(): #ver dados
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM lembrar"
        cur.execute(query)
        linha = cur.fetchall()
        for i in linha:
            lista.append(i)
    return lista
#Atualizar as senhas (Update)
def atualizar_lembrar(i): #Atualizar dados
    with con:
        cur = con.cursor()
        query = "UPDATE lembrar SET nome=?, senha=? WHERE id_lembrar=?"
        cur.execute(query, i)

def deletar_lembrar(i): #deletar dados
    with con:
        cur = con.cursor()
        query = "DELETE FROM lembrar WHERE id_lembrar=?"
        cur.execute(query, i)


#Tabela de Imovel*******************************************************************************************************
#Criar Imovel(Inserir)
def criar_imovel(i): #inserir dados
    with con:
        cur = con.cursor()
        query = "INSERT INTO imovel (etiqueta, tipo, endereco, descricao, area_total, quartos, salas, cozinhas, banheiros, adicionais, estacionamento, valor, tipo_pagamento, disponivel, fotos, proprietario, status, transacoes) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query, i)
#criar_imovel()

#Ver todos os Imóveis (Selecionar)
def ver_imovel(): #ver dados
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM imovel"
        cur.execute(query)
        linha = cur.fetchall()
        for i in linha:
            lista.append(i)
    return lista
#print(ver_imovel())

#Atualizar Imóvel (Update)
def atualizar_imovel(i): #Atualizar dados
    with con:
        cur = con.cursor()
        query = "UPDATE imovel SET etiqueta=?, tipo=?, endereco=?, descricao=?, area_total=?, quartos=?, salas=?, cozinhas=?, banheiros=?, adicionais=?, estacionamento=?, valor=?, tipo_pagamento=?, disponivel=?, fotos=?, proprietario=?, status=?, transacoes=? WHERE id=?"
        cur.execute(query, i)

# Deletar Imóvel (Delete)
def deletar_imovel(i): #deletar dados
    with con:
        cur = con.cursor()
        query = "DELETE FROM imovel WHERE id=?"
        cur.execute(query, i)
#Fim da Tabela Imóvel***************************************************************************************************


#Tabela de Transações***************************************************************************************************
#Criar Transação(Inserir)
def criar_transacao(i): #inserir dados
    with con:
        cur = con.cursor()
        query = ("""INSERT INTO transacoes (id_imovel, imovel, endereco_imovel, id_proprietario, proprietario, conjuge_proprietario, 
                 data_inicio, data_fim, valor_transacao, tempo, avalista1, avalista2, seguro, cliente, conjuge_cliente, parcelas, valor_parcela, 
                 extenso_parcela, data_parcela, valor_sinal, extenso_sinal, data_sinal, valor_restante, extenso_restante, 
                 data_restante, status) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""")
        cur.execute(query, i)
#criar_transacao()

#Ver todos as Transações (Selecionar)
def ver_transacao(): #ver dados
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM transacoes"
        cur.execute(query)
        linha = cur.fetchall()
        for i in linha:
            lista.append(i)
    return lista
#print(ver_transacao())

#Atualizar Transação (Update)
def atualizar_transacao(i): #Atualizar dados
    with con:
        cur = con.cursor()
        query = """UPDATE transacoes SET id_imovel=?, imovel=?, endereco_imovel=?, id_proprietario=?, proprietario=?, conjuge_proprietario=?, 
                 data_inicio=?, data_fim=?, valor_transacao=?, tempo=?, avalista1=?, avalista2=?, seguro=?, cliente=?, conjuge_cliente=?, parcelas=?, valor_parcela=?,
                 extenso_parcela=?, data_parcela=?, valor_sinal=?, extenso_sinal=?, data_sinal=?, valor_restante=?, extenso_restante=?,
                 data_restante=?, status=? WHERE id_transacao=?"""
        cur.execute(query, i)

# Deletar Transação (Delete)
def deletar_transacao(i): #deletar dados
    with con:
        cur = con.cursor()
        query = "DELETE FROM transacoes WHERE id_transacao=?"
        cur.execute(query, i)


#Tabela de Conta*********************************************************************************************************************************************************
#Criar conta(Inserir)
def criar_conta(i): #inserir dados
    with con:
        cur = con.cursor()
        query = "INSERT INTO conta (favorecido, banco, tipo_conta, agencia, conta, variacao, pix) VALUES(?,?,?,?,?,?,?)"
        cur.execute(query, i)
#Ver todas as contas (Selecionar)
def ver_conta(): #ver dados
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM conta"
        cur.execute(query)
        linha = cur.fetchall()
        for i in linha:
            lista.append(i)
    return lista
#print(ver_conta())

#Atualizar as contas (Update)
def atualizar_conta(i): #Atualizar dados
    with con:
        cur = con.cursor()
        query = "UPDATE conta SET favorecido=?, banco=?, tipo_conta=?, agencia=?, conta=?, variacao=?, pix=? WHERE id=?"
        cur.execute(query, i)
# Deletar as contas (Delete)
def deletar_conta(i): #deletar dados
    with con:
        cur = con.cursor()
        query = "DELETE FROM conta WHERE id=?"
        cur.execute(query, i)
#Fim da Tabela Transações***********************************************************************************************