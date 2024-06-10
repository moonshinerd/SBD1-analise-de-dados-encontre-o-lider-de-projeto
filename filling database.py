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
    ('12345678901', 'prog1@email.com', 'Programador 1', 'Desenvolvedor', 'prog1'),
    ('12345678902', 'prog2@email.com', 'Programador 2', 'Desenvolvedor', 'prog2'),
    ('12345678903', 'prog3@email.com', 'Programador 3', 'Desenvolvedor', 'prog3'),
    ('12345678904', 'prog4@email.com', 'Programador 4', 'Desenvolvedor', 'prog4'),
    ('12345678905', 'prog5@email.com', 'Programador 5', 'Desenvolvedor', 'prog5'),
    ('12345678906', 'prog6@email.com', 'Programador 6', 'Desenvolvedor', 'prog6'),
    ('12345678907', 'prog7@email.com', 'Programador 7', 'Desenvolvedor', 'prog7'),
    ('12345678908', 'prog8@email.com', 'Programador 8', 'Desenvolvedor', 'prog8'),
    ('12345678909', 'prog9@email.com', 'Programador 9', 'Desenvolvedor', 'prog9'),
    ('12345678910', 'prog10@email.com', 'Programador 10', 'Desenvolvedor', 'prog10'),
    ('12345678911', 'prog11@email.com', 'Programador 11', 'Desenvolvedor', 'prog11'),
    ('12345678912', 'prog12@email.com', 'Programador 12', 'Desenvolvedor', 'prog12'),
    ('12345678913', 'prog13@email.com', 'Programador 13', 'Desenvolvedor', 'prog13'),
    ('12345678914', 'prog14@email.com', 'Programador 14', 'Desenvolvedor', 'prog14'),
    ('12345678915', 'prog15@email.com', 'Programador 15', 'Desenvolvedor', 'prog15'),
    ('12345678916', 'prog16@email.com', 'Programador 16', 'Desenvolvedor', 'prog16'),
    ('12345678917', 'prog17@email.com', 'Programador 17', 'Desenvolvedor', 'prog17'),
    ('12345678918', 'prog18@email.com', 'Programador 18', 'Desenvolvedor', 'prog18'),
    ('12345678919', 'prog19@email.com', 'Programador 19', 'Desenvolvedor', 'prog19'),
    ('12345678920', 'prog20@email.com', 'Programador 20', 'Desenvolvedor', 'prog20')
]
cursor.executemany('''
INSERT INTO Programador (CPF, email, nome, role, nome_usuario)
VALUES (?, ?, ?, ?, ?)
''', programadores)

# Inserindo dados em Contratante
contratantes = [
    ('11111111000101', 'cont1@email.com', 'Empresa 1', '123456789'),
    ('11111111000102', 'cont2@email.com', 'Empresa 2', '123456780'),
    ('11111111000103', 'cont3@email.com', 'Empresa 3', '123456781'),
    ('11111111000104', 'cont4@email.com', 'Empresa 4', '123456782'),
    ('11111111000105', 'cont5@email.com', 'Empresa 5', '123456783'),
    ('11111111000106', 'cont6@email.com', 'Empresa 6', '123456784'),
    ('11111111000107', 'cont7@email.com', 'Empresa 7', '123456785'),
    ('11111111000108', 'cont8@email.com', 'Empresa 8', '123456786'),
    ('11111111000109', 'cont9@email.com', 'Empresa 9', '123456787'),
    ('11111111000110', 'cont10@email.com', 'Empresa 10', '123456788'),
    ('11111111000111', 'cont11@email.com', 'Empresa 11', '123456789'),
    ('11111111000112', 'cont12@email.com', 'Empresa 12', '123456780'),
    ('11111111000113', 'cont13@email.com', 'Empresa 13', '123456781'),
    ('11111111000114', 'cont14@email.com', 'Empresa 14', '123456782'),
    ('11111111000115', 'cont15@email.com', 'Empresa 15', '123456783'),
    ('11111111000116', 'cont16@email.com', 'Empresa 16', '123456784'),
    ('11111111000117', 'cont17@email.com', 'Empresa 17', '123456785'),
    ('11111111000118', 'cont18@email.com', 'Empresa 18', '123456786'),
    ('11111111000119', 'cont19@email.com', 'Empresa 19', '123456787'),
    ('11111111000120', 'cont20@email.com', 'Empresa 20', '123456788')
]
cursor.executemany('''
INSERT INTO Contratante (CNPJ, email, nome_empresa, telefone)
VALUES (?, ?, ?, ?)
''', contratantes)

