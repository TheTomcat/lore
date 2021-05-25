import {useState, useEffect} from 'react';

const useFetch = ( uri ) => {
    
    const [data, setData] = useState(null);
    const [isPending, setIsPending] = useState(true);
    const [error, setError] = useState(null);

    useEffect( () => {

        const abortCont = new AbortController();

        setTimeout(() => {
        fetch(uri, { signal: abortCont.signal })
        .then(res => {
            if (!res.ok) {
                throw Error('Could not fetch data from that resource');
            }
            return res.json()
        })
        .then(data => {
            setError(null);
            setData(data);
            setIsPending(false);
        })
        .catch( (err) => {
            if (err.name === 'AbortError') {
                console.log("Fetch aborted");
            } else {
                setIsPending(false);
                setError(err.message);
            }
        })
        }, 1000);
        return () => abortCont.abort();
    }, [uri]);

    return {data, isPending, error};
}

export default useFetch;