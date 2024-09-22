import React from 'react'
import { useState,useEffect,useRef } from 'react'
import './Form.css'

function Form({imprTabla}) {
const [eleccion,setEleccion] = useState('Biseccion');
const formRef = useRef();
const handleSubmit = () => {
  const datos = new FormData(formRef.current);
fetch(`http://127.0.0.1:5000/${eleccion}`,{
  method: 'POST',
  body: datos
})
.then(response => response.json())
.then(respuesta => {
  imprTabla(respuesta);
})
.catch(error =>
{
  alert('Servidor backend no responde,revisar');
  // console.log('Fallo el fetch');  
}
)


}
  return (
    
    <form action="" id='formulario' ref={formRef}>
      <label htmlFor="metodo">Seleccione el metodo a ejecutar</label>
     <select name="metodo" id="metodo" onInput={()=>setEleccion(()=> metodo.value)} >
        <option value="Biseccion">Biseccion</option>
        <option value="Regla-Falsa">Regla Falsa</option>
        <option value="Punto-Fijo">Punto Fijo</option>
        <option value="Secante">Secante</option>
        <option value="Newton">Newton</option>
        <option value="Raices-Multiples">Raices Multiples</option>
      </select>

      <label htmlFor="ErrorType">Tipo de Error</label>
      <select name="ErrorType" id="ErrorType">
        <option value="Abs">Error Absoluto</option>
        <option value="Rel">Error Relativo</option>
      </select>

      <label htmlFor="func">Funcion</label>
      <input type="text" name="func" id="func" placeholder='Ingrese la funcion a evaluar'/>
      
      <label htmlFor="Tol">Tolerancia</label>
      <input type="text" name='Tol' id='Tol' placeholder='Tol'/>

      <label htmlFor="Niter">Numero de Iteraciones</label>
      <input type="text" name='Niter' id='Niter' placeholder='Niter'/>

      {(eleccion==='Biseccion' || eleccion === 'Regla-Falsa') &&
      <>
      <label htmlFor="Xi">Inicio de Intervalo</label>
      <input type="text" name='Xi' id='Xi' placeholder='Xi' />
      </>
      }

      {(eleccion==='Biseccion' || eleccion === 'Regla-Falsa') &&
      <>
      <label htmlFor="Xf">Fin de Intervalo</label>
      <input type="text" name='Xf' id='Xf' placeholder='Xf' />
      </>
      }

      {eleccion==='Punto-Fijo' &&
      <>
      <label htmlFor="g">gdex</label>
      <input type="text" name='g' id='g' placeholder='g(x)'/>
      </>
      }

     {(eleccion==='Punto-Fijo' || eleccion==='Newton' || eleccion === 'Secante') &&
      <>
      <label htmlFor="X0">X0</label>
      <input type="text" name='X0' id='X0' placeholder='X0' />
      </>
      }

      {eleccion === 'Secante' &&
      <>
      <label htmlFor="X1">X1</label>
      <input type="text" name='X1' id='X1' placeholder='X1' />
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
      <button type='button' onClick={handleSubmit}>Enviar</button>
    </form>
    
  )
}

export default Form