import sqlite3 as sqlite

conn = sqlite.connect('banco.db')

cur = conn.cursor()

# Executar caso nao exista a tabela
SQL_CRIACAO_TABELA_CARGO = """

CREATE TABLE cargo (
    cargoId INT NOT NULL,
    cargoNm varchar(80),
    max_sal NUMERIC(10,2),
    min_sal NUMERIC(10,2),
    PRIMARY KEY (cargoId)
);

"""

SQL_CRIACAO_TABELA_FUNCIONARIO = """
CREATE TABLE funcionario (
    funcId INT NOT NULL,
    cargoID INT NOT NULL,
    funcNm varchar(80),
    sal NUMERIC(10,2),
    PRIMARY KEY(funcId, cargoId),
    FOREIGN KEY (cargoId) REFERENCES cargo(cargoId)
);
"""

# cur.execute(SQL_CRIACAO_TABELA_CARGO)
# cur.execute(SQL_CRIACAO_TABELA_FUNCIONARIO)

#INSERCOES

# cur.execute("INSERT INTO cargo (cargoId, cargoNm, min_sal, max_sal) VALUES(1, 'Gerente', 1000, 3000);")
# cur.execute("INSERT INTO cargo (cargoId, cargoNm, min_sal, max_sal) VALUES(2, 'Secretaria', 500, 800);")
# cur.execute("INSERT INTO cargo (cargoId, cargoNm, min_sal, max_sal) VALUES(3, 'Office Boy', 300, 490);")

# cur.execute("INSERT INTO funcionario (funcId, cargoId, funcNm, sal) VALUES(1, 1, 'Carlos', 2750);")
# cur.execute("INSERT INTO funcionario (funcId, cargoId, funcNm, sal) VALUES(1, 2, 'Maria', 825);")
# cur.execute("INSERT INTO funcionario (funcId, cargoId, funcNm, sal) VALUES(1, 3, 'Joao', 420);")
# cur.execute("INSERT INTO funcionario (funcId, cargoId, funcNm, sal) VALUES(2, 3, 'Miguel', 500);")

conn.commit()


SQL_SELECT_CARGO = """

    SELECT * FROM cargo; 

"""

SQL_JOIN_CONSULTA = """
    SELECT f.funcNm, c.cargoNm, f.sal, c.max_sal
    FROM funcionario f
    JOIN cargo c ON (c.cargoId = f.cargoId)
    WHERE f.sal > c.max_sal;
"""

result = cur.execute(SQL_JOIN_CONSULTA).fetchall()



print(result)