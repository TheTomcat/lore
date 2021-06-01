import { useParams, useHistory } from 'react-router-dom';
import useFetch from './useFetch';

const PageDetails = () => {
    const { id } = useParams();
    const { data , error, isPending } = useFetch('http://127.0.0.1:5000/page/' + id);

    const history = useHistory();

    const handleClick = () => {
        fetch('http://127.0.0.1:5000/page/' + id, {
            method: 'DELETE'
        }).then( () => {
            history.push('/');
        })
    }

    return ( 
        <div className="page-details">
            { isPending && <div>Loading...</div> }
            { error && <div>{ error }</div> }
            { data && (
            <article>
                {data['paragraphs'].map((paragraph) => (
                    <div key={ paragraph.paragraph_id }>
                    { console.log(paragraph) }
                    <h2>{ paragraph.title }</h2>
                    <div className="page-body">{ paragraph.body }</div>
                    </div> ))}
            </article>
            )}
        </div>
     );
}
 
export default PageDetails;