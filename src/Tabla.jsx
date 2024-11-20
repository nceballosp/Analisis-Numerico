import React from 'react'
import './Tabla.css'

function Tabla({datos,tipo,metodo}) {
  let convergencia
  if(datos.radioEsp < 1 ){
    convergencia = "El metodo converge";
  }
  else{
    convergencia = "El metodo no converge";
  }
  let tabla;
  let headers;
  if (datos.state === 'Exact' || datos.state === 'Aprox'){
    tabla = datos.tabla.map((fila,filaindex)=><tr key={filaindex}>{fila.map((celda,celdaindex)=><td key={celdaindex}>{celda}</td>)}</tr>);
    if(tipo === 'Linear'){
      let columnas = [<th key={0}>n</th>];
      for(let i=1;i<datos.tabla[0]?.length-1||0;i++){
        columnas.push(<th key={i+1}>X{i}</th>);
      };
      let ultkey = columnas.length;
      columnas.push(<th key={ultkey+1}>E</th>);
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
    <> 
      <table>
      <thead>
        {headers}
      </thead>
      <tbody>
        {tabla}
      </tbody>
      </table>
      <div className='radio'>
        <p>Radio Espectral:</p>
        {datos.radioEsp}
      </div>
      <div className='convergencia'>
        {convergencia}
      </div>
    </>
    }

    {(tipo === 'Interpolacion' && metodo === 'Vandermonde') &&
      <table>
      <thead>
        <tr>
          <th>
            Grado
          </th>
          <th>
            Polinomio
          </th>
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
