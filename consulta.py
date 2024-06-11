import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('jogo.db')
cursor = conn.cursor()

# Definindo a consulta SQL
query = '''
SELECT * FROM Programador;
'''

# Executando a consulta SQL
cursor.execute(query)
result = cursor.fetchone()

# Fechando a conexão
conn.close()

# Exibindo o resultado
if result:
    print(result)
else:
    print('Nenhum resultado encontrado.')
