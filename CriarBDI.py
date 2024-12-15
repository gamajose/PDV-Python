import sqlite3
import sqlite3 as lite

#Criando conexão
try:
    con = lite.connect('bdsystem.db')
    print('Conexão com o banco de dados realizada com sucesso!')
except sqlite3.Error as e:
    print('Erro ao conectar com o banco de dados: ', e)

# criando tabela de cliente
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS cliente(
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,            
            nome_cliente TEXT,            
            imagem_cliente TEXT,
            endereco_cliente TEXT,
            bairro_cliente TEXT,
            cidade_cliente TEXT,
            cep_cliente TEXT,
            estado_cliente TEXT,
            cpf_cnpj_cliente TEXT,
            ie_cliente TEXT,
            email_cliente TEXT,
            estado_civil_cliente TEXT,
            telefone_cliente TEXT
        )""")
        print("Tabela cliente criada com sucesso!")

except sqlite3.Error as e:
    print('Erro ao criar a tabela cliente:', e)

# criando tabela de FORNECEDOR
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS fornecedor(
            id_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT,            
            nome_fornecedor TEXT,
            imagem_fornecedor TEXT,
            endereco_fornecedor TEXT,
            bairro_fornecedor TEXT,
            cidade_fornecedor TEXT,
            cep_fornecedor TEXT,
            estado_fornecedor TEXT,
            cpf_cnpj_fornecedor TEXT,
            ie_fornecedor TEXT,
            email_fornecedor TEXT,
            estado_civil_fornecedor TEXT,
            telefone_fornecedor TEXT,
            conta_banco TEXT
        )""")
        print("Tabela fornecedor criada com sucesso!")

except sqlite3.Error as e:
    print('Erro ao criar a tabela fornecedor:', e)

#criando tabela de caixa
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS caixa(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data Date,
            hora TEXT,
            local TEXT,
            nome TEXT,
            cpf_cnpj TEXT,
            ie TEXT,
            endereco TEXT,
            bairro TEXT,
            cidade TEXT,
            cep TEXT,
            estado TEXT,
            produto TEXT,
            quantidade REAL,
            valor REAL,
            desconto REAL,
            valor_total REAL,
            tipo_pagamento TEXT,
            referente TEXT,
            situacao TEXT,
            telefone INTEGER,
            status TEXT,
            FOREIGN KEY (nome) REFERENCES fornecedor (nome_fornecedor) ON UPDATE CASCADE ON DELETE CASCADE 
        )""")

        print("Tabela caixa criada com sucesso!")

except sqlite3.Error as e:
    print('Erro ao criar a tabela caixa:', e)

#criando a tabela de contrato
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS contrato(
            id_contrato INTEGER PRIMARY KEY AUTOINCREMENT,            
            numero TEXT,
            vencimento INTEGER,
            objeto TEXT,
            fornecedor_contrato TEXT,
            cliente_contrato TEXT,
            cep TEXT,
            parcelas TEXT,
            valor REAL,
            data_inicio DATE,
            data_final DATE,
            iptu TEXT,
            condominio TEXT,
            luz TEXT,
            agua TEXT,
            outros TEXT,  
            status TEXT,                      
            FOREIGN KEY (fornecedor_contrato) REFERENCES fornecedor (nome_fornecedor) ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (cliente_contrato) REFERENCES cliente (nome_cliente) ON UPDATE CASCADE ON DELETE CASCADE       
        )""")

        print("Tabela contrato criada com sucesso!")

except sqlite3.Error as e:
    print('Erro ao criar a tabela contrato:', e)

#criando a tabela de produto
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS produto(
            id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT,
            quantidade REAL,
            descricao TEXT,
            localizacao TEXT,
            referencia TEXT,
            classe TEXT,
            imagem TEXT,
            valor TEXT,
            reserva TEXT,
            pedido TEXT,
            status TEXT,
            unidade TEXT                 
        )""")

        print("Tabela produto criada com sucesso!")

except sqlite3.Error as e:
    print('Erro ao criar a tabela produto:', e)

#criando a tabela de Senha
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS password(
            id_senha INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            senha TEXT,
            chave TEXT,
            tipo TEXT                            
        )""")

        print("Tabela password criada com sucesso!")

