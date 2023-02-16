def formularioInicioSesion():
    
    print ("FORMULARIO DE INICIO DE SESION\n")
    
    nombre = input (">Ingrese usuario: ")
    contraseña = input (">Ingrese contraseña : ")
    
    return [nombre, contraseña]

# formulario registro ...................................................................................................

def formularioRegistro():
    
    print ("FORMULARIO DE REGISTRO\n")
    
    nombre = input (">Ingrese usuario: ")
    contrasena = input (">Ingrese contraseña : ")
    telefono = input (">Ingrese su numero de contacto: ")
    correo = input (">Ingrese su correo electronico: ")    
    
    return [nombre, contrasena, telefono, correo]