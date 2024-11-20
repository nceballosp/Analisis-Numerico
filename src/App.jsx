import {useState,useRef, useEffect} from 'react'
import './App.css'
import Tabla from './Tabla'
import Form from './Form'
import Grafico from './Grafico';
import Instrucciones from './Instrucciones';

function App({type}) {
  const appletref = useRef(null);
  const [datos,setDatos] = useState(null);

  const handleData = (respuesta) => {
    setDatos(respuesta);
  };

  const params = {"appName": "graphing", "showToolBar": true, "showAlgebraInput": true, "showMenuBar": true,"scaleContainerClass":"ggb-element" };
  const applet = new GGBApplet(params, true);
  
  // window.addEventListener("load", function() {
  //     applet.inject(appletref.current);
  // });

  useEffect(() => {
    if (appletref.current) {
        applet.inject(appletref.current);
    }
}, []);

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
      <div className="content">
      <Form imprTabla={handleData} imprGraph={graphFunction} tipo={type} />
      <div id="resultados">
        {datos && <Tabla datos={datos} tipo={type}/>}
      </div>
      <Instrucciones/>
      </div>        
      <div className="ggb-element" ref={appletref}></div>
    </>
  )
}

export default App
