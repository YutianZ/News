import LoginForm from './LoginForm';
import React from 'react';

//This component handles the logic part of Login
//export default when only export one thing
// use { bala, bala } instead
//can import jquery in index.html if necessary

class LoginPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            errors: {
            },
            user: {
                email: '',
                password: ''    
            }
        };
    }

    processForm(event) {
        event.preventDefault();
        const email = this.state.user.email;
        const password = this.state.user.password;
        //TODO: post the login data to server then get response
        console.log("email", email);
        console.log("password", password);
    }

    changeUser(event) {
        const field = event.target.name;
        const user = this.state.user;
        user[field] = event.target.value;

        this.setState({user});    
    }

    render() {
        return(
            <LoginForm 
                onSubmit={(e) => this.processForm(e)}
                onChange={(e) => this.changeUser(e)}
                errors={this.state.errors} />
        )
    }
}

export default LoginPage;