import PageList from './PageList';
import useFetch from './useFetch';

const Home = () => {

    const { data:pages, isPending, error } = useFetch('http://127.0.0.1:5000/page');

    return (
        <div className="home">
            { error && <div className="error">{ error }</div>}
            { isPending && <div>Loading...</div>}
            { pages && <PageList pages={pages} title="All pages" />}
        </div>
    )
}

export default Home;