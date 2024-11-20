import React from 'react'

function Instrucciones({tipo}) {
  return (
    <>
    {tipo === 'NoLinear' &&
    <div id='instrucciones' style={{padding:"2%"}}>
      <p>Instrucciones y Recomendaciones</p>
      <br />
      <ul className="lista">
        <li>La tolerancia se puede escribir como "1e-2" o "0.002" </li>
        <br />
        <li>La funcion debe ser continua y diferenciable</li>
        <br />
        <li>Para ingresar las funciones utilice notacion de Python,
          para las esponenciales se debe usar "exp()" y para logaritmo natural "ln()"
          <p style={{fontWeight:1}}>Ejemplo: "-exp(-x)+x*(-1-x)+x**(2/3)-1"</p>
        </li>
        <br />
        <li>Para hacer la derivada de la funcion puedes ir a geogebra y copiar la misma funcion y pedir la derivada,
          despues copiar la derivada de geogebra con notacion de python en donde dice Derivada.
          <p style={{fontWeight:1}}>Ejemplo: "((3*x*(exp(-x)))+(6*(x**2))-(2*(x**(2/3)))-(3*x))/(3*x)" </p></li>
          <br />
          <li>Los intervalos tienen que existir en la funcion</li>
          <br />
          <li>La tolerancia y las iteraciones deben ser un numero positivo</li>
      </ul>
     </div>
    }

    {tipo === 'Linear' &&
    <div id='instrucciones' style={{padding:"2%"}}>
      <p>Instrucciones y Recomendaciones</p>
      <br />
      <ul className="lista">
        <li>La tolerancia se puede escribir como "1e-2" o "0.002" </li>
        <br />
        <li>El determinante de la matriz A no puede ser 0</li>
        <br />
        <li>La matriz A no puede tener algun elemento en su diagonal que sea 0.</li>
        <br />
        <li>Los vectores deben tener el mismo número de datos.
        <p style={{fontWeight:1}}>Ejemplo:x0 = [2,2], b = [10,4], </p></li>
        <br />
        <li>Asegurate de que la matriz sea cuadrada, para evitar errores</li>
        <br />
        <li>La matriz A y los vectores se deben escribir usando el formato de python.
          <p style={{fontWeight:1}}>Ejemplo: A = [[8,3],[4,5]], </p></li>
          <br />
        <li>La tolerancia y las iteraciones deben ser un numero positivo</li>
      </ul>
   </div>
    }

    {tipo === 'Interpolacion' &&
    <div id='instrucciones' style={{padding:"2%"}}>
      <p>Instrucciones y Recomendaciones</p>
      <br />
      <ul className="lista">
        <li>Ni el vector x ni el y pueden tener valores repetidos.</li>
        <br />
        <li> El vector x debe estar ordenado, es decir los valores deben ir de menor a mayor.</li>
        <br />
        <li>La matriz A no puede tener algun elemento en su diagonal que sea 0.</li>
        <br />
        <li>Los vectores deben tener el mismo número de datos.</li>
        <br />
        <li>Los vectores se deben escribir usando el formato de python.
          <p style={{fontWeight:1}}>Ejemplo: x_data = [1,2,3,4,5], </p></li>
      </ul>
     </div>
    }
    </>
  )
}

export default Instrucciones