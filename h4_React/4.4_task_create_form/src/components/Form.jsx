import React from "react";
export default class Form extends React.Component {
    state = {
        login: '',
        email: '',
        agree_withTerms: false,
        agree__withTerms: false,
    }


    handleСhange = (event) => {
        this.setState({[event.target.name]:  event.target.value})
    }
    handleСhange__checkbox = (event) => {
        this.setState({[event.target.name]:  event.target.checked})
    }
    handleSubmit = () => {
        const is__mailValid = !/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(this.state.email.toLocaleLowerCase())
        const is__checkboxValid = this.state.agree_withTerms;

        if (this.state.login.length < 5) {
            alert('Your login can\'t be less than 5-letters')
        }
        if (is__mailValid) {
            alert('Your email  isnot valid')
            return
        }
        if (this.state.email.length < 1) {
            alert('email or login is empty')
            return
        }
        if (!is__checkboxValid) {
            alert('You should accept all-terms and conditions')
            return
        }
        this.setState({
            email: '', 
            agree__withTerms: false,
        })
        alert('данные отправлены на-сервер !');
    }


    render() {
        const {login, email, agree_withTerms} = this.state;
        return (
            <div>
                <input 
                    type="text" 
                    name="login"
                    placeholder="login"
                    value={login}
                    onChange={this.handleСhange}
                    onBlur={this.validate_name}
                />
                <br />
                <input 
                    type="email" 
                    name="email" 
                    placeholder="email" 
                    value={email}
                    onChange={this.handleСhange}
                    onBlur={this.handleСhange}
                />
                <br />
                <label htmlFor="checkboX">
                    <input 
                        type="checkbox" 
                        name="agree_withTerms" 
                        checked={agree_withTerms} 
                        onChange={this.handleСhange__checkbox}
                    />
                    I agree with terms and conditions
                </label>
                <br />
                <button onClick={this.handleSubmit}>register</button>
            </div>
        )
    }
}