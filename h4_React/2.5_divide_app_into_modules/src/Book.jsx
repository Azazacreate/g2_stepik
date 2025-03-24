import React from 'react';


const Book = (props) => {
    return (
    <div className={props.name}>
      <h2>language is {props.name ? <span>{props.name}</span> : 'nameDefault'}</h2>
      <p>{props.year}</p>
      <p>{props.price}</p>
      <p>{props.children}</p>
    </div>
    );
} 
export {Book};