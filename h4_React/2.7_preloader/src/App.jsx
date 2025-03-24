import React from 'react';
import Book from './Book';
import Preloader from './Preloader';
// import logo from './logo.svg';
import './App.css';

const App = (props) => {
 return props.is__loading ? (
  <Preloader />
 )
 : (<div>
    <Book name='JS' year='2018' price='1000-rub'/>
    <Book name='Vue' year='2019' price='1100-rub'/>
    <Book year='2020' price='1200-rub'> 
      <b>this is children</b>
    </Book>
 </div>)
};

export default App;
