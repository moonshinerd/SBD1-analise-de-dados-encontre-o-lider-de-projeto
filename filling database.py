import sqlite3

# Conectando ao banco de dados (ou criando-o)
conn = sqlite3.connect('jogo.db')
cursor = conn.cursor()

# Criando as tabelas
cursor.executescript('''
CREATE TABLE IF NOT EXISTS Programador(
    CPF TEXT PRIMARY KEY,
    email TEXT,
    nome TEXT,
    role TEXT,
    nome_usuario TEXT
);

CREATE TABLE IF NOT EXISTS Contratante(
    CNPJ TEXT PRIMARY KEY,
    email TEXT,
    nome_empresa TEXT,
    telefone TEXT
);

CREATE TABLE IF NOT EXISTS Projeto(
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

CREATE TABLE IF NOT EXISTS Participa_Programador_Projeto(
    CPF_programador TEXT,
    id_projeto INTEGER,
    FOREIGN KEY (CPF_programador) REFERENCES Programador (CPF),
    FOREIGN KEY (id_projeto) REFERENCES Projeto(id)
);

CREATE TABLE IF NOT EXISTS Versao(
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

CREATE TABLE IF NOT EXISTS Cria_Programador_Versao(
    CPF_programador TEXT,
    idVersao INTEGER,
    FOREIGN KEY (CPF_programador) REFERENCES Programador(CPF),
    FOREIGN KEY (idVersao) REFERENCES Versao(id)
);

CREATE TABLE IF NOT EXISTS Commits (
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
CREATE TABLE IF NOT EXISTS Issue (
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
CREATE TABLE IF NOT EXISTS Realiza_Issue_Programador(
    CPF_programador TEXT,
    id_issue INTEGER,
    FOREIGN KEY (CPF_programador) REFERENCES Programador (CPF),
    FOREIGN KEY (id_issue) REFERENCES Issue (id)
);
''')

programadores = [
    ('456.821.922-33', 'maria.prog@email.com', 'Maria Luiza Silva Costa', 'Estagiária de Desenvolvimento Back End', 'malu_sil'),
    ('789.654.123-00', 'joao.prog@email.com', 'João Pedro Oliveira', 'Desenvolvedor Full Stack', 'joao_oliveira'),
    ('123.456.789-01', 'ana.prog@email.com', 'Ana Carolina Souza', 'Desenvolvedora Front End', 'ana_souza'),
    ('234.567.890-12', 'carlos.prog@email.com', 'Carlos Eduardo Pereira', 'Desenvolvedor Back End', 'carlospereira'),
    ('345.678.901-23', 'luiza.prog@email.com', 'Luiza Fernandes Lima', 'Desenvolvedora Full Stack', 'luizafernandes'),
    ('456.789.012-34', 'renato.prog@email.com', 'Renato Dias Rocha', 'Desenvolvedor Mobile', 'renatodias'),
    ('567.890.123-45', 'claudia.prog@email.com', 'Cláudia Silva Mendes', 'Engenheira de Software', 'claudiamendes'),
    ('678.901.234-56', 'marcelo.prog@email.com', 'Marcelo Almeida Santos', 'Desenvolvedor Front End', 'marceloalmeida'),
    ('789.012.345-67', 'bruna.prog@email.com', 'Bruna Costa Ribeiro', 'Desenvolvedora Back End', 'brunacosta'),
    ('890.123.456-78', 'felipe.prog@email.com', 'Felipe Andrade Nunes', 'Desenvolvedor Full Stack', 'felipenunes'),
    ('901.234.567-89', 'camila.prog@email.com', 'Camila Oliveira Souza', 'Desenvolvedora Front End', 'camilaoliveira'),
    ('012.345.678-90', 'roberto.prog@email.com', 'Roberto Costa Lima', 'Desenvolvedor Back End', 'robertocosta'),
    ('123.450.987-65', 'patricia.prog@email.com', 'Patrícia Silva Dias', 'Desenvolvedora Mobile', 'patriciasilva'),
    ('234.560.987-65', 'eduardo.prog@email.com', 'Eduardo Mendes Rocha', 'Engenheiro de Software', 'eduardorocha'),
    ('345.670.987-65', 'rafaela.prog@email.com', 'Rafaela Lima Pereira', 'Desenvolvedora Full Stack', 'rafaelalima'),
    ('456.780.987-65', 'gustavo.prog@email.com', 'Gustavo Souza Oliveira', 'Desenvolvedor Back End', 'gustavosouza'),
    ('567.890.987-65', 'mariana.prog@email.com', 'Mariana Fernandes Ribeiro', 'Desenvolvedora Front End', 'marianafernandes'),
    ('678.900.987-65', 'paulo.prog@email.com', 'Paulo Andrade Lima', 'Desenvolvedor Full Stack', 'pauloandrade'),
    ('789.010.987-65', 'leticia.prog@email.com', 'Letícia Costa Santos', 'Desenvolvedora Mobile', 'leticiacosta'),
    ('890.120.987-65', 'anderson.prog@email.com', 'Anderson Silva Mendes', 'Engenheiro de Software', 'andersonsilva'),
    ('901.230.987-65', 'thais.prog@email.com', 'Thaís Almeida Souza', 'Desenvolvedora Front End', 'thaissouza'),
    ('012.340.987-65', 'juliana.prog@email.com', 'Juliana Lima Pereira', 'Desenvolvedora Back End', 'julianalima'),
    ('123.451.234-56', 'vinicius.prog@email.com', 'Vinícius Dias Rocha', 'Desenvolvedor Full Stack', 'viniciusdias'),
    ('234.561.234-56', 'fernanda.prog@email.com', 'Fernanda Costa Oliveira', 'Desenvolvedora Mobile', 'fernandacosta'),
    ('345.671.234-56', 'alexandre.prog@email.com', 'Alexandre Souza Mendes', 'Engenheiro de Software', 'alexandresouza'),
    ('456.781.234-56', 'isabela.prog@email.com', 'Isabela Fernandes Lima', 'Desenvolvedora Full Stack', 'isabelalima'),
    ('567.891.234-56', 'ricardo.prog@email.com', 'Ricardo Oliveira Souza', 'Desenvolvedor Back End', 'ricardooliveira'),
    ('678.901.234-55', 'sara.prog@email.com', 'Sara Mendes Rocha', 'Desenvolvedora Front End', 'saramendes'),
    ('789.011.234-56', 'antonio.prog@email.com', 'Antônio Pereira Dias', 'Desenvolvedor Full Stack', 'antoniopereira'),
    ('890.121.234-56', 'luana.prog@email.com', 'Luana Costa Fernandes', 'Desenvolvedora Mobile', 'luanacosta')
]


