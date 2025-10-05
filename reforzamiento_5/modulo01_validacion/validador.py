#Para validador
def validar_usuario(nombre_usuario):
    #Verificar longitud mínima
    if len(nombre_usuario) < 7:
        return "El nombre de usuario debe contener al menos 7 caracteres."

    #Verificar la longitud máxima
    elif len(nombre_usuario) > 12:
        return "El nombre de usuario no puede contener más de 12 caracteres."

    #Verificar si es alfanumérico
    elif not nombre_usuario.isalnum():
        return "El nombre de usuario puede contener solo letras y números."

    #Si pasa todas las validaciones
    else:
        return True
