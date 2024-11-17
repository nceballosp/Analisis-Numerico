import React from 'react'
import { useState,useEffect,useRef } from 'react'
import './Form.css'

function Form({imprTabla,imprGraph}) {
const funcref = useRef(null);
const [eleccion,setEleccion] = useState('Biseccion');
const formRef = useRef();
const handleSubmit = () => {
  const datos = new FormData(formRef.current);
  imprGraph(funcref.current.value);
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
        <option value="Raices-Multiples-1">Raices Multiples 1</option>
        <option value="Raices-Multiples-2">Raices Multiples 2</option>
        <option value="SOR">SOR</option>
        <option value="GaussSeidel">Gauss Seidel</option>
        <option value="Jacobi">Jacobi</option>
      </select>

      <label htmlFor="ErrorType">Tipo de Error</label>
      <select name="ErrorType" id="ErrorType">
        <option value="Abs">Error Absoluto</option>
        <option value="Rel">Error Relativo</option>
      </select>

      {(eleccion !== 'GaussSeidel'  && eleccion !== 'Jacobi' && eleccion !== 'SOR') && 
        <>
          <label htmlFor="func">Funcion</label>
          <input type="text" name="func" id="func" placeholder="Ingrese la funcion a evaluar" ref={funcref} />
        </>
      }
      
      <label htmlFor="Tol">Tolerancia</label>
      <input autoComplete='OFF' type="text" name='Tol' id='Tol' placeholder='Tol'/>

      <label htmlFor="Niter">Numero de Iteraciones</label>
      <input autoComplete='OFF' type="text" name='Niter' id='Niter' placeholder='Niter'/>

      {(eleccion==='Biseccion' || eleccion === 'Regla-Falsa') &&
      <>
      <label htmlFor="Xi">Inicio de Intervalo</label>
      <input autoComplete='OFF' type="text" name='Xi' id='Xi' placeholder='Xi' />
      </>
      }

      {(eleccion==='Biseccion' || eleccion === 'Regla-Falsa') &&
      <>
      <label htmlFor="Xf">Fin de Intervalo</label>
      <input autoComplete='OFF' type="text" name='Xf' id='Xf' placeholder='Xf' />
      </>
      }

      {eleccion==='Punto-Fijo' &&
      <>
      <label htmlFor="g">g(x)</label>
      <input autoComplete='OFF' type="text" name='g' id='g' placeholder='g(x)'/>
      </>
      }

     {(eleccion==='Punto-Fijo' || eleccion==='Newton' || eleccion === 'Secante' || eleccion === 'Raices-Multiples-1' || eleccion === 'Raices-Multiples-2') &&
      <>
      <label htmlFor="X0">X0</label>
      <input autoComplete='OFF' type="text" name='X0' id='X0' placeholder='X0' />
      </>
      }

      {eleccion === 'Secante' &&
      <>
      <label htmlFor="X1">X1</label>
      <input autoComplete='OFF' type="text" name='X1' id='X1' placeholder='X1' />
      </>
      }   

      {eleccion === 'Raices-Multiples-1' &&
      <>
      <label htmlFor="m">Multiplicidad</label>
      <input autoComplete='OFF' type="text" name='m' id='m' placeholder='m' />
      </>
      }
      
      {eleccion === 'Newton' &&
      <>
      <label htmlFor="df">Df</label>
      <input autoComplete='OFF' type="text" name='df' id='df' placeholder='df' />
      </>
      }
      

      {eleccion === 'SOR' && 
        <>
          <label htmlFor="X0">X0</label>
          <input autoComplete="OFF" type="text" name="X0" id="X0" placeholder="X0" />

          <label htmlFor="A">A</label>
          <input autoComplete="OFF" type="text" name="A" id="A" placeholder="A" />

          <label htmlFor="b">b</label>
          <input autoComplete="OFF" type="text" name="b" id="b" placeholder="b" />

          <label htmlFor="w">w</label>
          <input autoComplete="OFF" type="text" name="w" id="w" placeholder="w" />
        </>
      }

      {eleccion === 'Jacobi' && 
        <>
          <label htmlFor="X0">X0</label>
          <input autoComplete="OFF" type="text" name="X0" id="X0" placeholder="X0" />

          <label htmlFor="A">A</label>
          <input autoComplete="OFF" type="text" name="A" id="A" placeholder="A" />

          <label htmlFor="b">b</label>
          <input autoComplete="OFF" type="text" name="b" id="b" placeholder="b" />
        </>}

        {eleccion === 'GaussSeidel'  && 
        <>
          <label htmlFor="X0">X0</label>
          <input autoComplete="OFF" type="text" name="X0" id="X0" placeholder="X0" />

          <label htmlFor="A">A</label>
          <input autoComplete="OFF" type="text" name="A" id="A" placeholder="A" />

          <label htmlFor="b">b</label>
          <input autoComplete="OFF" type="text" name="b" id="b" placeholder="b" />
        </>}




      <button type='button' onClick={handleSubmit}>Enviar</button>
    </form>
    
  )
}

export default Form
