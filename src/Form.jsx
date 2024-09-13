import React from 'react'
import { useState,useEffect } from 'react'
import './Form.css'

function Form() {
const [eleccion,setEleccion] = useState('Biseccion');
  return (
    
    <form action="" id='formulario'>
     <select name="metodo" id="metodo" onInput={()=>setEleccion(()=> metodo.value)} >
        <option value="Biseccion">Biseccion</option>
        <option value="Regla Falsa">Regla Falsa</option>
        <option value="Punto Fijo">Punto Fijo</option>
        <option value="Newton">Newton</option>
        <option value="Raices Multiples">Raices Multiples</option>
      </select>

      <label htmlFor="func">Funcion</label>
      <input type="text" name="func" id="func" placeholder='Ingrese la funcion a evaluar'/>
      
      <label htmlFor="Tol">Tolerancia</label>
      <input type="text" name='Tol' id='Tol' placeholder='Tol'/>

      <label htmlFor="Niter">Numero de Iteraciones</label>
      <input type="text" name='Niter' id='Niter' placeholder='Niter'/>

      {(eleccion==='Biseccion' || eleccion === 'Regla Falsa') &&
      <>
      <label htmlFor="Xi">Inicio de Intervalo</label>
      <input type="text" name='Xi' id='Xi' placeholder='Xi' />
      </>
      }

      {(eleccion==='Biseccion' || eleccion === 'Regla Falsa') &&
      <>
      <label htmlFor="Xf">Fin de Intervalo</label>
      <input type="text" name='Xf' id='Xf' placeholder='Xf' />
      </>
      }

      {eleccion==='Punto Fijo' &&
      <>
      <label htmlFor="g">gdex</label>
      <input type="text" name='g' id='g' placeholder='g(x)'/>
      </>
      }

     {(eleccion==='Punto Fijo' || eleccion==='Newton') &&
      <>
      <label htmlFor="X0">X inicial</label>
      <input type="text" name='X0' id='X0' placeholder='X0' />
      </>
      }
      
      {/* {(eleccion==='Newton' || eleccion==='Raices Multiples') &&
      <>
      <label htmlFor="df">Derivada f</label>
      <input type="text" name='df' id='df' placeholder='df'/>
      </>
      } */}
      
      {/* {eleccion==='Raices Multiples' && 
      <>
      <label htmlFor="dff">Seguna Derivada f</label>
      <input type="text" name='dff' id='dff' placeholder='dff'/>
      </>
      } */}
    </form>
    
  )
}

export default Form