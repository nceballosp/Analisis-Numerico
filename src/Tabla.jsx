import React from 'react'
import './Tabla.css'

function Tabla({datos,tipo,metodo}) {
  let tabla;
  let headers;
  if ((datos.state === 'Exact' || datos.state === 'Aprox') && datos.tabla){
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
    // else if(tipo === 'Interpolacion' && metodo === 'NewtonInterpolante'){
    //   let columnas = [<th key={0}>n</th>];
    //   columnas.push(<th key={1}>Xi</th>);
    //   columnas.push(<th key={2}>y=F[Xi]</th>);
    //   for(let i=0;i<datos.tabla[0]?.length-3||0;i++){
    //     columnas.push(<th key={i+3}>{i}</th>);
    //   };
    //   headers= <tr>{columnas}</tr>
    // }
  }
  else if(datos.table){
    tabla = <div dangerouslySetInnerHTML={{ __html: datos.table }}></div>
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

    {(tipo === 'Interpolacion' && metodo === 'Vandermonde') &&
    <>
      <table>
      <tbody>
        {tabla}
      </tbody>
      </table>
      <h1>{datos.coefficients}</h1>
      <h1>{datos.polynomial}</h1>
      </>
    }
    {(tipo === 'Interpolacion' && (metodo === 'NewtonInterpolante' || metodo === 'Lagrange')) &&
    <>
      {tabla}
      <h1>{datos.polynomial}</h1>
      </>
    }
    
    </>
  )
}

export default Tabla