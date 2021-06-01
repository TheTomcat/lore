import { Link } from 'react-router-dom';

const PageList = ({pages, title}) => {
    return (
        <div className="page-list">
            <h2>{title}</h2>
            
            {pages['items'].map((page) => (
                <div className="page-preview" key={page.page_id}>
                    <Link to={`/page/${page.page_id}`}>
                    <h2>{ page.title }</h2>
                    </Link>
                </div>
            ))}
        </div>
    );
}

export default PageList;