import {useState, useEffect} from 'react';
const axios = require('axios');

const useFetch = ( uri ) => {
    
    const [data, setData] = useState(null);
    const [isPending, setIsPending] = useState(true);
    const [error, setError] = useState(null);

    useEffect( () => {
        const options = {
            url: uri,
            method:'get'
        }
        setTimeout(() => {
        axios(options)
        .then(res => {
            // if (!res.ok) {
            //     throw Error('Could not fetch data from that resource');
            // }
            // console.log(res.data);
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