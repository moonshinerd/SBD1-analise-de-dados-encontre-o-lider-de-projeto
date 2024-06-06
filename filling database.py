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
    CPF TEXT PRIMARY KEY,
    email TEXT,
    nome TEXT,
    telefone TEXT
);

CREATE TABLE Projeto(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datacriacao TEXT,
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
    datalancamento TEXT,
    descricao TEXT,
    idProjeto INTEGER,   
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
    dataCommit TEXT,
    mensagem TEXT,
    CPF_programador TEXT,
    idVersao INTEGER,
    FOREIGN KEY (CPF_programador) REFERENCES Programador (CPF),
    FOREIGN KEY (idVersao) REFERENCES Versao (id)
);

''')
