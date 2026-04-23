def division(a,b):
    rest = a / b
    return rest

def suma(a,b):
    """
    Realiza la suma de dos numeros.

    Argumentos:
        a (float): Primer numero a sumar.
        b (float): Segundo numero a sumar.
        
    retorno:
        (float): Resultado de la suma a y b.
    """
    rest = a + b
    return rest

<<<<<<< HEAD

=======
>>>>>>> main
def resta(a,b):
    """
    Realiza la resta de los dos numeros.

    Argumentos:
        a (float): primer numero a restar.
        b (float): segundo numero a restar.
        
    Retorno:
        (float): Resultado de la resta de a menos b.
    """
    rest = a - b
    return rest
    
def multiplicacion(a,b):
    rest = a * b
    return rest

def potencia(a,b):
    """
    Calcula la potencia de un número elevado a otro.
    
    Args:
        a (float): La base de la potencia.
        b (float): El exponente al que se eleva la base.
        
    Returns:
        float: El resultado de a elevado a la potencia de b.
    """
    rest = a ** b
    return rest
  

def main():
    print("---Analizador de datos v1.0 ---")
    datos = [10,20,30,40,50,60] #datos de prueba
    int(f"Datos a procesar: {datos}")
    
    #Aqui se llamaran las funciones de los integrantes del equipo
if __name__=="__main__":
    main()