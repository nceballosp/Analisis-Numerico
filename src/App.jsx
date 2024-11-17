import { useState,useRef} from 'react'
import './App.css'
import Tabla from './Tabla'
import Form from './Form'
import Grafico from './Grafico';
import Instrucciones from './Instrucciones';
function App() {
  // const [currentFunc,setCurrentFunc]= useState(null);
  const appletref = useRef(null);
  const [datos,setDatos] = useState(null);
  const handleData = (respuesta) => {
    setDatos(respuesta);
  };
  var params = {"appName": "graphing", "showToolBar": true, "showAlgebraInput": true, "showMenuBar": true,"scaleContainerClass":"ggb-element" };
  var applet = new GGBApplet(params, true);
  window.addEventListener("load", function() {
      applet.inject(appletref.current);
  });
  const graphFunction = (func) => {

    try{
      if(applet && applet.getAppletObject()){
        const ggbObject = applet.getAppletObject();
        ggbObject.evalCommand(`f(x)=${func}`);
      }
    }
    catch(error){
      console.error("Error al graficar:", error);
      alert("La función ingresada no es válida.");
    }
  }
  return (
    <>
      <h1>Proyecto Analisis Numerico</h1>
      <div className="content">
      <Form imprTabla={handleData} imprGraph={graphFunction}/>
      <div id="resultados">
        {datos && <Tabla datos={datos} tipo={'NonLinear'}/>}
      </div>
      <Instrucciones/>
      </div>        <div className="ggb-element" ref={appletref}></div>
    </>
  )
}

export default App
