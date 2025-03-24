import React from "react";


export default class Form extends React.Component {
    state = {
        nameFirst: '',
        email: '',
    }

    handleСhange = (event) => {
        this.setState({[event.target.name]:  event.target.value})
    }
    render() {
        const {nameFirst, email} = this.state;
        return (
            <div>
                <input 
                    type="text" 
                    name='nameFirst' 
                    placeholder="nameFirst"
                    value={nameFirst}
                    onChange={this.handleСhange}
                />
                <input 
                    type="email" 
                    name='email' 
                    placeholder="email"
                    value={email}
                    onChange={this.handleСhange}
                />
            </div>
        )
    }
}