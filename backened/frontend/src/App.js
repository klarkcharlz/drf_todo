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
import TodoForm from "./components/TodoForm";
import ProjectForm from "./components/ProjectFrom";


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

    deleteProject(id) {
        const headers = this.getHeaders()
        axios.delete(`http://127.0.0.1:8000/api/projects/${id}/`, {headers})
            .then(response => {
                this.setState({projects: this.state.projects.filter((item) => item.id !== id)})
            }).catch(error => console.log(error))
    }

    deleteTodo(id) {
        const headers = this.getHeaders()
        axios.delete(`http://127.0.0.1:8000/api/todo/${id}/`, {headers})
            .then(response => {
                this.loadData();
            }).catch(error => console.log(error))
    }

    createTodo(project, user, text) {
        const headers = this.getHeaders()
        const data = {project: project, user: user, text: text}
        axios.post(`http://127.0.0.1:8000/api/create_todo/`, data, {headers})
            .then(response => {
                console.log(response.data)
                this.loadData();
            }).catch(error => console.log(error))
    }

    createProject(name, url, users) {
        const headers = this.getHeaders()
        const data = {name: name, url: url, users: users}
        axios.post(`http://127.0.0.1:8000/api/create_project/`, data, {headers})
            .then(response => {
                console.log(response.data)
                this.loadData();
            }).catch(error => console.log(error))
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

                    <Menu obj={this}/>

                    <Switch>
                        <Route path='/' exact component={() => <UserList users={this.state.users}/>}/>
                        <Route path='/projects/' exact component={() => <ProjectList projects={this.state.projects}
                                                                               deleteProject={(id) => this.deleteProject(id)}/>}/>
                        <Route path='/todo/' exact component={() => <TodoList todos={this.state.todos}
                                                                              deleteTodo={(id) => this.deleteTodo(id)}/>}/>
                        <Route path='/user/:id' component={() => <UseProjectsList projects={this.state.projects}/>}/>
                        <Redirect from='/users' to='/'/>
                        <Route path='/login' exact component={() => <LoginForm
                            getToken={(login, password) => this.getToken(login, password)}/>}/>

                        <Route exact path='/todo/create' component={() => <TodoForm
                            createTodo={(project, user, text) => this.createTodo(project, user, text)}
                            projects={this.state.projects} users={this.state.users}/>}/>

                        <Route exact path='/project/create' component={() => <ProjectForm
                            createProject={(name, url, users) => this.createProject(name, url, users)}
                            users={this.state.users}/>}/>
                        <Route component={NotFound}/>
                    </Switch>

                    <Footer data={"User Api"}/>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
