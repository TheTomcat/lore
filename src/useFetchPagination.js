import {useState, useEffect, useReducer } from 'react';

function reducer(state, action) {

}

const useFetchPagination = ( uri ) => {
    
    const [data, setData] = useState(null);
    const [isPending, setIsPending] = useState(true);
    const [error, setError] = useState(null);

    const [state, dispatch] = useReducer(reducer);

    useEffect( () => {

        const abortCont = new AbortController();

        fetch(uri, { signal: abortCont.signal })
        .then(res => {
            if (!res.ok) {
                throw Error('Could not fetch data from that resource');
            }
            return res.json()
        })
        .then(data => {
            console.log(data);
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
        });
        return () => abortCont.abort();
    }, [uri]);

    return {data, isPending, error};
}

export default useFetchPagination;