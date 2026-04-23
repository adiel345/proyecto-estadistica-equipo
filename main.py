def suma(a,b):
    rest = a + b
    return rest

"""
Realiza la suma de dos numeros.

Argumentos:
    a (float): Primer numero a sumar.
    b (float): Segundo numero a sumar.
     
retorno:
    (float): Resultado de la suma a y b.
"""

def resta(a,b):
    rest = a - b
    return rest

"""
 realiza la resta de los dos numeros.

 Argumentos:
    a (float): primer numero a restar.
    b (float): segundo numero a restar.
     
 retorno:
    (float): Resultado de la resta de a menos b.
"""
    
def main():
    print("---Analizador de datos v1.0 ---")
    datos = [10,20,30,40,50,60] #datos de prueba
    int(f"Datos a procesar: {datos}")
    
    #Aqui se llamaran las funciones de los integrantes del equipo
if __name__=="__main__":
    main()