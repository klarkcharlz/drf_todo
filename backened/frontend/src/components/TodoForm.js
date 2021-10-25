import React from 'react'


class TodoForm extends React.Component {
    constructor(props) {
        super(props)
        console.log(props.projects)
        console.log(props.users)
        this.state = {project: props.projects[0].id, user: props.users[0].id, text: ''}
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        console.log(this.state.project)
        console.log(this.state.user)
        console.log(this.state.text)
        this.props.createTodo(this.state.project, this.state.user, this.state.text)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>

                <div>
                    <label for="project">Project</label>
                    <select name="project" className='form-control' onChange={(event) => this.handleChange(event)}>
                        {this.props.projects.map((item) => <option value={item.id}>{item.name}</option>)}
                    </select>
                </div>

                <div>
                    <label for="user">User</label>
                    <select name="user" className='form-control' onChange={(event) => this.handleChange(event)}>
                        {this.props.users.map((item) => <option value={item.id}>{item.username}</option>)}
                    </select>
                </div>

                <div className="form-group">
                    <label for="text">Text</label>
                    <input type="text" className="form-control" name="text" value={this.state.text}
                           onChange={(event) => this.handleChange(event)}/>
                </div>

                <input type="submit" className="btn btn-primary" value="Save"/>
            </form>
        );
    }
}

export default TodoForm
