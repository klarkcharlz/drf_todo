import React from 'react'
import {useParams} from 'react-router-dom'


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.url}
            </td>
            <td>
                {project.users.map((user) => user.id)}
            </td>
        </tr>
    )
}


const UserProjectList = ({projects}) => {
    let {id} = useParams()
    let filtered_projects = []
    projects.forEach((project) => {
        if(project.users.map((user) => user.id).includes(parseInt(id))){
            filtered_projects.push(project);
        }
    })
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
            {filtered_projects.map((project) => <ProjectItem project={project}/>)}
        </table>
    )
}

export default UserProjectList
