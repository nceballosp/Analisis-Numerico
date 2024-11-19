import React from 'react'
import './Tabla.css'

function Tabla({datos,tipo}) {
  let tabla;
  let headers;
  if (datos.state === 'Exact' || datos.state === 'Aprox'){
    tabla = datos.tabla.map((fila,filaindex)=><tr key={filaindex}>{fila.map((celda,celdaindex)=><td key={celdaindex}>{celda}</td>)}</tr>);
    if(tipo === 'Linear'){
      let columnas = [<th key={0}>E</th>];
      for(let i=0;i<datos.tabla[0]?.length-2||0;i++){
        columnas.push(<th key={i+1}>X{i}</th>);
      };
      let ultkey = columnas.length;
      columnas.push(<th key={ultkey+1}>N</th>);
      headers= <tr>{columnas}</tr>
    }
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
    {tipo === 'NoLinear' &&
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
        {headers}
      </thead>
      <tbody>
        {tabla}
      </tbody>
      </table>
      
    }

    {tipo === 'Interpolacion' &&
      <table>
      <thead>
        <tr>
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