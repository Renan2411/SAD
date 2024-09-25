"""
Implementando um banco de dados no SQLite
> sqlite3 banco_teste.db
sqlite> CREATE TABLE test (id int, num int);
sqlite> INSERT INTO test VALUES (1, 100), (2, 200);
sqlite> SELECT * FROM test LIMIT 1;
sqlite> .tables
sqlite> .quit
"""

import sqlite3 as s

# Criar objeto de conexão e conectar ao banco
conn = s.connect('banco_teste.db')

# Criar cursor
cur = conn.cursor()

# Determinar declarações SQL a serem executadas e executá-las no banco
#cur.execute("CREATE TABLE test(id int, num int);").fetchall()
#conn.commit()

cur.execute("INSERT INTO test VALUES (1 100), (2, 200);")
#cur.execute("INSERT INTO test VALUES (3, 300), (4, 400);")
conn.commit()

res = cur.execute("SELECT * FROM test LIMIT 1;").fetchall()


# Verificar se tabelas foram criadas
print(res)

cur.close()
conn.close()

