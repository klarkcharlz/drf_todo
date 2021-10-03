import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'
import ProjectList from './components/Projects.js'
import UseProjectsList from './components/UserProjects.js'
import TodoList from './components/Todo.js'
import Footer from './components/Footer.js'
import Menu from './components/Menu.js'
import axios from 'axios'
import {HashRouter, Route, Link, Switch, Redirect, BrowserRouter} from 'react-router-dom'


const NotFound = ({location}) => {
    return (<div>Page not found: {location.pathname}</div>)
}

class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data.results
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo/')
            .then(response => {
                const todos = response.data.results
                this.setState(
                    {
                        'todos': todos
                    }
                )
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <Menu/>

                    <Switch>
                        <Route path='/' exact component={() => <UserList users={this.state.users}/>}/>
                        <Route path='/projects/' component={() => <ProjectList projects={this.state.projects}/>}/>
                        <Route path='/todo/' component={() => <TodoList todos={this.state.todos}/>}/>

                        <Route path='/user/:id' component={() => <UseProjectsList projects={this.state.projects}/>}/>


                        <Redirect from='/users' to='/'/>
                        <Route component={NotFound}/>
                    </Switch>

                    <Footer data={"User Api"}/>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
