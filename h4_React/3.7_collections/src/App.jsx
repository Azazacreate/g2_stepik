import React from 'react';
import './App.css';
import Posts from './components/Posts'

export default class App extends React.Component {
  state = {
    posts: [
      {id: 'abc1', name: 'JS bacis'},
      {id: 'abc2', name: 'JS advanced'},
      {id: 'abc3', name: 'React'},
    ]
  }

  handle__something = () => {
    // this.setState({})
    console.log('App.jsx setState update')
  }


  render() {
    const {posts} = this.state;

    return (
      <div className="App">
        <Posts posts={posts} cb={this.handle__something} />
      </div>
    );
  }
}