import datetime
import sqlite3

from modulo3.aula4.DatabaseConnection import DatabaseConnection

class Blog_model:

    def __init__(self):
        self.db_conn = DatabaseConnection()
        self._create_table()

    def _create_table(self):
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS blog (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                conteudo TEXT,
                data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP
                id_user INTEGER,
                FOREIGN KEY (id_user) REFERENCES usuarios(id)
            );
            """
        )

    def create_post(self, titulo, conteudo, id_user):
        self.db_conn.connect()
        try:
            self.db_conn.cursor.execute(
                """
                INSERT INTO blog (titulo, conteudo, id_user)
                VALUES (?, ?, ?);
            """,
                (titulo, conteudo, id_user),
            )
            print("post criado com sucesso")
        except sqlite3.IntegrityError:
            print(f"erro de integridade")
        finally:
            self.db_conn.close()

    def get_all_posts(self):
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM blog;")
        posts = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return posts

    def find_post_by_id(self, id):
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM blog WHERE id = ?;", (id,))
        post = self.db_conn.cursor.fetchone()
        self.db_conn.close()
        return post

    def update_post_by_id(self, id, titulo, conteudo):
        self.db_conn.connect()
        updates = []
        params = []
        if titulo:
            updates.append("titulo = ?")
            params.append(titulo)
        if conteudo:
            updates.append("conteudo = ?")
            params.append(conteudo)

        if not updates:
            print("Nenhum dado para atualizar.")
            self.db_conn.close()
            return

        updates.append("data_atualizacao = ?")
        params.append(datetime.now())
        params.append(id)
        query = f"UPDATE usuarios SET {', '.join(updates)} WHERE id = ?;"

        self.db_conn.cursor.execute(query, params)
        print("Usuário atualizado com sucesso!")
        self.db_conn.close()

    def delete_post_by_id(self, id):
        self.db_conn.connect()
        self.db_conn.cursor.execute("DELETE FROM blog WHERE id = ?;", (id,))
        self.db_conn.close()

    def get_all_users(self):
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM blog;")
        posts = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return posts
