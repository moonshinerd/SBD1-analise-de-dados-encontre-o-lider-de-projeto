import sqlite3

# Conectando ao banco de dados (ou criando-o)
conn = sqlite3.connect('jogo.db')
cursor = conn.cursor()

# Criando as tabelas
cursor.executescript('''
CREATE TABLE Programador(
    CPF TEXT PRIMARY KEY,
    email TEXT,
    nome TEXT,
    role TEXT,
    nome_usuario TEXT                   
);

CREATE TABLE Contratante(
    CNPJ TEXT PRIMARY KEY,
    email TEXT,
    nome_empresa TEXT,
    telefone TEXT
);

CREATE TABLE Projeto(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mes INTEGER,
    ano INTEGER,
    dia INTEGER,
    valor REAL,
    situacao TEXT,
    CPF_gerente TEXT,
    CPF_contratante TEXT,
    FOREIGN KEY (CPF_gerente) REFERENCES Programador (CPF),
    FOREIGN KEY (CPF_contratante) REFERENCES Contratante (CPF)               
);

CREATE TABLE Participa_Programador_Projeto(
    CPF_programador TEXT,
    id_projeto INTEGER,
    FOREIGN KEY (CPF_programador) REFERENCES Programador (CPF),
    FOREIGN KEY (id_projeto) REFERENCES Projeto(id)
);

CREATE TABLE Versao(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numeroversao REAL,
    mes INTEGER,
    ano INTEGER,
    dia INTEGER,
    descricao TEXT,
    idProjeto INTEGER,   
    status TEXT,
    FOREIGN KEY (idProjeto) REFERENCES Projeto (id)     
);

CREATE TABLE Cria_Programador_Versao(
    CPF_programador TEXT,
    idVersao INTEGER,
    FOREIGN KEY (CPF_programador) REFERENCES Programador(CPF),
    FOREIGN KEY (idVersao) REFERENCES Versao(id)
);

CREATE TABLE Commit (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mes INTEGER,
    ano INTEGER,
    dia INTEGER,
    mensagem TEXT,
    CPF_programador TEXT,
    idVersao INTEGER,
    FOREIGN KEY (CPF_programador) REFERENCES Programador (CPF),
    FOREIGN KEY (idVersao) REFERENCES Versao (id)
);
CREATE TABLE Issue (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mes INTEGER,
    ano INTEGER,
    dia INTEGER,
    status TEXT,
    descricao TEXT,
    id_versao INTEGER,
    CPF_prog_criador TEXT,
    FOREIGN KEY (id_versao) REFERENCES Versao (id),
    FOREIGN KEY (CPF_prog_criador) REFERENCES Programador (CPF)
);
CREATE TABLE Realiza_Issue_Programador(
    CPF_programador TEXT,
    id_issue INTEGER,
    FOREIGN KEY (CPF_programador) REFERENCES Programador (CPF),
    FOREIGN KEY (id_issue) REFERENCES Issue (id)
);
''')
