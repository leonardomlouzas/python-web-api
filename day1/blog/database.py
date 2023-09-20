# Conectar com o banco de dados
from sqlite3 import connect

conn = connect("blog.db")
cursor = conn.cursor()

# Definir e criar a tabela
conn.execute(
    """\
    CREATE TABLE if not exists post (
        id integer PRIMARY KEY  AUTOINCREMENT,
        title varchar UNIQUE NOT NULL,
        content varchar NOT NULL,
        author varchar NOT NULL
    );
    """
)

# Criar os posts iniciais para popular o DB
posts = [
    {
        "title": "Python é eleita a linguagem mais popular",
        "content": """\
            A linguagem Python foi eleita a linguagem mais popular pela revista
            tech masters e segue dominando o mundo.
        """,
        "author": "Satoshi namamoto",
    },
    {
        "title": "Como criar um blog utilizando Python",
        "content": """\
            Neste tutorial você aprenderá como criar um blog utilizando Python.
            <pre> import make_a_blog </pre>
        """,
        "author": "Guido Van Rossum",
    },
]

# Inserir os posts caso o DB esteja vazio
count = cursor.execute("SELECT * FROM post;").fetchall()

if not count:
    cursor.executemany(
        """\
        INSERT INTO post (title, content, author)
        VALUES (:title, :content, :author);
        """,
        posts,
    )
    conn.commit()

# Verificar o que foi inserido
posts = cursor.execute("SELECT * FROM post;").fetchall()
assert len(posts) >= 2
