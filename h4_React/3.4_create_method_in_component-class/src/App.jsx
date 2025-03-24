import React from 'react';
import './App.css';

class App extends React.Component {
  state = {
    count: 0
  }

  decrement = () => {
    this.setState({count: this.state.count - 1});
  }
  increment = () => {
    this.setState({count: this.state.count + 1});
  }

  render() {
    return (
      <div className="App" style={countStyle}>
        <p>app: Clicker</p>
        <button onClick={this.decrement}>-</button>
          <span style={{margin: '0 1rem', display: 'inline-block'}}>
            {this.state.count}
          </span>
        <button onClick={this.increment}>+</button>
      </div>
    );
  }
}
export default App;


const countStyle = {margin: 'auto', width: '300px'}