from modelsmodelos.loginModels import consultaIniciarSesion, registrarUsuarioModel


def validarInicioSesion (datos):
    
    datosUsuario =consultaIniciarSesion(datos)
    
    if len(datosUsuario) != 0:
        return datosUsuario
    else:
        return False
    

def registrarUsuarioController(datos):
    
    #Validar si envio datos
    
    return registrarUsuarioModel(datos)