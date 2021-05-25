import { useState, useRef, useContext } from 'react';
import {UserContext} from './App'

//  https://bezkoder.com/react-hooks-jwt-auth/

const Login = () => {
    const currentUser = useContext(UserContext);
    console.log(currentUser);
    return ( <div></div> );
}
 
export default Login;