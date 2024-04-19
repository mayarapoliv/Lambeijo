import sqlite3

class LambeijosDB:
    def __init__(self):
        self.db_name = "lambeijos.db"
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def close(self):
        if self.connection:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()

    def create_table(self):
        self.cursor.execute(
                    '''CREATE TABLE IF NOT EXISTS Usuarios (
                    id INTEGER PRIMARY KEY,
                    email TEXT,
                    usuario TEXT,
                    senha TEXT,
                    numero_contato TEXT	
                     );'''
        )
        self.cursor.execute(
                    '''CREATE TABLE IF NOT EXISTS Cliente (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    raca TEXT,
                    idade INTEGER,
                    comportamento TEXT,
                    sobre TEXT,
                    usuario_id INTEGER,
                    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id)
                     );''')
        self.close()

    def escrever_dados_usuario(self, email, usuario, senha, numero_contato):
        # Executar uma instrução SQL para inserir dados na tabela
        self.cursor.execute(
            """INSERT INTO Usuarios (email, usuario, senha, numero_contato) VALUES (?, ?, ?, ?)""",
            (email, usuario, senha, numero_contato),
     )
        self.close()

    def escrever_dados_cliente(self, nome, raca, idade, comportamento, sobre, usuario_id):      
        self.cursor.execute(
            """INSERT INTO Cliente (nome, raca, idade, comportamento, sobre, usuario_id) VALUES (?, ?, ?, ?, ?, ?)""",
            (nome, raca, idade, comportamento, sobre, usuario_id),
        )
        self.close()


    '''  def atualizar_dados_usuario(self, email, usuario, senha, numero_contato):
        # Executar uma instrução SQL para atualizar os dados na tabela
        self.cursor.execute(
            """UPDATE Usuarios SET senha = ?, numero_contato = ? WHERE usuario = ? AND email = ?""",
            (email, usuario, senha, numero_contato),
                    )
        self.close()


    def atualizar_dados_cliente(self, nome, raca, idade, comportamento, sobre, usuario_id):
        # Executar uma instrução SQL para atualizar os dados na tabela
        self.cursor.execute(
            """UPDATE Cliente SET raca = ?, idade = ?, comportamento = ?, sobre = ? WHERE nome = ? AND usuario_id = ?""",
            (nome, raca, idade, comportamento, sobre, usuario_id),
        )
        self.close()
    '''

    def selecionar_todos_os_dados(self,usuario_id):
        # Executar uma instrução SQL para selecionar todos os dados da tabela
        self.cursor.execute("""SELECT * FROM Clientes WHERE usuario_id = ? """, (usuario_id))

        # Recuperar todos os dados
        dados = self.cursor.fetchall()
        self.close()

        # Imprimir os dados
        return dados

    
    def excluir_dados(self):
        self.cursor.execute('''DELETE FROM Cliente WHERE usuario_id = ?''')
        self.close()


x = LambeijosDB()
#x.create_table()
#x.escrever_dados_usuario('teste2@teste.com', 'teste2', 1234, 19999999998)
#x.escrever_dados_cliente('Macondo', 'Shiba inu', 4, 'Manso', 'Tem muita energia', 1)
#x.atualizar_dados('mayara@gmail.com', 'Mayara', 666, 14991409292)
