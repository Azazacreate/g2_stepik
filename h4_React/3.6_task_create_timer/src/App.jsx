import React from 'react';
import './App.css';

export default class App extends React.Component {
  state = {
    count: 0,
    is__counting: false,
    localStorage: 0,
  }

  componentDidMount() {
    const user_count = localStorage.getItem('timer');
    if (user_count) {
      this.setState({count: +user_count})
    }
  }

  componentDidUpdate() {
    localStorage.setItem('timer', this.state.count)
  }

  componentWillUnmount() {
    clearInterval(this.counter_id);
  }

  handle_start = () => {
    this.setState({is__counting: true})
    this.counter_id = setInterval(() => {
      this.setState({count: this.state.count + 1})
    }, 1000)
    
  }
  handle_stop = () => {
    this.setState({is__counting: false})
    clearInterval(this.counter_id);
  }
  handle_reset = () => {
    this.setState({count: 0, is__counting: false})
    clearInterval(this.counter_id);
  }


  render() {
    return (
      <div className="App">
        <h1>timer-React</h1>
        <h3>{this.state.count}</h3>
        {!this.state.is__counting ? 
          <button onClick={this.handle_start}>start</button> 
          : 
          <button onClick={this.handle_stop}>stop</button>}
        <button onClick={this.handle_reset}>reset</button>
      </div>
    );
  }
}