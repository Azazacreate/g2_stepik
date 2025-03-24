import React from 'react';
import './App.css';

class App extends React.Component {
  state = {
    count: 0
  }

  handleClick1 = () => {
    this.setState({count: this.state.count + 1});
  }
  handleClick2 = () => {
    this.setState({count: this.state.count - 1});
  }

  render() {
    return (
      <div className="App">
        <p>app: Clicker</p>
        <button onClick={this.handleClick1}>
          +
        </button>
        <p>{this.state.count}</p>
        <button onClick={this.handleClick2}>
          -
        </button>
      </div>
    );
  }
}

export default App;