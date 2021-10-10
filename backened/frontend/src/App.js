import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'
import ProjectList from './components/Projects.js'
import UseProjectsList from './components/UserProjects.js'
import TodoList from './components/Todo.js'
import Footer from './components/Footer.js'
import Menu from './components/Menu.js'
import LoginForm from './components/LoginForm.js'
import axios from 'axios'
import {Route, Link, Switch, Redirect, BrowserRouter} from 'react-router-dom'


const NotFound = ({location}) => {
    return (<div>Page not found: {location.pathname}</div>)
}

class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'token': ''
        }
    }

    getToken(login, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {"username": login, "password": password})
            .then(response => {
                console.log(response.data.token)
                localStorage.setItem('token', response.data.token)
                this.setState({'token': response.data.token}, this.loadData)
            })
            .catch(error => alert("Wrong password"))
    }

    logout() {
        localStorage.setItem('token', '')
        this.setState({'token': ''}, this.loadData)
    }

    isAuthenticated() {
        return !!this.state.token
    }

    getHeaders() {
        if (this.isAuthenticated()) {
            return {'Authorization': 'Token ' + this.state.token}
        }
        return {}
    }

    loadData() {
        const headers = this.getHeaders()

        axios.get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                const users = response.data.results
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => {
            console.log(error)
            this.setState(
                {
                    'users': []
                }
            )
        })

        axios.get('http://127.0.0.1:8000/api/projects/', {headers})
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => {
            console.log(error)
            this.setState(
                {
                    'projects': []
                }
            )
        })

        axios.get('http://127.0.0.1:8000/api/todo/', {headers})
            .then(response => {
                const todos = response.data.results
                this.setState(
                    {
                        'todos': todos
                    }
                )
            }).catch(error => {
            console.log(error)
            this.setState(
                {
                    'todos': []
                }
            )
        })
    }

    componentDidMount() {
        const token = localStorage.getItem('token')
        console.log(token)
        this.setState({'token': token}, this.loadData)
    }

    render() {
        return (
            <div>
                <BrowserRouter>

                    {this.isAuthenticated() ?
                        <button onClick={() => this.logout()}>Logout</button> :
                        <Link to='/login'>Login</Link>
                    }

                    <Menu/>

                    <Switch>
                        <Route path='/' exact component={() => <UserList users={this.state.users}/>}/>
                        <Route path='/projects/' component={() => <ProjectList projects={this.state.projects}/>}/>
                        <Route path='/todo/' component={() => <TodoList todos={this.state.todos}/>}/>
                        <Route path='/user/:id' component={() => <UseProjectsList projects={this.state.projects}/>}/>
                        <Redirect from='/users' to='/'/>
                        <Route path='/login' exact component={() => <LoginForm
                            getToken={(login, password) => this.getToken(login, password)}/>}/>
                        <Route component={NotFound}/>
                    </Switch>

                    <Footer data={"User Api"}/>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
