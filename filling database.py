import sqlite3

# Conectando ao banco de dados (ou criando-o)
conn = sqlite3.connect('jogo.db')
cursor = conn.cursor()

# Criando as tabelas
cursor.executescript('''
''')