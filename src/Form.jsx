import React from 'react'
import { useState,useEffect } from 'react'
import './Form.css'

function Form() {
useEffect(()=>{
  const metodo = document.querySelector('#metodo');
  console.log(metodo);
})
const [eleccion,setEleccion] = useState('Biseccion');
  return (
    
    <form action="" id='formulario'>
     <select name="metodo" id="metodo" onInput={()=>setEleccion((method)=> metodo.value)} >
        <option value="Biseccion">Biseccion</option>
        <option value="Busquedas Incrementales">Busquedas Incrementales</option>
        <option value="Newton">Newton</option>
      </select>
      {/* Completar lo inputs con condicionales para mostarse en los metodos que aplican */}
      {/* Agregar labels a cada input */}
      <input type="text" name="func" id="func" placeholder='Ingrese la funcion a evaluar'/>
      {/* ejemplo de conditional rendering */}
      {eleccion==='Biseccion' && 
      <>
      <label htmlFor="X0">Inicio de Intervalo</label>
      <input type="text" name='X0'placeholder='X0' />
      </>
      }
     
    </form>
    
  )
}

export default Form