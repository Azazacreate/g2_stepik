import React from 'react';
import './App.css';

class App extends React.Component {
  state = {
    posts: [],
    loading: true,
    comments: [],
  }

  decrement = () => {
    this.setState({count: this.state.count - 1});
  }
  increment = () => {
    this.setState({count: this.state.count + 1});
  }
  componentDidMount() {
    console.log('componentDidMount')
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then(response => response.json())
      .then(data => this.setState({posts: data, loading: false}))

      this.timerId = setInterval(() => {
        fetch('https://jsonplaceholder.typicode.com/comments')
          .then(response => response.json())
          .then(data => this.setState({comments: data}))
      }, 3000)
  }
  componentDidUpdate() {
    console.log('componentDidUpdate')
  }
  componentWillUnmount() {
    clearInterval(this.timerId);
  }

  render() {
    return (
      <div className="App">
        {this.state.loading ? <h3>Loading ...</h3> 
        : <h3>{this.state.posts.length} was loaded</h3>
        }
      </div>
    );
  }
}
export default App;