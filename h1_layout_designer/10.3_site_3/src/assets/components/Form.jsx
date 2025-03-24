import React, { useState } from "react";

const Form = () => {
    const [login, setLogin] = useState('');
    const [email, setEmail] = useState('');
    const [agree_withTerms, setAgreeWithTerms] = useState(false);

    const handleChange = (event) => {
        const { name, value } = event.target;
        if (name === "login") setLogin(value);
        if (name === "email") setEmail(value);
    };

    const handleChangeCheckbox = (event) => {
        setAgreeWithTerms(event.target.checked);
    };

    const handleSubmit = () => {
        const isMailValid = !/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email.toLocaleLowerCase());
        
        if (login.length < 5) {
            alert('Your login can\'t be less than 5-letters');
        }
        if (isMailValid) {
            alert('Your email is not valid');
            return;
        }
        if (email.length < 1) {
            alert('Email or login is empty');
            return;
        }
        if (!agree_withTerms) {
            alert('You should accept all terms and conditions');
            return;
        }

        setEmail('');
        setAgreeWithTerms(false);
        alert('Данные отправлены на сервер!');
    };

    return (
        <div>
            <input 
                type="text" 
                name="login"
                placeholder="login"
                value={login}
                onChange={handleChange}
            />
            <br />
            <input 
                type="email" 
                name="email" 
                placeholder="email" 
                value={email}
                onChange={handleChange}
            />
            <br />
            <label htmlFor="checkboX">
                <input 
                    type="checkbox" 
                    name="agree_withTerms" 
                    checked={agree_withTerms} 
                    onChange={handleChangeCheckbox}
                />
                I agree with terms and conditions
            </label>
            <br />
            <button onClick={handleSubmit}>register</button>
        </div>
    );
};
export default Form;