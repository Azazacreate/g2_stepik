import React from "react";
export default class Form extends React.Component {
    state = {
        nameFirst: '',
        email: '',
    }

    handleСhange = (event) => {
        this.setState({[event.target.name]:  event.target.value})
    }
    validate_name = () => {
        if (this.state.nameFirst.length < 5) {
            alert('Your nameFirst can\'t be less than 5-letters')
        }
    }
    validate_email = () => {
        console.log(this.state.email, /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(this.state.email))
        if (!/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(this.state.email)) {
            alert('email isn\'t valid')
    }}
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
                    onBlur={this.validate_name}
                />
                <input 
                    type="email" 
                    name='email' 
                    placeholder="email"
                    value={email}
                    onChange={this.handleСhange}
                    onBlur={this.validate_email}
                />
            </div>
        )
    }
}