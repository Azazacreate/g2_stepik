import React from 'react';


const Book = (props) => {
  return props.name ? (
  <div className={props.name}>
    <h2>language is {props.name}</h2>
    <p>{props.year}</p>
    <p>{props.price}</p>
    <p>{props.children}</p>
  </div>
  )
  : null;
} 
export default Book;