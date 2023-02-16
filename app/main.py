# Controlador
from controllerscontroladores.loginController import registrarUsuarioController, validarInicioSesion

#Template - plantillas - vistas
from templatesvista.login import formularioInicioSesion, formularioRegistro
from templatesvista.menu import menu
from templatesvista.salir import salir
from templatesvista.inicio import inicio

import os

while True:
    # Limpiar pantalla...........................
    os.system("cls")
    
    
    # Menu opciones.................................
    opcion = menu()
    
    # Formulario de inicio de sesion......................
    if opcion == "1":
        
        datos = formularioInicioSesion() 
        
        if validarInicioSesion(datos) == False:
            print ("Usuario incorrecto, intetalo nuevamente")
        else:
            inicio()   
        
      #  validarInicioSesion( datos )
        input ("")
    
    #Formulario de registro..................................................
    elif opcion == "2":
        
        
        registrarUsuarioController( formularioRegistro () )
        input ("Presione ENTER para continuar. ")
        
    #opcion salir........................................
    elif opcion == "0":
        
        salir ()
        break
    
    else: 
        print ("---Por favor ingrese una opcion valida---")
        input ("")