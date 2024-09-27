import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { BrowserRouter,Routes, Route } from 'react-router-dom';
import Run_Predictor from './Components/run_predictor';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <Routes>
      <Route path='/' element={<Run_Predictor/>}></Route>
    </Routes>
  </BrowserRouter>
);