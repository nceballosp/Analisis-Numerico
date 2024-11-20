import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp

def lagrange_interpolation(x_data, y_data):
    """
    Calcula el polinomio interpolante de Lagrange utilizando el método de Lagrange.
    
    Parámetros:
    - x_data: Lista o array de valores x (n)
    - y_data: Lista o array de valores y (n)
    
    Retorna:
    - result: Diccionario con el estado y los datos del polinomio
        - 'state': 'Exact' o 'Failed'
        - 'message': Mensaje descriptivo en caso de error
        - 'table': DataFrame con la tabla de términos de Lagrange (si es exitoso)
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
    
    # Crear la tabla de términos de Lagrange
    Tabla = []
    x = sp.symbols('x')
    polynomial = 0  # Inicializar el polinomio
    
    try:
        for i in range(n):
            Li = 1
            den = 1
            for j in range(n):
                if j != i:
                    Li *= (x - x_data[j])
                    den *= (x_data[i] - x_data[j])
            term = (y_data[i] * Li) / den
            Tabla.append({'Lagrange Term': f"L{i+1}(x)", 'Polynomial': term})
            polynomial += term
    except Exception as e:
        return {'state': 'Failed', 'message': f"Error durante el cálculo de los términos de Lagrange: {e}"}
    
    # Expandir el polinomio para una mejor visualización
    polynomial = sp.expand(polynomial)
    
    # Convertir la tabla a DataFrame para mejor visualización
    Tabla_df = pd.DataFrame(Tabla)
    
    
    # Preparar resultado
    result = {
        'state': 'Exact',
        'table': Tabla_df.to_html(),
        'polynomial': str(polynomial)
    }
    
    return result
