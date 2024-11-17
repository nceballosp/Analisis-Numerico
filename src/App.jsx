import { useState,useRef} from 'react'
import './App.css'
import Tabla from './Tabla'
import Form from './Form'
import Grafico from './Grafico';
import Instrucciones from './Instrucciones';
function App() {
  var applet = useRef(null);
  const [datos,setDatos] = useState(null);
  const handleData = (respuesta) => {
    setDatos(respuesta);
  };
  var params = {"appName": "graphing", "showToolBar": true, "showAlgebraInput": true, "showMenuBar": true,"scaleContainerClass":"ggb-element" };
  var applet = new GGBApplet(params, true);
  window.addEventListener("load", function() {
      applet.inject(applet.current);
  });
  return (
    <>
      <h1>Proyecto Analisis Numerico</h1>
      <div className="content">
      <Form imprTabla={handleData}/>
      <div id="resultados">
        {datos && <Tabla datos={datos}/>}
      </div>
      <Instrucciones/>
      </div>
        <div class="ggb-element" ref={applet}></div>
    </>
  )
}

export default App
