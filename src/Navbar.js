import { Link } from 'react-router-dom';
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
                { links.map((item) => (
                    <li className="nav-item" key={item.id}>
                        <Link className="nav-link" to={item.uri}>
                            {item.icon}
                            <span className="link-text">{item.label}</span>
                        </Link>
                    </li>
                ))}
            </ul>
        </nav>
    )
}

export default Navbar;