cursor.executemany('''
INSERT INTO Programador (CPF, email, nome, role, nome_usuario)
VALUES (?, ?, ?, ?, ?)
''', programadores)

# Inserindo dados em Contratante
contratantes = [
    ('16.412.386/0001-89', 'treehouse@contato.com', 'Tree House Comp.', '(16) 3879-0960'),
    ('12.345.678/0001-01', 'contato@techsolutions.com', 'Tech Solutions Ltda.', '(11) 3123-4567'),
    ('98.765.432/0001-02', 'info@digitalinnovations.com', 'Digital Innovations S.A.', '(21) 2123-8765'),
    ('23.456.789/0001-03', 'support@cloudware.com', 'Cloudware Inc.', '(41) 3344-5566'),
    ('87.654.321/0001-04', 'contact@webgenius.com', 'Web Genius Ltda.', '(51) 3232-4545'),
    ('34.567.890/0001-05', 'services@technohub.com', 'TechnoHub S.A.', '(61) 3344-6677'),
    ('76.543.210/0001-06', 'info@networks.com', 'Networks & Co.', '(31) 3131-5454'),
    ('45.678.901/0001-07', 'hello@softwarehouse.com', 'Software House Ltda.', '(71) 3234-2323'),
    ('65.432.109/0001-08', 'contact@innotech.com', 'InnoTech S.A.', '(81) 3322-7788'),
    ('56.789.012/0001-09', 'support@solutionsx.com', 'SolutionsX Ltda.', '(91) 3244-8899'),
    ('67.890.123/0001-10', 'services@futuretech.com', 'Future Tech Inc.', '(51) 3255-7788'),
    ('78.901.234/0001-11', 'info@smartsoft.com', 'SmartSoft Ltda.', '(41) 3266-5566')
]

cursor.executemany('''
INSERT INTO Contratante (CNPJ, email, nome_empresa, telefone)
VALUES (?, ?, ?, ?)
''', contratantes)

