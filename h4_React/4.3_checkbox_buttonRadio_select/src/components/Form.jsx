import React from "react";
export default class Form extends React.Component {
    state = {
        nameFirst: '',
        email: '',
        message: '',
        select: '',
        subscription: false,
        gender: 'none',
    }

    handleСhange = (event) => {
        this.setState({[event.target.name]:  event.target.value})
    }
    handleСhange__checkbox = (event) => {
        this.setState({[event.target.name]:  event.target.checked})
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
        }
    }


    render() {
        const {nameFirst, email, message, select, subscription, gender} = this.state;
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
                <br />
                <textarea name="message" value={message} onChange={this.handleСhange} />
                <br />
                <select name="select" value={select} onChange={this.handleСhange} >
                    <option value="" disabled>choice</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                </select>
                <br />
                <label htmlFor="">
                    <input type="checkbox" name="subscription" checked={subscription} onChange={this.handleСhange__checkbox} />
                    checkbox
                </label>
                <br />
            <input type="radio" name="gender" value='male' onChange={this.handleСhange}  checked={gender === 'male'} /> Male
            <input type="radio" name="gender" value='female' onChange={this.handleСhange} checked={gender === 'female'} /> Female
            </div>
        )
    }
}