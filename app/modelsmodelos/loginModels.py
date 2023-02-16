from datasource.mysqlconect import MysqlConect

conexion = MysqlConect("localhost", "root", "", "aprendiendopython")

def consultaIniciarSesion (datos):
    
    sql = """
        SELECT * 
        FROM `usuarios` 
        WHERE 
            `nombre` like "{0}" AND
            `contrasena` like "{1}"
    
    """.format (datos [0], datos [1])
    
    return conexion.getData(sql)

# registrar usuarios model......................................

def registrarUsuarioModel(datos):
    
    sql = """"
        INSERT INTO `usuarios` 
            (`id`, `nombre`, `contrasena`, `telefono`, `correo`) 
        VALUES 
            (NULL, '{0}', '{1}', '{2}', '{3}');
        
    """.format (datos [0], datos [1], datos [2], datos [3])
    
    return conexion.query(sql)