# Inserindo dados em Projeto
projetos = [
    (2021, 5, 17, 50565.32, 'Em andamento', '345.671.234-56', '16.412.386/0001-89'),
    (2022, 9, 23, 63450.21, 'Concluído', '567.890.123-45', '12.345.678/0001-01'),
    (2020, 12, 14, 75432.89, 'Em andamento', '234.560.987-65', '98.765.432/0001-02'),
    (2023, 3, 8, 82000.75, 'Fora do Ar', '678.900.987-65', '23.456.789/0001-03'),
    (2024, 4, 5, 67000.50, 'Em andamento', '789.011.234-56', '87.654.321/0001-04'),
    (2019, 11, 29, 46000.00, 'Concluído', '890.120.987-65', '34.567.890/0001-05'),
    (2021, 6, 19, 54000.25, 'Em andamento', '123.451.234-56', '76.543.210/0001-06'),
    (2022, 7, 12, 68000.75, 'Fora do Ar', '567.890.123-45', '45.678.901/0001-07'),
    (2020, 10, 20, 75000.80, 'Concluído', '345.670.987-65', '65.432.109/0001-08'),
    (2023, 8, 25, 82000.00, 'Em andamento', '345.671.234-56', '56.789.012/0001-09'),
    (2021, 3, 17, 92000.90, 'Em andamento', '890.120.987-65', '67.890.123/0001-10'),
    (2022, 5, 15, 47500.60, 'Concluído', '234.560.987-65', '78.901.234/0001-11'),
    (2023, 10, 10, 84000.00, 'Em andamento', '345.670.987-65', '16.412.386/0001-89'),
    (2024, 1, 5, 43000.00, 'Fora do Ar', '678.900.987-65', '12.345.678/0001-01'),
    (2019, 12, 28, 55000.30, 'Concluído', '123.451.234-56', '98.765.432/0001-02'),
    (2022, 4, 13, 60000.25, 'Em andamento', '234.560.987-65', '23.456.789/0001-03'),
    (2020, 2, 20, 46000.70, 'Em andamento', '789.011.234-56', '87.654.321/0001-04'),
    (2021, 7, 5, 78000.50, 'Concluído', '345.671.234-56', '34.567.890/0001-05'),
    (2023, 9, 12, 82000.80, 'Em andamento', '567.890.123-45', '76.543.210/0001-06'),
    (2022, 8, 10, 90000.60, 'Concluído', '123.451.234-56', '45.678.901/0001-07'),
    (2019, 11, 20, 53000.75, 'Em andamento', '345.670.987-65', '65.432.109/0001-08'),
    (2024, 2, 5, 88000.30, 'Concluído', '789.011.234-56', '56.789.012/0001-09'),
    (2020, 6, 25, 75000.25, 'Em andamento', '234.560.987-65', '67.890.123/0001-10')
]
cursor.executemany('''
INSERT INTO Projeto (mes, ano, dia, valor, situacao, CPF_gerente, CPF_contratante)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', projetos)

# Inserindo dados em Participa_Programador_Projeto
participacoes = [
    # Projetos e gerentes correspondentes
    ('345.671.234-56', 1),
    ('567.890.123-45', 2),
    ('234.560.987-65', 3),
    ('678.900.987-65', 4),
    ('789.011.234-56', 5),
    ('890.120.987-65', 6),
    ('123.451.234-56', 7),
    ('567.890.123-45', 8),
    ('345.670.987-65', 9),
    ('345.671.234-56', 10),
    ('890.120.987-65', 11),
    ('234.560.987-65', 12),
    ('345.670.987-65', 13),
    ('678.900.987-65', 14),
    ('123.451.234-56', 15),
    ('234.560.987-65', 16),
    ('789.011.234-56', 17),
    ('345.671.234-56', 18),
    ('567.890.123-45', 19),
    ('123.451.234-56', 20),
    ('345.670.987-65', 21),
    ('789.011.234-56', 22),
    ('234.560.987-65', 23),

    # Projetos com 2 a 5 programadores, incluindo gerentes
    ('123.456.789-01', 1),
    ('234.567.890-12', 1),
    ('345.678.901-23', 2),
    ('456.789.012-34', 2),
    ('567.890.123-45', 3),
    ('678.901.234-56', 3),
    ('789.012.345-67', 4),
    ('890.123.456-78', 4),
    ('901.234.567-89', 4),
    ('012.345.678-90', 5),
    ('123.450.987-65', 5),
    ('234.560.987-65', 5),
    ('345.670.987-65', 6),
    ('456.780.987-65', 6),
    ('567.890.987-65', 6),
    ('678.900.987-65', 7),
    ('789.010.987-65', 7),
    ('890.120.987-65', 7),
    ('901.230.987-65', 8),
    ('012.340.987-65', 8),
    ('123.451.234-56', 8),
    ('234.561.234-56', 9),
    ('345.671.234-56', 9),
    ('456.781.234-56', 9),
    ('567.891.234-56', 10),
    ('678.901.234-56', 10),
    ('789.011.234-56', 11),
    ('890.121.234-56', 11),
    ('012.345.678-90', 12),
    ('123.450.987-65', 12),
    ('234.560.987-65', 13),
    ('345.670.987-65', 13),
    ('456.780.987-65', 14),
    ('567.890.987-65', 14),
    ('678.900.987-65', 15),
    ('789.010.987-65', 15),
    ('890.120.987-65', 15),
    ('901.230.987-65', 16),
    ('012.340.987-65', 16),
    ('123.451.234-56', 16),
    ('234.561.234-56', 17),
    ('345.671.234-56', 17),
    ('456.781.234-56', 17),
    ('567.891.234-56', 18),
    ('678.901.234-56', 18),
    ('789.011.234-56', 19),
    ('890.121.234-56', 19),
    ('012.345.678-90', 20),
    ('123.450.987-65', 20),
    ('234.560.987-65', 21),
    ('345.670.987-65', 21),
    ('456.780.987-65', 22),
    ('567.890.987-65', 22),
    ('678.900.987-65', 23),
    ('789.010.987-65', 23)
]
cursor.executemany('''
INSERT INTO Participa_Programador_Projeto (CPF_programador, id_projeto)
VALUES (?, ?)
''', participacoes)

# Inserindo dados em Versao
versoes = [
    (1.0, 1, 2021, 17, 'Primeira versão', 1, 'Online'),
    (2.0, 1, 2021, 20, 'Segunda versão', 1, 'Online'),
    (3.0, 1, 2021, 23, 'Terceira versão', 1, 'Online'),
    (4.0, 1, 2021, 25, 'Quarta versão', 1, 'Online'),
    (5.0, 1, 2021, 28, 'Quinta versão', 1, 'Online'),
    (6.0, 1, 2021, 30, 'Sexta versão', 1, 'Online'),
    (1.0, 2, 2022, 23, 'Primeira versão', 2, 'Online'),
    (2.0, 2, 2022, 26, 'Segunda versão', 2, 'Online'),
    (3.0, 2, 2022, 28, 'Terceira versão', 2, 'Online'),
    (4.0, 2, 2022, 30, 'Quarta versão', 2, 'Online'),
    (1.0, 3, 2020, 14, 'Primeira versão', 3, 'Online'),
    (2.0, 3, 2021, 15, 'Segunda versão', 3, 'Online'),
    (3.0, 3, 2021, 17, 'Terceira versão', 3, 'Online'),
    (1.0, 4, 2023, 8, 'Primeira versão', 4, 'Erro'),
    (2.0, 4, 2023, 10, 'Segunda versão', 4, 'Erro'),
    (3.0, 4, 2023, 12, 'Terceira versão', 4, 'Erro'),
    (4.0, 4, 2023, 14, 'Quarta versão', 4, 'Erro'),
    (5.0, 4, 2023, 16, 'Quinta versão', 4, 'Erro'),
    (6.0, 4, 2023, 18, 'Sexta versão', 4, 'Erro'),
    (7.0, 4, 2023, 20, 'Sétima versão', 4, 'Erro'),
    (1.0, 5, 2024, 5, 'Primeira versão', 5, 'Online'),
    (2.0, 5, 2024, 6, 'Segunda versão', 5, 'Erro'),
    (3.0, 5, 2024, 8, 'Terceira versão', 5, 'Erro'),
    (4.0, 5, 2024, 10, 'Quarta versão', 5, 'Erro'),
    (5.0, 5, 2024, 12, 'Quinta versão', 5, 'Erro'),
    (6.0, 5, 2024, 14, 'Sexta versão', 5, 'Erro'),
    (7.0, 5, 2024, 16, 'Sétima versão', 5, 'Erro'),
    (8.0, 5, 2024, 18, 'Oitava versão', 5, 'Erro'),
    (9.0, 5, 2024, 20, 'Nona versão', 5, 'Erro'),
    (10.0, 5, 2025, 22, 'Décima versão', 5, 'Erro'),
    (1.0, 6, 2019, 29, 'Primeira versão', 6, 'Online'),
    (2.0, 6, 2019, 30, 'Segunda versão', 6, 'Erro'),
    (3.0, 6, 2020, 31, 'Terceira versão', 6, 'Erro'),
    (4.0, 6, 2020, 29, 'Quarta versão', 6, 'Erro'),
    (5.0, 6, 2020, 31, 'Quinta versão', 6, 'Erro'),
    (6.0, 6, 2020, 30, 'Sexta versão', 6, 'Erro'),
    (1.0, 7, 2021, 19, 'Primeira versão', 7, 'Online'),
    (2.0, 7, 2021, 20, 'Segunda versão', 7, 'Online'),
    (3.0, 7, 2021, 21, 'Terceira versão', 7, 'Online'),
    (4.0, 7, 2021, 22, 'Quarta versão', 7, 'Online'),
    (5.0, 7, 2021, 23, 'Quinta versão', 7, 'Online'),
    (6.0, 7, 2021, 24, 'Sexta versão', 7, 'Erro'),
    (1.0, 8, 2022, 12, 'Primeira versão', 8, 'Erro'),
    (2.0, 8, 2022, 13, 'Segunda versão', 8, 'Online'),
    (3.0, 8, 2022, 14, 'Terceira versão', 8, 'Online'),
    (4.0, 8, 2022, 15, 'Quarta versão', 8, 'Online'),
    (5.0, 8, 2022, 16, 'Quinta versão', 8, 'Erro'),
    (1.0, 9, 2020, 20, 'Primeira versão', 9, 'Online'),
    (2.0, 9, 2020, 21, 'Segunda versão', 9, 'Online'),
    (3.0, 9, 2020, 22, 'Terceira versão', 9, 'Erro'),
    (4.0, 9, 2020, 23, 'Quarta versão', 9, 'Erro'),
    (5.0, 9, 2020, 24, 'Quinta versão', 9, 'Erro'),
    (1.0, 10, 2023, 25, 'Primeira versão', 10, 'Online'),
    (2.0, 10, 2023, 26, 'Segunda versão', 10, 'Online'),
    (3.0, 10, 2023, 27, 'Terceira versão', 10, 'Erro'),
    (4.0, 10, 2023, 28, 'Quarta versão', 10, 'Erro'),
    (5.0, 10, 2023, 29, 'Quinta versão', 10, 'Erro'),
    (6.0, 10, 2024, 30, 'Sexta versão', 10, 'Erro'),
    (7.0, 10, 2024, 31, 'Sétima versão', 10, 'Erro'),
    (1.0, 11, 2021, 17, 'Primeira versão', 11, 'Online'),
    (2.0, 11, 2021, 18, 'Segunda versão', 11, 'Online'),
    (3.0, 11, 2021, 19, 'Terceira versão', 11, 'Online'),
    (1.0, 12, 2022, 15, 'Primeira versão', 12, 'Online'),
    (2.0, 12, 2022, 16, 'Segunda versão', 12, 'Online'),
    (3.0, 12, 2022, 17, 'Terceira versão', 12, 'Online'),
    (4.0, 12, 2022, 18, 'Quarta versão', 12, 'Erro'),
    (5.0, 12, 2022, 19, 'Quinta versão', 12, 'Erro'),
    (6.0, 12, 2022, 20, 'Sexta versão', 12, 'Erro'),
    (1.0, 13, 2023, 10, 'Primeira versão', 13, 'Online'),
    (2.0, 13, 2023, 11, 'Segunda versão', 13, 'Erro'),
    (3.0, 13, 2023, 12, 'Terceira versão', 13, 'Erro'),
    (4.0, 13, 2024, 13, 'Quarta versão', 13, 'Erro'),
    (5.0, 13, 2024, 14, 'Quinta versão', 13, 'Erro'),
    (6.0, 13, 2024, 15, 'Sexta versão', 13, 'Erro'),
    (1.0, 14, 2024, 5, 'Primeira versão', 14, 'Erro'),
    (2.0, 14, 2024, 6, 'Segunda versão', 14, 'Erro'),
    (3.0, 14, 2024, 7, 'Terceira versão', 14, 'Erro'),
    (4.0, 14, 2024, 8, 'Quarta versão', 14, 'Erro'),
    (5.0, 14, 2024, 9, 'Quinta versão', 14, 'Erro'),
    (6.0, 14, 2024, 10, 'Sexta versão', 14, 'Erro'),
    (1.0, 15, 2019, 28, 'Primeira versão', 15, 'Erro'),
    (2.0, 15, 2020, 29, 'Segunda versão', 15, 'Online'),
    (3.0, 15, 2020, 1, 'Terceira versão', 15, 'Online'),
    (1.0, 16, 2022, 13, 'Primeira versão', 16, 'Online'),
    (2.0, 16, 2022, 14, 'Segunda versão', 16, 'Online'),
    (3.0, 16, 2022, 15, 'Terceira versão', 16, 'Online'),
    (4.0, 16, 2022, 16, 'Quarta versão', 16, 'Erro'),
    (1.0, 17, 2020, 20, 'Primeira versão', 17, 'Online'),
    (2.0, 17, 2020, 21, 'Segunda versão', 17, 'Online'),
    (3.0, 17, 2020, 22, 'Terceira versão', 17, 'Online'),
    (4.0, 17, 2020, 23, 'Quarta versão', 17, 'Online'),
    (5.0, 17, 2020, 24, 'Quinta versão', 17, 'Online'),
    (6.0, 17, 2020, 25, 'Sexta versão', 17, 'Online'),
    (1.0, 18, 2021, 5, 'Primeira versão', 18, 'Online'),
    (2.0, 18, 2021, 6, 'Segunda versão', 18, 'Online'),
    (3.0, 18, 2021, 7, 'Terceira versão', 18, 'Online'),
    (4.0, 18, 2021, 8, 'Quarta versão', 18, 'Online'),
    (1.0, 19, 2023, 12, 'Primeira versão', 19, 'Online'),
    (2.0, 19, 2023, 13, 'Segunda versão', 19, 'Online'),
    (3.0, 19, 2023, 14, 'Terceira versão', 19, 'Erro'),
    (4.0, 19, 2023, 15, 'Quarta versão', 19, 'Erro'),
    (5.0, 19, 2024, 16, 'Quinta versão', 19, 'Erro'),
    (6.0, 19, 2024, 17, 'Sexta versão', 19, 'Erro'),
    (7.0, 19, 2024, 18, 'Sétima versão', 19, 'Erro'),
    (8.0, 19, 2024, 19, 'Oitava versão', 19, 'Erro'),
    (9.0, 19, 2024, 20, 'Nona versão', 19, 'Erro'),
    (10.0, 19, 2024, 21, 'Décima versão', 19, 'Erro'),
    (1.0, 20, 2022, 10, 'Primeira versão', 20, 'Online'),
    (2.0, 20, 2022, 11, 'Segunda versão', 20, 'Online'),
    (3.0, 20, 2022, 12, 'Terceira versão', 20, 'Online'),
    (4.0, 20, 2022, 13, 'Quarta versão', 20, 'Erro'),
    (5.0, 20, 2022, 14, 'Quinta versão', 20, 'Erro'),
    (6.0, 20, 2023, 15, 'Sexta versão', 20, 'Erro'),
    (7.0, 20, 2023, 16, 'Sétima versão', 20, 'Erro'),
    (1.0, 21, 2019, 20, 'Primeira versão', 21, 'Online'),
    (2.0, 21, 2019, 21, 'Segunda versão', 21, 'Online'),
    (3.0, 21, 2020, 22, 'Terceira versão', 21, 'Online'),
    (4.0, 21, 2020, 23, 'Quarta versão', 21, 'Erro'),
    (5.0, 21, 2020, 24, 'Quinta versão', 21, 'Erro'),
    (1.0, 22, 2024, 5, 'Primeira versão', 22, 'Online'),
    (2.0, 22, 2024, 6, 'Segunda versão', 22, 'Online'),
    (3.0, 22, 2024, 7, 'Terceira versão', 22, 'Online'),
    (1.0, 23, 2020, 25, 'Primeira versão', 23, 'Online'),
    (2.0, 23, 2020, 26, 'Segunda versão', 23, 'Online'),
    (3.0, 23, 2020, 27, 'Terceira versão', 23, 'Online')
]
cursor.executemany('''
INSERT INTO Versao (numeroversao, mes, ano, dia, descricao, idProjeto, status)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', versoes)

# Inserindo dados em Cria_Programador_Versao
criadores_versao = [
    ('345.671.234-56', 1),
    ('345.671.234-56', 2),
    ('345.671.234-56', 3),
    ('345.671.234-56', 4),
    ('345.671.234-56', 5),
    ('345.671.234-56', 6),
    ('567.890.123-45', 7),
    ('567.890.123-45', 8),
    ('234.560.987-65', 9),
    ('234.560.987-65', 10),
    ('890.120.987-65', 11),
    ('234.560.987-65', 12),
    ('345.670.987-65', 13),
    ('789.011.234-56', 14),
    ('123.451.234-56', 15),
    ('234.560.987-65', 16),
    ('123.451.234-56', 17),
    ('345.671.234-56', 18),
    ('567.890.123-45', 19),
    ('123.451.234-56', 20),
    ('345.670.987-65', 21),
    ('789.011.234-56', 22),
    ('234.560.987-65', 23),
    ('567.890.123-45', 24),
    ('567.890.123-45', 25),
    ('567.890.123-45', 26),
    ('567.890.123-45', 27),
    ('567.890.123-45', 28),
    ('567.890.123-45', 29),
    ('890.120.987-65', 30),
    ('890.120.987-65', 31),
    ('890.120.987-65', 32),
    ('890.120.987-65', 33),
    ('890.120.987-65', 34),
    ('890.120.987-65', 35),
    ('123.451.234-56', 36),
    ('123.451.234-56', 37),
    ('123.451.234-56', 38),
    ('123.451.234-56', 39),
    ('123.451.234-56', 40),
    ('123.451.234-56', 41),
    ('567.890.123-45', 42),
    ('567.890.123-45', 43),
    ('567.890.123-45', 44),
    ('567.890.123-45', 45),
    ('567.890.123-45', 46),
    ('567.890.123-45', 47),
    ('345.670.987-65', 48),
    ('345.670.987-65', 49),
    ('345.670.987-65', 50),
    ('345.670.987-65', 51),
    ('345.670.987-65', 52),
    ('345.671.234-56', 53),
    ('345.671.234-56', 54),
    ('345.671.234-56', 55),
    ('345.671.234-56', 56),
    ('345.671.234-56', 57),
    ('345.671.234-56', 58),
    ('345.670.987-65', 59),
    ('345.670.987-65', 60),
    ('345.670.987-65', 61),
    ('345.670.987-65', 62),
    ('345.670.987-65', 63),
    ('345.670.987-65', 64),
    ('345.670.987-65', 65),
    ('345.670.987-65', 66),
    ('345.670.987-65', 67),
    ('345.670.987-65', 68),
    ('345.670.987-65', 69),
    ('345.670.987-65', 70),
    ('345.670.987-65', 71),
    ('345.670.987-65', 72),
    ('345.670.987-65', 73),
    ('345.670.987-65', 74),
    ('789.011.234-56', 75),
    ('789.011.234-56', 76),
    ('789.011.234-56', 77),
    ('789.011.234-56', 78),
    ('789.011.234-56', 79),
    ('789.011.234-56', 80),
    ('789.011.234-56', 81),
    ('789.011.234-56', 82),
    ('789.011.234-56', 83),
    ('789.011.234-56', 84),
    ('789.011.234-56', 85),
    ('789.011.234-56', 86),
    ('789.011.234-56', 87),
    ('789.011.234-56', 88),
    ('789.011.234-56', 89),
    ('789.011.234-56', 90),
    ('789.011.234-56', 91),
    ('789.011.234-56', 92),
    ('789.011.234-56', 93),
    ('789.011.234-56', 94),
    ('789.011.234-56', 95),
    ('789.011.234-56', 96),
    ('789.011.234-56', 97),
    ('789.011.234-56', 98),
    ('789.011.234-56', 99),
    ('789.011.234-56', 100),
    ('789.011.234-56', 101),
    ('789.011.234-56', 102),
    ('789.011.234-56', 103),
    ('789.011.234-56', 104),
    ('789.011.234-56', 105),
    ('789.011.234-56', 106),
    ('789.011.234-56', 107),
    ('789.011.234-56', 108),
    ('789.011.234-56', 109),
    ('789.011.234-56', 110),
    ('789.011.234-56', 111),
    ('789.011.234-56', 112),
    ('789.011.234-56', 113),
    ('789.011.234-56', 114),
    ('789.011.234-56', 115),
    ('789.011.234-56', 116),
    ('789.011.234-56', 117),
    ('789.011.234-56', 118),
    ('789.011.234-56', 119),
    ('789.011.234-56', 120),
    ('789.011.234-56', 121),
    ('789.011.234-56', 122),
    ('789.011.234-56', 123),
    ('789.011.234-56', 124),
    ('789.011.234-56', 125)
]
cursor.executemany('''
INSERT INTO Cria_Programador_Versao (CPF_programador, idVersao)
VALUES (?, ?)
''', criadores_versao)

# Inserindo dados em Commits
commits = [
    (11, 2021, 10, 'Commit inicial', '12345678901', 1),
    (11, 2021, 11, 'Correção de bug', '12345678902', 2),
    (12, 2021, 12, 'Adição de funcionalidade', '12345678903', 3),
    (1, 2022, 1, 'Ajuste de performance', '12345678904', 4),
    (2, 2022, 2, 'Refatoração de código', '12345678905', 5),
    (4, 2022, 3, 'Melhoria de segurança', '12345678906', 6),
    (8, 2022, 4, 'Implementação de testes', '12345678907', 7),
    (11, 2022, 5, 'Atualização de dependências', '12345678908', 8),
    (2, 2023, 6, 'Otimização de consultas', '12345678909', 9),
    (2, 2023, 7, 'Correção de layout', '12345678910', 10),
    (6, 2023, 8, 'Ajuste de responsividade', '12345678911', 11),
    (8, 2023, 9, 'Melhoria de usabilidade', '12345678912', 12),
    (9, 2023, 10, 'Adição de documentação', '12345678913', 13),
    (1, 2024, 11, 'Configuração de CI/CD', '12345678914', 14),
    (2, 2024, 12, 'Correção de vulnerabilidade', '12345678915', 15),
    (2, 2024, 1, 'Ajuste de compatibilidade', '12345678916', 16),
    (3, 2024, 2, 'Expansão de funcionalidades', '12345678917', 17),
    (3, 2024, 3, 'Correção de erro crítico', '12345678918', 18),
    (4, 2024, 4, 'Otimização de algoritmo', '12345678919', 19),
    (5, 2024, 5, 'Melhoria de arquitetura', '12345678920', 20)
]
cursor.executemany('''
INSERT INTO Commits (mes, ano, dia, mensagem, CPF_programador, idVersao)
VALUES (?, ?, ?, ?, ?, ?)
''', commits)

# Inserindo dados em Issue
issues = [
    (6, 2023, 10, 'Aberto', 'Bug na tela de login', 1, '12345678901'),
    (6, 2023, 11, 'Fechado', 'Erro no cálculo de valores', 2, '12345678902'),
    (6, 2023, 12, 'Aberto', 'Problema de performance', 3, '12345678903'),
    (6, 2024, 1, 'Fechado', 'Vulnerabilidade de segurança', 4, '12345678904'),
    (6, 2024, 2, 'Aberto', 'Interface quebrada no mobile', 5, '12345678905'),
    (6, 2024, 3, 'Fechado', 'Falha na integração de API', 6, '12345678906'),
    (6, 2024, 4, 'Aberto', 'Problema de compatibilidade', 7, '12345678907'),
    (6, 2024, 5, 'Fechado', 'Erro de usabilidade', 8, '12345678908'),
    (6, 2024, 6, 'Aberto', 'Bug em nova funcionalidade', 9, '12345678909'),
    (6, 2024, 7, 'Fechado', 'Problema de carga', 10, '12345678910'),
    (6, 2024, 8, 'Aberto', 'Falha na configuração de CI/CD', 11, '12345678911'),
    (6, 2024, 9, 'Fechado', 'Vulnerabilidade de segurança', 12, '12345678912'),
    (6, 2024, 10, 'Aberto', 'Problema de performance', 13, '12345678913'),
    (6, 2024, 11, 'Fechado', 'Erro no cálculo de valores', 14, '12345678914'),
    (6, 2024, 12, 'Aberto', 'Bug na tela de login', 15, '12345678915'),
    (6, 2025, 1, 'Fechado', 'Interface quebrada no mobile', 16, '12345678916'),
    (6, 2025, 2, 'Aberto', 'Problema de compatibilidade', 17, '12345678917'),
    (6, 2025, 3, 'Fechado', 'Erro de usabilidade', 18, '12345678918'),
    (6, 2025, 4, 'Aberto', 'Bug em nova funcionalidade', 19, '12345678919'),
    (6, 2025, 5, 'Fechado', 'Problema de carga', 20, '12345678920')
]
cursor.executemany('''
INSERT INTO Issue (mes, ano, dia, status, descricao, id_versao, CPF_prog_criador)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', issues)

# Inserindo dados em Realiza_Issue_Programador
realiza_issues = [
    ('12345678901', 1),
    ('12345678902', 2),
    ('12345678903', 3),
    ('12345678904', 4),
    ('12345678905', 5),
    ('12345678906', 6),
    ('12345678907', 7),
    ('12345678908', 8),
    ('12345678909', 9),
    ('12345678910', 10),
    ('12345678911', 11),
    ('12345678912', 12),
    ('12345678913', 13),
    ('12345678914', 14),
    ('12345678915', 15),
    ('12345678916', 16),
    ('12345678917', 17),
    ('12345678918', 18),
    ('12345678919', 19),
    ('12345678920', 20)
]
cursor.executemany('''
INSERT INTO Realiza_Issue_Programador (CPF_programador, id_issue)
VALUES (?, ?)
''', realiza_issues)

# Salvando (commit) as mudanças
conn.commit()

# Fechando a conexão
conn.close()
