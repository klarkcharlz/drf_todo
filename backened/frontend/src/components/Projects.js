import React from 'react'

const UserItem = ({user}) => {
    return user.username
}


const ProjectItem = ({project, deleteProject}) => {
    return (
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.url}
            </td>
            <td>
                {project.users.map((user) => <UserItem user={user}/>)}
            </td>
            <td><button onClick={()=>deleteProject(project.id)} type='button'>Delete</button></td>
        </tr>
    )
}


const ProjectList = ({projects, deleteProject}) => {
    return (
        <table>
            <th>
                Name
            </th>
            <th>
                Url
            </th>
            <th>
                Users
            </th>
            <th></th>
            {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject}/>)}
        </table>
    )
}

export default ProjectList
