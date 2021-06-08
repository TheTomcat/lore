import {useState, useEffect} from 'react';
const axios = require('axios');

const useFetch = ( uri, method="GET", body ={} ) => {
    
    const [data, setData] = useState(null);
    const [isPending, setIsPending] = useState(true);
    const [error, setError] = useState(null);

    useEffect( () => {
        setIsPending(true);
        const options = {
            url: uri,
            method:method,
            data:body
        }
        setTimeout(() => {
        axios(options)
        .then(res => {
            setError(null);
            setData(res.data);
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
        return 
    }, [uri]);

    return {data, isPending, error};
}

export default useFetch;