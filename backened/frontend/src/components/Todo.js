import React from 'react'
import {Link} from 'react-router-dom'


const TodoItem = ({todo, deleteTodo}) => {
    return (
        <tr>
            <td>
                {todo.project.name}
            </td>
            <td>
                {todo.user.username}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.createdAt}
            </td>
            <td>
                {todo.updatedAt}
            </td>
            <td>
                {todo.isActive ? "True" : "False"}
            </td>
            <td>
                <button onClick={() => deleteTodo(todo.id)} type='button'>Delete</button>
            </td>
        </tr>
    )
}


const TodoList = ({todos, deleteTodo}) => {
    return (
        <div>
            <table>
                <th>
                    Project
                </th>
                <th>
                    User
                </th>
                <th>
                    Text
                </th>
                <th>
                    Created
                </th>
                <th>
                    Updated
                </th>
                <th>
                    Active
                </th>
                <th></th>
                {todos.map((todo) => <TodoItem todo={todo} deleteTodo={deleteTodo}/>)}
            </table>
            <Link to='/todo/create'>Create</Link>
        </div>
    )
}

export default TodoList
