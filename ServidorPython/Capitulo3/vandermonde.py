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

    # Generar gráfica del polinomio interpolante y la función real
    plot_file, errors = plot_vandermonde_polynomial(polynomial, x_data, y_data)

    # Determinar el estado basado en los errores
    error_threshold_exact = 1e-10  # Umbral para considerar 'Exact'
    error_threshold_aprox = 1e-3    # Umbral para considerar 'Aprox'

    if all(error < error_threshold_exact for error in errors.values()):
        state = 'Exact'
    elif all(error < error_threshold_aprox for error in errors.values()):
        state = 'Aprox'
    else:
        state = 'Failed'

    # Preparar resultado
    if state != 'Failed':
        result = {
            'state': state,
            'coefficients': a,
            'polynomial': polynomial,
            'plot_file': plot_file,
            'errors': errors
        }
    else:
        # En caso de que el estado sea 'Failed' debido a errores elevados
        result = {
            'state': state,
            'message': "Los errores en los puntos específicos exceden el umbral permitido.",
            'coefficients': a,
            'polynomial': polynomial,
            'plot_file': plot_file,
            'errors': errors
        }

    return result

def plot_vandermonde_polynomial(polynomial, x_data, y_data):
    """
    Grafica el polinomio interpolante de Vandermonde junto con la función real y los datos.

    Parámetros:
    - polynomial: Expresión simbólica del polinomio interpolante
    - x_data: Lista o array de valores x de los datos
    - y_data: Lista o array de valores y de los datos

    Retorna:
    - filename: Nombre del archivo donde se guardó la gráfica
    - errors: Diccionario con errores en puntos específicos
    """
    # Convertir la expresión simbólica a una función de Python
    polynomial_func = sp.lambdify(sp.symbols('x'), polynomial, modules=['numpy'])

    # Definir el rango para la gráfica
    x_min, x_max = min(x_data), max(x_data)
    x_plot = np.linspace(x_min - 1, x_max + 1, 500)
    y_plot = polynomial_func(x_plot)

    # Definir la función real para comparar
    def real_function(x_val):
        return np.exp(-x_val / 1.8) + 1.0 / (x_val**2 - 3)

    y_real = real_function(x_plot)

    # Definir puntos específicos para calcular errores
    error_points = [2.5, 6.0]
    errors = {}

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(x_plot, y_plot, 'b-', label='Polinomio de Vandermonde')
    plt.plot(x_plot, y_real, 'c--', label='Función Real')
    plt.plot(x_data, y_data, 'r*', label='Datos')

    for point in error_points:
        try:
            p_val = polynomial_func(point)
            real_val = real_function(point)
            error = abs(p_val - real_val)
            errors[point] = error

            # Plotear los puntos de comparación
            plt.plot(point, real_val, 'go', label=f'Función Real en x={point}' if point == error_points[0] else "")
            plt.plot(point, p_val, 'kx', label=f'Polinomio en x={point}' if point == error_points[0] else "")

            # Anotar el error en la gráfica
            plt.text(point, p_val, f'Error={error:.2e}', fontsize=9, ha='left', va='bottom', color='k')
        except Exception as e:
            # En caso de que el punto cause una división por cero o cualquier otro error
            errors[point] = np.inf
            plt.text(point, 0, f'Error al calcular en x={point}: {e}', fontsize=9, ha='left', va='bottom', color='r')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolación de Vandermonde vs Función Real')
    plt.legend()
    plt.grid(True)

    # Guardar la gráfica en formato SVG
    filename = 'vandermonde_interpolacion.svg'
    plt.savefig(filename, format='svg')
    plt.close()

    return filename, errors

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