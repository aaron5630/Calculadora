respuesta="si"
print("Calculadora")
while respuesta in ["si","sí"]:
    try:
        operacion=input("Escribe la operación matemática completa que deseas consultar: ")
        resultado=eval(operacion)
        print(resultado)
    except ZeroDivisionError:
        print("No se puede dividir entre 0.")
    except:
        print("Operación no válida.") 
    respuesta=input("¿Quieres hacer otra operación? ").lower()      
    while respuesta not in ["si","sí","no"]:
        print("Respuesta no válida.")
        respuesta=input("¿Quieres hacer otra operación? ").lower()
print("Fín de la aplicación.")
