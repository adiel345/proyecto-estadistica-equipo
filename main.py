def division(a,b):
    rest = a / b
    return rest

def suma(a,b):
    rest = a + b
    return rest

def resta(a,b):
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

    #Aqui se llamaran las fumciones de los intengrantes del equipo
if __name__ == "__main__":
    main()