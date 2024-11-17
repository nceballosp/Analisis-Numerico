import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp

def spline_interpolation(x_data, y_data, degree):
    """
    Calcula los coeficientes de los polinomios de interpolación de Spline
    de grado lineal (1) o cúbico (3) para el conjunto de n datos (x, y).
    
    Parámetros:
    - x_data: Lista o array de valores x (n)
    - y_data: Lista o array de valores y (n)
    - degree: Grado del spline (1 para lineal, 3 para cúbico)
    
    Retorna:
    - result: Diccionario con el estado y los datos del spline
        - 'state': 'Exact' o 'Failed'
        - 'message': Mensaje descriptivo en caso de error
        - 'coefficients': DataFrame con los coeficientes de los polinomios (si es exitoso)
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
    if degree not in [1, 3]:
        return {'state': 'Failed', 'message': "El grado debe ser 1 (lineal) o 3 (cúbico)."}

    # Ordenar los datos por x en caso de que no estén ordenados
    sorted_indices = np.argsort(x_data)
    x_data = np.array(x_data)[sorted_indices]
    y_data = np.array(y_data)[sorted_indices]

    try:
        if degree == 1:
            coefficients = linear_spline(x_data, y_data)
        elif degree == 3:
            coefficients = cubic_spline(x_data, y_data)
    except np.linalg.LinAlgError:
        return {'state': 'Failed', 'message': "La matriz es singular y no se puede invertir."}
    except Exception as e:
        return {'state': 'Failed', 'message': f"Error durante el cálculo del spline: {e}"}
    
    # Crear DataFrame para los coeficientes
    if degree == 1:
        df_coeff = pd.DataFrame(coefficients, columns=['Slope (m)', 'Intercept (b)'])
    elif degree == 3:
        df_coeff = pd.DataFrame(coefficients, columns=['a', 'b', 'c', 'd'])
    
    # Generar gráfica del spline
    plot_spline(x_data, y_data, coefficients, degree)
    
    # Preparar resultado
    result = {
        'state': 'Exact',
        'coefficients': df_coeff
    }
    
    return result

def linear_spline(x, y):
    """
    Calcula los coeficientes de los splines lineales.
    
    Parámetros:
    - x: Array de valores x (n)
    - y: Array de valores y (n)
    
    Retorna:
    - coefficients: Array de coeficientes [m, b] para cada intervalo
    """
    n = len(x)
    A = np.zeros((2*(n-1), 2*(n-1)))
    b_vec = np.zeros(2*(n-1))
    
    # Construir el sistema de ecuaciones
    for i in range(n-1):
        # Ecuación y = m*x + b para cada intervalo
        A[i, 2*i] = x[i]
        A[i, 2*i+1] = 1
        b_vec[i] = y[i]
        
        # Continuidad en los puntos interiores
        if i != n-2:
            A[n-1 + i, 2*i] = x[i+1]
            A[n-1 + i, 2*i+1] = 1
            b_vec[n-1 + i] = y[i+1]
    
    # Resolver el sistema
    coeff = np.linalg.solve(A, b_vec)
    
    # Reshape para obtener [m, b] por intervalo
    coefficients = coeff.reshape((n-1, 2))
    
    return coefficients

def cubic_spline(x, y):
    """
    Calcula los coeficientes de los splines cúbicos naturales.
    
    Parámetros:
    - x: Array de valores x (n)
    - y: Array de valores y (n)
    
    Retorna:
    - coefficients: Array de coeficientes [a, b, c, d] para cada intervalo
    """
    n = len(x)
    h = np.diff(x)
    
    # Construir la matriz A y el vector b
    A = np.zeros((n, n))
    b_vec = np.zeros(n)
    
    # Condiciones de suavidad
    A[0,0] = 1  # Natural spline: second derivative at first point is 0
    A[-1,-1] = 1  # Natural spline: second derivative at last point is 0
    
    for i in range(1, n-1):
        A[i, i-1] = h[i-1]
        A[i, i] = 2*(h[i-1] + h[i])
        A[i, i+1] = h[i]
        b_vec[i] = 3*((y[i+1] - y[i])/h[i] - (y[i] - y[i-1])/h[i-1])
    
    # Resolver el sistema para las segundas derivadas
    M = np.linalg.solve(A, b_vec)
    
    # Calcular los coeficientes de los polinomios
    coefficients = []
    for i in range(n-1):
        a = y[i]
        b_coef = (y[i+1] - y[i])/h[i] - h[i]*(2*M[i] + M[i+1])/3
        c = M[i]
        d = (M[i+1] - M[i]) / (3*h[i])
        coefficients.append([a, b_coef, c, d])
    
    coefficients = np.array(coefficients)
    
    return coefficients

def plot_spline(x_data, y_data, coefficients, degree):
    """
    Grafica el spline interpolante junto con los datos.
    
    Parámetros:
    - x_data: Array de valores x de los datos
    - y_data: Array de valores y de los datos
    - coefficients: Array de coeficientes de los splines
    - degree: Grado del spline (1 para lineal, 3 para cúbico)
    """
    plt.figure(figsize=(8,6))
    plt.scatter(x_data, y_data, color='red', label='Datos')
    
    for i in range(len(coefficients)):
        if degree == 1:
            m, b = coefficients[i]
            y_plot = m * (x_plot := np.linspace(x_data[i], x_data[i+1], 100)) + b
            plt.plot(x_plot, y_plot, label=f'Spline {i+1} (Lineal)')
        elif degree == 3:
            a, b_coef, c, d = coefficients[i]
            x_plot = np.linspace(x_data[i], x_data[i+1], 100)
            y_plot = a + b_coef*(x_plot - x_data[i]) + c*(x_plot - x_data[i])**2 + d*(x_plot - x_data[i])**3
            plt.plot(x_plot, y_plot, label=f'Spline {i+1} (Cúbico)')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Interpolación Spline {"Lineal" if degree ==1 else "Cúbico"}')
    plt.legend()
    plt.grid(True)
    filename = f'spline_interpolacion_{ "lineal" if degree ==1 else "cubico" }.svg'
    plt.savefig(filename, format='svg')
    plt.close()
    
    # No se muestra el gráfico automáticamente para evitar interrupciones en la ejecución

# Función principal
if __name__ == '__main__':
    # Explicación al usuario
    print("Interpolación Spline")
    print("Ingrese hasta 8 puntos de datos (x, y).")
    print("Los valores de x deben ser distintos entre sí.")
    print("Seleccione el grado del spline: 1 para lineal, 3 para cúbico.\n")
    
    try:
        n = int(input("¿Cuántos puntos desea ingresar? (entre 2 y 8): "))
        if n < 2 or n > 8:
            raise ValueError("El número de puntos debe estar entre 2 y 8.")
        
        x_data = []
        y_data = []
        
        print("\nIngrese los valores de x:")
        for i in range(n):
            x_val = float(input(f"x[{i+1}]: "))
            x_data.append(x_val)
        
        print("\nIngrese los valores de y correspondientes:")
        for i in range(n):
            y_val = float(input(f"y[{i+1}]: "))
            y_data.append(y_val)
        
        print("\nSeleccione el grado del spline:")
        print("1: Lineal")
        print("3: Cúbico")
        degree = int(input("Ingrese el grado (1 o 3): "))
        if degree not in [1, 3]:
            raise ValueError("El grado debe ser 1 (lineal) o 3 (cúbico).")
        
        # Llamada a la función principal
        result = spline_interpolation(x_data, y_data, degree)
        
        if result['state'] == 'Exact':
            print("\nCoeficientes de los Splines:")
            print(result['coefficients'])
            
            print(f"\nEl gráfico ha sido guardado como 'spline_interpolacion_{ 'lineal' if degree ==1 else 'cubico' }.svg'.")
        else:
            print(f"\nError: {result['message']}")
    
    except Exception as e:
        print(f"\nError: {e}")