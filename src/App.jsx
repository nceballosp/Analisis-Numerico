import { useState } from 'react'
import './App.css'
import Tabla from './Tabla'
import Form from './Form'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1>Proyecto Analisis Numerico</h1>
      <div className="content">
      <Form/>
      <div id="resultados"></div>
      </div>
    </>
  )
}

export default App
