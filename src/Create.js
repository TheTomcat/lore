import { useState } from "react";
import { useHistory } from 'react-router-dom';

const Create = () => {
    const [ title, setTitle ] = useState('');
    const [ body, setBody ] = useState('');
    const [ author, setAuthor ] = useState('mario');
    const [ isPending, setIsPending ] = useState(false);

    const history = useHistory();

    const handleSubmit = (e) => {
        e.preventDefault();
        const blog = { title, body, author };
        setIsPending(true);

        fetch('http://localhost:8000/blogs', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(blog)
        }).then( () => {
            setIsPending(false);
            console.log('blog submitted');
            history.push('/');
        });        
    }
    return ( 
    <div className="create">
        <h2>Add a new blog</h2>
        <form onSubmit={handleSubmit}>
            <label>Blog Title:</label>
            <input 
                type="text" 
                value={title} 
                onChange={(e) => setTitle(e.target.value)}
                required
            />
            <label></label>
            <textarea 
                required
                value={body} 
                onChange={(e) => setBody(e.target.value)}
            >
            </textarea>
            <label>Blog Title:</label>
            <select
                value={author} 
                onChange={(e) => setAuthor(e.target.value)}
            >
                <option value="mario">Mario</option>
                <option value="luigi">Luigi</option>
                <option value="yoshi">Yoshi</option>
            </select>
            { !isPending && <button>Add blog</button>}
            { isPending && <button disabled>Adding blog...</button>}
        </form>
    </div> );
}
 
export default Create;