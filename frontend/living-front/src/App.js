import SelectImg from './pages/identify/SelectImg';
import Header from './pages/Header';
import Apitest from './pages/Apitest';
import {Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import IdentyResult from './pages/identify/IndentyResult';
import Login from './pages/Login';
import DetailPlant from './pages/dictionary/DetailPlant';
import Plants from './pages/dictionary/Plants';

const App = () => {
    return (
        <>
        <Header/>
        <Routes>
            <Route path="/" element={<Home/>}/>
            <Route path="/apitest" element={<Apitest/>}/>
            <Route path="/selectimg" element={<SelectImg/>}/>
            <Route path ="/identyResults" element={<IdentyResult/>} />
            <Route path ="/login" element={<Login/>} />
            <Route path ="/detailplant" element={<DetailPlant/>} />
            <Route path ="/plantList" element={<Plants/>} />
        </Routes>
        </>
    );
  


};
export default App;