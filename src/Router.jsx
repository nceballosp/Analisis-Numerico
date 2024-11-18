import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css'
import Navbar from './components/Navbar'
import Home from './pages/Home';
import App from './App';


function Router() {
  return (
    <>
    <BrowserRouter>
        <Navbar/>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/lineares" element={<App type={'Linear'} />} />
          <Route path="/nolineares" element={<App type={'NoLinear'} />} />
          <Route path="/interpolacion" element={<App type={'Interpolacion'} />} />
        </Routes>
    </BrowserRouter>
    </>
  )
}

export default Router
