import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
// import App from './App';
import reportWebVitals from './reportWebVitals';


const Book = (props) => {
  return <div>
    <h2>{props.name}</h2>
    <p>{props.year}</p>
    <p>{props.price}</p>
  </div>
}

const App = () => {
 return <div>
    <Book name='JS' year='2018' price='1000-rub'/>
    <Book name='Vue' year='2019' price='1100-rub'/>
    <Book name='React' year='2020' price='1200-rub'/>
 </div>
} 

// JSX
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
    <h1 name='name_1'>h1</h1>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
