import React from 'react'

function Home() {
  return (
    <>
    <p style={{fontSize:25, marginTop:"2%", textAlign:'center'}}>Calculadora Metodos Numericos</p>
    <div style={{display:'flex', flexDirection: 'row', width: "100%", justifyContent:'space-evenly', margin:"3%"}}>
    <img src="/public/h2.jpg" alt="" style={{height:400}} />
    <p>Hola, bievenido a nuestra pagina
    <br />Aqui vas a encontrar una calculadora para los metodos,
    <br /> No lineales, Lineales y de Interpolacion.</p>
    </div>
    </>
  )
}

export default Home