import sqlite3 as sq


class DatabaseManager:

    def __init__(self, db_name):
        self.conn = sq.connect(db_name) # подключение к базе данных 
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        query1 = (
            "CREATE TABLE IF NOT EXISTS users("
                "user_id INTEGER PRIMARY KEY,"
                "telegram_id TEXT,"
                "username Text NOT NULL);"
        )
        query2 = (
            "CREATE TABLE IF NOT EXISTS cryptocurrencies("
                "crypto_id INTEGER PRIMARY KEY,"
                "crypto_name TEXT NOT NULL);"
            )

        try:
            self.query(query1)
            self.query(query2)
            self.conn.commit()
            
        except sq.Error as Error:
            print("Ошибка при создании базы данных:", Error)
    
    def add_user(self, user_name, telegram_id):
        self.cur.execute(f"INSERT INTO users(username, telegram_id) VALUES(?, ?)", (user_name, telegram_id))
        self.conn.commit()


    def add_crypto(self, crypto_names:list):
        for crypto_name in crypto_names:
            self.cur.execute("INSERT INTO cryptocurrencies VALUES(NULL, ?)", [crypto_name])
        self.conn.commit()



    def select_user_id(self, telegram_id):
        users = self.cur.execute("SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
        return users.fetchone()


    def select_symbols(self):
        symbols = self.cur.execute("SELECT * FROM cryptocurrencies")
        return symbols.fetchone()


    def select_piece_of_data(self, start, end):
        query = ("SELECT * FROM cryptocurrencies WHERE crypto_id BETWEEN 540 AND 545")
        data = self.cur.execute(query)
        return data.fetchall()

    # вспомогательные функции (сокращение, чтобы не обращаться к классу sq)
    def query(self, arg, values=None):
        if values == None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        self.conn.commit()

    def fetchone(self, arg, values=None):
        if values == None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchone()
    
    def fetchall(self, arg, values=None):
        if values == None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchall()
        
    def __del__(self):
        self.cur.close()
        self.conn.close()