except sqlite3.Error as e:
    print('Erro ao criar a tabela produto:', e)

#criando a tabela de notas
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS notas(
            id_notas INTEGER PRIMARY KEY AUTOINCREMENT,            
            banco TEXT,
            data_emissao DATE,            
            fatura_numero INTEGER,
            fatura_valor REAL,
            ordem INTEGER,
            ordem_valor REAL,
            data_vencimento DATE,
            data_aceite DATE,
            fornecedor_notas TEXT,
            cliente_notas TEXT,                       
            FOREIGN KEY (fornecedor_notas) REFERENCES fornecedor (nome_fornecedor) ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (cliente_notas) REFERENCES cliente (nome_cliente) ON UPDATE CASCADE ON DELETE CASCADE       
        )""")

        print("Tabela notas criada com sucesso!")

except sqlite3.Error as e:
    print('Erro ao criar a tabela contrato:', e)

#criando a tabela imovel
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS imovel(
            id INTEGER NOT NULL UNIQUE,
            etiqueta INTEGER UNIQUE,
            tipo TEXT,
            endereco TEXT,
            descricao TEXT ,
            area_total TEXT,
            quartos TEXT,
            salas TEXT,
            cozinhas TEXT,
            banheiros TEXT,
            adicionais TEXT,
            estacionamento TEXT,
            valor TEXT,
            tipo_pagamento TEXT,
            disponivel TEXT,
            fotos TEXT,
            proprietario TEXT,
            status TEXT,
            transacoes TEXT,
            PRIMARY KEY(id AUTOINCREMENT)                      
            FOREIGN KEY (transacoes) REFERENCES transacoes (id_transacao) ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (proprietario) REFERENCES fornecedor (nome_fornecedor) ON UPDATE CASCADE ON DELETE CASCADE       
        )""")

        print("Tabela imovel criada com sucesso!")

except sqlite3.Error as e:
    print('Erro ao criar a tabela imovel:', e)

#criando a tabela transações
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS transacoes(          
            id_transacao INTEGER NOT NULL UNIQUE,
            id_imovel INTEGER,
            imovel TEXT,
            endereco_imovel TEXT,
            id_proprietario INTEGER,
            proprietario TEXT,
            conjuge_proprietario TEXT,
            data_inicio	DATE,
            data_fim DATE,
            valor_transacao REAL,
            tempo INTEGER,
            avalista1 TEXT,
            avalista2 TEXT,
            seguro REAL,
            cliente TEXT,
            conjuge_cliente TEXT,
            parcelas TEXT,
            valor_parcela REAL,
            extenso_parcela TEXT,
            data_parcela INTEGER,
            valor_sinal REAL,
            extenso_sinal TEXT,
            data_sinal DATE,
            valor_restante REAL,
            extenso_restante TEXT,
            data_restante DATE,
            status TEXT,
            PRIMARY KEY("id_transacao" AUTOINCREMENT),                    
            FOREIGN KEY (id_imovel) REFERENCES imovel (id) ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (proprietario) REFERENCES fornecedor (nome_fornecedor) ON UPDATE CASCADE ON DELETE CASCADE       
        )""")

        print("Tabela transacoes criada com sucesso!")

except sqlite3.Error as e:
    print('Erro ao criar a tabela transacoes:', e)

#criando a tabela conta
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS conta(         
            id INTEGER NOT NULL UNIQUE,
	        banco TEXT,
	        tipo_conta TEXT,
	        agencia TEXT,
	        conta TEXT,
	        variacao TEXT,
	        pix TEXT,
	        favorecido TEXT,
	        PRIMARY KEY("id" AUTOINCREMENT),
	        FOREIGN KEY (favorecido) REFERENCES cliente (nome_cliente) ON UPDATE CASCADE ON DELETE CASCADE
        )""")
        print("Tabela conta criada com sucesso!")

except sqlite3.Error as e:
    print('Erro ao criar a tabela conta:', e)
