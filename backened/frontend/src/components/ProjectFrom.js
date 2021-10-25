import React from 'react'


class ProjectForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {name: '', url: '', users: props.users[0].id,}
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleChangeOptions(event) {
        let [...options] = [...event.target.options]
            .filter(option => option.selected)
            .map(x => parseInt(x.value))

        console.log(options)

        this.setState(
            {
                [event.target.name]: options
            }
        );
    }

    handleSubmit(event) {
        console.log(this.state.name)
        console.log(this.state.url)
        console.log(this.state.users)
        this.props.createProject(this.state.name, this.state.url, this.state.users)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>

                <div className="form-group">
                    <label for="name">Name</label>
                    <input type="text" className="form-control" name="name" value={this.state.name}
                           onChange={(event) => this.handleChange(event)}/>
                </div>

                <div className="form-group">
                    <label for="url">URL</label>
                    <input type="text" className="form-control" name="url" value={this.state.url}
                           onChange={(event) => this.handleChange(event)}/>
                </div>

                <div>
                    <label for="users">Users</label>
                    <select size="3" multiple name="users" className='form-control'
                            onChange={(event) => this.handleChangeOptions(event)}>
                        {this.props.users.map((item) => <option value={item.id}>{item.username}</option>)}
                    </select>
                </div>


                <input type="submit" className="btn btn-primary" value="Save"/>
            </form>
        );
    }
}

export default ProjectForm
