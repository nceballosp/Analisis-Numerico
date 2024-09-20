import React from 'react'

function Tabla({datos}) {
  const tabla = datos.tabla.map(data=><tr key={data[0]}><td>{data[0]}</td><td>{data[1]}</td><td>{data[2]}</td><td>{data[3]}</td></tr>);
  return (
    <>
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
    </>
  )
}

export default Tabla