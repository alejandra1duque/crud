import pymysql.cursors

class MysqlConect():
    
    con = ""
    
    def __init__(self, host, user, password, db) :
        
        # Connect to the database
        self.con = pymysql.connect(host = host,
                                    user = user,
                                    password = password,
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor)

    # obtener datos de la base de datos (select)
    def getData(self, sql):
        cursor = self.con.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    
    # ejecutar consultas  (insert, delete, update)
    def query (self, sql):
        cursor = self.con.cursor()
        cursor.execute(sql)
        return self.con.commit()

    
   
    
        
        