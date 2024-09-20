import { useState } from 'react'
import './App.css'
import Tabla from './Tabla'
import Form from './Form'

function App() {
  const [datos,setDatos] = useState(null);
  const handleData = (respuesta) => {
    setDatos(respuesta);
  };

  return (
    <>
      <h1>Proyecto Analisis Numerico</h1>
      <div className="content">
      <Form imprTabla={handleData}/>
      <div id="resultados">
        {datos && <Tabla datos={datos}/>}
      </div>
      </div>
    </>
  )
}

export default App
