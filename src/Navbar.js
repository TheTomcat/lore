import { NavLink, withRouter  } from 'react-router-dom';
import { FiUsers, FiBookOpen, FiFile } from 'react-icons/fi'
//https://react-icons.github.io/react-icons/
const Navbar = () => {

    const links = [
        {uri: '/lore', id: 'lore', icon: <FiBookOpen />, label:'Lore'},
        {uri: '/users', id: 'users', icon: <FiUsers />, label:'Users'},
        {uri: '/blank', id: 'blank', icon: <FiFile />, label:'Blank'},
        {uri: '/blank', id: 'blank2', icon: <FiFile />, label:'Blank'}
    ];
    
    return (
        <nav className="navbar">
            <ul className="navbar-nav">
                <li className="logo">
            <a href="#" className="nav-link">
            <span className="link-text logo-text">Lore</span>
            
            </a>
        </li>
                { links.map((item) => (
                    <li className="nav-item" key={item.id}>
                        <NavLink className="nav-link" activeClassName="active" to={item.uri}>
                            {item.icon}
                            <span className="link-text">{item.label}</span>
                        </NavLink>
                    </li>
                ))}
                {/* <li></li> */}
            </ul>
        </nav>
    )
}

export default withRouter(Navbar);