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

  remove__post = (id) => {
    this.setState({posts: this.state.posts.filter(post => post.id !== id)});
  }


  render() {
    const {posts} = this.state;

    return (
      <div className="App">
        <Posts posts={posts} remove__post={this.remove__post} />
      </div>
    );
  }
}