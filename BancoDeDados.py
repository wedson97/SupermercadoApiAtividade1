import sqlite3



def criarTabela(nomeTabela):
    conn = sqlite3.connect('supermercado.db')
    cursor = conn.cursor()

    cursor.execute(f"""
    CREATE TABLE {nomeTabela} (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
    );
    """)

    print('Tabela criada com sucesso.')
    conn.close()

def requisicaoGetPorId(nomeTabela, id):
    conn = sqlite3.connect('supermercado.db')
    cursor = conn.cursor()

    cursor.execute(f"""
    SELECT * FROM {nomeTabela} WHERE id={id};
    """)

    dados = cursor.fetchall()
    conn.close()

    return dados    

def requisicaoGet(nomeTabela):
    conn = sqlite3.connect('supermercado.db')
    cursor = conn.cursor()

    cursor.execute(f"""
    SELECT * FROM {nomeTabela};
    """)

    dados = cursor.fetchall()
    conn.close()

    return dados
    

def requisicaoPost(nomeTabela,nome):
    conn = sqlite3.connect('supermercado.db')
    cursor = conn.cursor()

    cursor.execute(f"""
    INSERT INTO {nomeTabela} (nome)
    VALUES ('{nome}')
    """)

    conn.commit()

    print('Dados inseridos com sucesso.')

    dados = cursor.fetchall()
    conn.close()
    
    return dados

