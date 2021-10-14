import React from 'react'
import {Link} from "react-router-dom";


const Menu = ({obj}) => {
    return (
        <nav>
            <ul>
                {obj.isAuthenticated() ?
                    <button onClick={() => obj.logout()}>Logout</button> :
                    <Link to='/login'>Login</Link>
                }
                <li><Link to='/'>Users</Link></li>
                <li><Link to='/projects'>Projects</Link></li>
                <li><Link to='/todo'>ToDo</Link></li>
            </ul>
        </nav>
    )
}

export default Menu
