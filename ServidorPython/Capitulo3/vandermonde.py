import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp

def vandermonde_interpolation(x_data, y_data):
    """
    Calcula el polinomio interpolante utilizando el método de Vandermonde.

    Parámetros:
    - x_data: Lista o array de valores x (n)
    - y_data: Lista o array de valores y (n)

    Retorna:
    - result: Diccionario con el estado y los datos del polinomio
        - 'state': 'Exact', 'Aprox' o 'Failed'
        - 'message': Mensaje descriptivo en caso de error
        - 'coefficients': Coeficientes del polinomio (si es exitoso)
        - 'polynomial': Expresión simbólica del polinomio interpolante (si es exitoso)
        - 'plot_file': Nombre del archivo donde se guardó la gráfica (si es exitoso)
        - 'errors': Diccionario con errores en puntos específicos (si es exitoso)
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

    # Ordenar los datos por x en caso de que no estén ordenados
    sorted_indices = np.argsort(x_data)
    x_data = np.array(x_data)[sorted_indices]
    y_data = np.array(y_data)[sorted_indices]

    try:
        # Construcción de la matriz de Vandermonde
        degree = n - 1
        A = np.vander(x_data, N=n, increasing=False)  # [x^n-1, ..., x, 1]
        b = np.array(y_data)

        # Solución de los coeficientes utilizando la inversa de A
        a = np.linalg.inv(A).dot(b)
    except np.linalg.LinAlgError:
        return {'state': 'Failed', 'message': "La matriz de Vandermonde es singular y no se puede invertir."}
    except Exception as e:
        return {'state': 'Failed', 'message': f"Error durante el cálculo de los coeficientes: {e}"}

    # Crear el polinomio simbólico
    x = sp.symbols('x')
    polynomial = 0
    for i in range(n):
        polynomial += a[i] * x**(degree - i)
    polynomial = sp.expand(polynomial)

    state = 'Exact'

    result = {
        'state': state,
        'tabla': A.tolist(),
        'coefficients': str(a.tolist()),
        'polynomial': str(polynomial),
    }

    return result
# Función principal
if __name__ == '__main__':
    # Explicación al usuario
    print("Interpolación de Vandermonde")
    print("Ingrese hasta 8 puntos de datos (x, y).")
    print("Los valores de x deben ser distintos entre sí.\n")

    try:
        # Solicitar número de puntos
        n = int(input("¿Cuántos puntos desea ingresar? (entre 2 y 8): "))
        if n < 2 or n > 8:
            raise ValueError("El número de puntos debe estar entre 2 y 8.")

        x_data = []
        y_data = []

        # Ingresar valores de x
        print("\nIngrese los valores de x:")
        for i in range(n):
            x_val = float(input(f"x[{i+1}]: "))
            x_data.append(x_val)

        # Ingresar valores de y
        print("\nIngrese los valores de y correspondientes:")
        for i in range(n):
            y_val = float(input(f"y[{i+1}]: "))
            y_data.append(y_val)

        # Llamada a la función de interpolación
        result = vandermonde_interpolation(x_data, y_data)

        # Manejo de resultados
        if result['state'] in ['Exact', 'Aprox']:
            print(f"\nEstado de la interpolación: {result['state']}")
            print("\nCoeficientes del polinomio de interpolación de Vandermonde:")
            for i, coeff in enumerate(result['coefficients']):
                print(f"a[{i}] = {coeff:.10f}")

            print("\nPolinomio Interpolante de Vandermonde:")
            print(result['polynomial'])

            print(f"\nEl gráfico ha sido guardado como '{result['plot_file']}'.")
            print("\nCálculo de errores en puntos específicos:")
            for point, error in result['errors'].items():
                print(f"Error en x = {point}: |P({point}) - Real({point})| = {error:.6e}")
        else:
            # Estado 'Failed'
            print(f"\nEstado de la interpolación: {result['state']}")
            print(f"Mensaje: {result['message']}")
            if 'plot_file' in result:
                print(f"\nEl gráfico ha sido guardado como '{result['plot_file']}'.")
            if 'errors' in result:
                print("\nCálculo de errores en puntos específicos:")
                for point, error in result['errors'].items():
                    print(f"Error en x = {point}: |P({point}) - Real({point})| = {error:.6e}")

    except ValueError as ve:
        print(f"\nError de entrada: {ve}")
    except Exception as e:
        print(f"\nError: {e}")