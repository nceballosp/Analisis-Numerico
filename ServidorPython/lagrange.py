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
    
    # Generar gráfica del polinomio interpolante
    plot_lagrange_polynomial(polynomial, x_data, y_data)
    
    # Preparar resultado
    result = {
        'state': 'Exact',
        'table': Tabla_df,
        'polynomial': polynomial
    }
    
    return result

def plot_lagrange_polynomial(polynomial, x_data, y_data):
    """
    Grafica el polinomio interpolante de Lagrange junto con los datos.
    
    Parámetros:
    - polynomial: Expresión simbólica del polinomio interpolante
    - x_data: Lista o array de valores x de los datos
    - y_data: Lista o array de valores y de los datos
    """
    # Convertir la expresión simbólica a una función de Python
    polynomial_func = sp.lambdify(sp.symbols('x'), polynomial, modules=['numpy'])
    
    x_min, x_max = min(x_data), max(x_data)
    x_plot = np.linspace(x_min - 1, x_max + 1, 500)
    y_plot = polynomial_func(x_plot)
    
    plt.figure(figsize=(8,6))
    plt.plot(x_plot, y_plot, label='Polinomio Interpolante de Lagrange')
    plt.scatter(x_data, y_data, color='red', label='Datos')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolación de Lagrange')
    plt.legend()
    plt.grid(True)
    filename = 'lagrange_interpolacion.svg'
    plt.savefig(filename, format='svg')
    plt.close()
    
    # No se muestra el gráfico automáticamente para evitar interrumpir la ejecución
    # El usuario será informado de que el gráfico ha sido guardado

# Función principal
if __name__ == '__main__':
    # Explicación al usuario
    print("Interpolación de Lagrange")
    print("Ingrese hasta 8 puntos de datos (x, y).")
    print("Los valores de x deben ser distintos entre sí.\n")
    
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
        
        # Llamada a la función principal
        result = lagrange_interpolation(x_data, y_data)
        
        if result['state'] == 'Exact':
            print("\nTabla de Términos de Lagrange:")
            print(result['table'])
            
            print("\nPolinomio Interpolante de Lagrange:")
            print(result['polynomial'])
            
            print("\nEl gráfico ha sido guardado como 'lagrange_interpolacion.svg'.")
        else:
            print(f"\Failed: {result['message']}")
    
    except Exception as e:
        print(f"\Failed: {e}")