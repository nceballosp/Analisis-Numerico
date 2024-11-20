import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp

def newton_interpolation(x_data, y_data):
    """
    Calcula el polinomio interpolante de Newton utilizando diferencias divididas.
    
    Parámetros:
    - x_data: Lista o array de valores x (n)
    - y_data: Lista o array de valores y (n)
    
    Retorna:
    - result: Diccionario con el estado y los datos del polinomio
        - 'state': 'Exact' o 'Failed'
        - 'message': Mensaje descriptivo en caso de error
        - 'table': DataFrame con la tabla de diferencias divididas (si es exitoso)
        - 'polynomial': Expresión simbólica del polinomio interpolante (si es exitoso)
    """
    # Validaciones de entrada
    n = len(x_data)
    if n != len(y_data):
        return {'state': 'Failed', 'message': "Los vectores x e y deben tener la misma longitud."}
    if n < 2:
        return {'state': 'Failed', 'message': "Se requieren al menos 2 puntos para la interpolación."}
    if n > 8:
        return {'state': 'Failed', 'message': "Se permiten hasta 8 datos de entrada."}
    if len(set(x_data)) != n:
        return {'state': 'Failed', 'message': "Los valores de x deben ser distintos entre sí."}
    
    # Crear la tabla de diferencias divididas
    try:
        Tabla = np.zeros((n, n+1))
        Tabla[:,0] = x_data
        Tabla[:,1] = y_data
        for j in range(2, n+1):
            for i in range(j-1, n):
                denominator = Tabla[i,0] - Tabla[i-j+1,0]
                if denominator == 0:
                    return {'state': 'Failed', 'message': "División por cero detectada en las diferencias divididas."}
                Tabla[i,j] = (Tabla[i,j-1] - Tabla[i-1,j-1]) / denominator
    except Exception as e:
        return {'state': 'Failed', 'message': f"Error durante el cálculo de diferencias divididas: {e}"}
    
    # Convertir la tabla a DataFrame para mejor visualización
    columnas = ['x', 'y'] + [f'f[x{i},x{j}]' for i in range(1, n+1) for j in range(i+1, n+1)]
    Tabla_df = pd.DataFrame(Tabla, columns=columnas[:Tabla.shape[1]])
    
    # Construcción del polinomio interpolante de Newton
    x = sp.symbols('x')
    polynomial = Tabla[0,1]  # f[x0]
    term = 1
    for i in range(1, n):
        term *= (x - Tabla[i-1,0])
        polynomial += Tabla[i,i+1] * term
    polynomial = sp.expand(polynomial)
    
    # Preparar resultado
    result = {
        'state': 'Exact',
        'table': Tabla_df.to_html(),
        'polynomial': str(polynomial)
    }
    
    return result

# if __name__ == '__main__':
#     # Explicación al usuario
#     print("Interpolación de Newton con diferencias divididas")
#     print("Ingrese hasta 8 puntos de datos (x, y).")
#     print("Los valores de x deben ser distintos entre sí.\n")
    
#     try:
#         n = int(input("¿Cuántos puntos desea ingresar? (entre 2 y 8): "))
#         if n < 2 or n > 8:
#             raise ValueError("El número de puntos debe estar entre 2 y 8.")
        
#         x_data = []
#         y_data = []
        
#         print("\nIngrese los valores de x:")
#         for i in range(n):
#             x_val = float(input(f"x[{i+1}]: "))
#             x_data.append(x_val)
        
#         print("\nIngrese los valores de y correspondientes:")
#         for i in range(n):
#             y_val = float(input(f"y[{i+1}]: "))
#             y_data.append(y_val)
        
#         # Llamada a la función principal
#         result = newton_interpolation(x_data, y_data)
        
#         if result['state'] == 'Exact':
#             print("\nTabla de Diferencias Divididas:")
#             print(result['table'])
            
#             print("\nPolinomio Interpolante de Newton:")
#             print(result['polynomial'])
            
#             print("\nEl gráfico ha sido guardado como 'newton_interpolacion.svg'.")
#         else:
#             print(f"\Failed: {result['message']}")
    
#     except Exception as e:
#         print(f"\Failed: {e}")