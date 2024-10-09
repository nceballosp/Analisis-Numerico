import React from 'react'
import './Tabla.css'

function Tabla({datos,tipo}) {
  let tabla
  if (datos.state === 'Exact' || datos.state === 'Aprox'){
    tabla = datos.tabla.map(data=><tr key={data[0]}><td>{data[0]}</td><td>{data[1]}</td><td>{data[2]}</td><td>{data[3]}</td></tr>);
  }
  else if(datos.state === 'Failed'){
    return (<>
    <div>El metodo fracaso en {datos.Niter} iteraciones</div>
    </>)
  }
  else{
    return (<>
      <div>Inputs invalidos por favor revisar</div>
      </>)
  }
  return (
    <>
    {tipo === 'NonLinear' &&
      <table>
      <thead>
        <tr>
        <th>i</th>
        <th>Xn</th>
        <th>F(Xn)</th>
        <th>E</th>
        </tr>
      </thead>
      <tbody>
        {tabla}
      </tbody>
      </table>
      
    }

    {tipo === 'Linear' &&
      <table>
      <thead>
        <tr>
        <th>n</th>
        <th>X</th>
        <th>E</th>
        </tr>
      </thead>
      <tbody>
        {tabla}
      </tbody>
      </table>
      
    }
    
    </>
  )
}

export default Tabla