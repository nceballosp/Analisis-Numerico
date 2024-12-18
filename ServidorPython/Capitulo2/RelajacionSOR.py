import numpy as np

def SOR(x0, A, b, w, Tol, niter, error_type):
    try:
        if len(x0) != len(b):
            return {'state':'Failed','message':"x and y must be the same size"}
        if np.linalg.det(A) == 0:
            return {'state':'Failed','message':"El determinante de la matriz A no puede ser 0"}
        if all(len(fila) != len(A) for fila in A):
            return {'state':'Failed','message':"La matriz debe ser cuadrada"}
        if niter < 0 or Tol <0:
            return {'state':'Failed','message':"La tolerancia y el numero de iteraciones debe ser positivo"}
        c = 0
        error = Tol + 1
        D = np.diag(np.diag(A))
        L = -np.tril(A, -1)
        U = -np.triu(A, 1)
        
        E = []    # Para guardar los errores
        Xn = []   # Para guardar los valores de x en cada iteración
        N = []    # Para guardar las iteraciones

        # Inicializa Xn como una lista de listas
        for _ in range(len(x0)):
            Xn.append([])

        # Guardar los valores iniciales
        for i in range(len(x0)):
            Xn[i].append(float(x0[i]))  # Guardar x0 en cada columna
        N.append(c)              # Guardar la iteración 0
        E.append("-")            # No hay error en la primera iteración

        while error > Tol and c < niter:
            T = np.linalg.inv(D - w * L) @ ((1 - w) * D + w * U)
            C = w * np.linalg.inv(D - w * L) @ b
            x1 = T @ x0 + C
            radioEsp = np.max(np.abs(np.linalg.eigvals(T)))
            
            # Calcular error absoluto o relativo
            if error_type == 'Abs':
                error = np.linalg.norm(x1 - x0, np.inf)  # Error absoluto
            elif error_type == 'Rel':
                error = np.linalg.norm((x1 - x0) / x1, np.inf)  # Error relativo

            # Guardar los valores de x1, la iteración y el error
            for i in range(len(x1)):
                Xn[i].append(float(x1[i]))  # Guardar el valor de x1 en la columna correspondiente
            E.append(float(error))          # Guardar el error
            c += 1
            N.append(c)              # Guardar la iteración actual
            
            x0 = x1  # Actualizar x0

        if error < Tol:
            # Construir la tabla como lista de tuplas: (i, x1, x2, ..., error)
            tabla = []
            for i in range(len(N)):
                fila = [N[i]] + [Xn[j][i] for j in range(len(x0))] + [E[i]]
                tabla.append(tuple(fila))  # Convertir cada fila en tupla

            state = 'Aprox' 
            return {'state': state, 'tabla': tabla, 'radioEsp':radioEsp}
        else:
            s = x0
            state = 'Failed'
            return {'state': state, 'Niter': niter, 'radioEsp':radioEsp}
    except Exception as e:
        return {'state':'Failed','message':f"Error when trying to solve the system: {e}"}





if __name__ == '__main__':
    x0 = [2,2,3]
    A = [[8,3,4],[4,5,5], [5,6,10]]
    b = [10,4,3]
    Tol = 0.005
    niter = 100
    w = 1.5
    ErrorType = "Abs"
    print(SOR(x0, A, b, w, Tol, niter, ErrorType))