# Inserindo dados em Projeto
projetos = [
    (1, 2023, 10, 15000.0, 'Em andamento', '12345678901', '11111111000101'),
    (2, 2023, 11, 20000.0, 'Concluído', '12345678902', '11111111000102'),
    (3, 2023, 12, 25000.0, 'Em andamento', '12345678903', '11111111000103'),
    (4, 2024, 1, 30000.0, 'Concluído', '12345678904', '11111111000104'),
    (5, 2024, 2, 35000.0, 'Em andamento', '12345678905', '11111111000105'),
    (6, 2024, 3, 40000.0, 'Concluído', '12345678906', '11111111000106'),
    (7, 2024, 4, 45000.0, 'Em andamento', '12345678907', '11111111000107'),
    (8, 2024, 5, 50000.0, 'Concluído', '12345678908', '11111111000108'),
    (9, 2024, 6, 55000.0, 'Em andamento', '12345678909', '11111111000109'),
    (10, 2024, 7, 60000.0, 'Concluído', '12345678910', '11111111000110'),
    (11, 2024, 8, 65000.0, 'Em andamento', '12345678911', '11111111000111'),
    (12, 2024, 9, 70000.0, 'Concluído', '12345678912', '11111111000112'),
    (13, 2024, 10, 75000.0, 'Em andamento', '12345678913', '11111111000113'),
    (14, 2024, 11, 80000.0, 'Concluído', '12345678914', '11111111000114'),
    (15, 2024, 12, 85000.0, 'Em andamento', '12345678915', '11111111000115'),
    (16, 2025, 1, 90000.0, 'Concluído', '12345678916', '11111111000116'),
    (17, 2025, 2, 95000.0, 'Em andamento', '12345678917', '11111111000117'),
    (18, 2025, 3, 100000.0, 'Concluído', '12345678918', '11111111000118'),
    (19, 2025, 4, 105000.0, 'Em andamento', '12345678919', '11111111000119'),
    (20, 2025, 5, 110000.0, 'Concluído', '12345678920', '11111111000120')
]
cursor.executemany('''
INSERT INTO Projeto (mes, ano, dia, valor, situacao, CPF_gerente, CPF_contratante)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', projetos)

# Inserindo dados em Participa_Programador_Projeto
participacoes = [
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
INSERT INTO Participa_Programador_Projeto (CPF_programador, id_projeto)
VALUES (?, ?)
''', participacoes)

# Inserindo dados em Versao
versoes = [
    (1.0, 2023, 10, 'Primeira versão', 1, 'Finalizada'),
    (1.1, 2023, 11, 'Correções de bugs', 1, 'Finalizada'),
    (2.0, 2023, 12, 'Nova funcionalidade', 2, 'Finalizada'),
    (2.1, 2024, 1, 'Ajustes na nova funcionalidade', 2, 'Finalizada'),
    (3.0, 2024, 2, 'Refatoração completa', 3, 'Finalizada'),
    (3.1, 2024, 3, 'Melhorias de performance', 3, 'Finalizada'),
    (4.0, 2024, 4, 'Implementação de API', 4, 'Finalizada'),
    (4.1, 2024, 5, 'Aprimoramento de segurança', 4, 'Finalizada'),
    (5.0, 2024, 6, 'Redesign da interface', 5, 'Finalizada'),
    (5.1, 2024, 7, 'Correções de usabilidade', 5, 'Finalizada'),
    (6.0, 2024, 8, 'Integração com novos serviços', 6, 'Finalizada'),
    (6.1, 2024, 9, 'Otimização de processos', 6, 'Finalizada'),
    (7.0, 2024, 10, 'Atualização de dependências', 7, 'Finalizada'),
    (7.1, 2024, 11, 'Ajustes de compatibilidade', 7, 'Finalizada'),
    (8.0, 2024, 12, 'Adição de novos módulos', 8, 'Finalizada'),
    (8.1, 2025, 1, 'Correções pós-lançamento', 8, 'Finalizada'),
    (9.0, 2025, 2, 'Expansão de funcionalidades', 9, 'Finalizada'),
    (9.1, 2025, 3, 'Ajustes de segurança', 9, 'Finalizada'),
    (10.0, 2025, 4, 'Nova arquitetura', 10, 'Finalizada'),
    (10.1, 2025, 5, 'Aprimoramento da arquitetura', 10, 'Finalizada')
]
cursor.executemany('''
INSERT INTO Versao (numeroversao, mes, ano, descricao, idProjeto, status)
VALUES (?, ?, ?, ?, ?, ?)
''', versoes)

# Inserindo dados em Cria_Programador_Versao
criadores_versao = [
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
