import React, { useCallback, useEffect, useRef, useState } from "react"
import Quill from "quill"
import { io } from 'socket.io-client'
import "quill/dist/quill.snow.css"
import { useParams } from "react-router-dom";

const uri = 'http://127.0.0.1:5000';
const SAVE_INTERVAL_MS = 2000;

/* const structure = {user:'user_id',
 document: 'document_id', delta:'delta'
} */

const QuillComponent = (props) => {
    const [ socket, setSocket ] = useState();
    const [ quill, setQuill ] = useState();
    // const [ oldData, setOldData ] = useState();
    const [ isEditable, setIsEditable ] = useState(false);
    const { id } = useParams();

    const emit_event_delta = (event, delta) => {
        socket.emit(event, {user: 'user_id',
            document: id, //props.id
            delta: delta});
    }

    useEffect(() => {
        const s = io(uri);
        setSocket(s);
        return () => {
            s.disconnect();
            console.log('disconnected');
        }
    }, []);

    useEffect(() => {
        if (socket == null || quill == null) return;
        socket.once('load-document', (document) => {
            console.log(document);
            quill.setContents({ops:[{'insert':document}]});
            console.log('asdf' + id);
            quill.enable();
        })
        socket.emit('get-document', {user:'user_id', document:id});
        console.log(id);
    }, [socket, quill, id, isEditable])

    useEffect(() => {
        if (socket == null || quill == null) return
        const interval = setInterval(() => {
            emit_event_delta('save-document', quill.getContents());
        }, SAVE_INTERVAL_MS);
        return () => {
            clearInterval(interval);
        }
    }, [socket, quill]);

    useEffect(() => {
        if (socket == null || quill == null) return;
        const handler = (delta, oldDelta, source) => {
            if (source != 'user') return
            emit_event_delta('send-changes', delta)
        };
        quill.on('text-change', handler);
        return () => {
            quill.off('text-change', handler);
        }
    }, [socket, quill]);

    useEffect(() => {
        if (socket == null || quill == null) return;
        const handler = (delta, oldDelta, source) => {
            quill.updateContents(delta);
        };
        socket.on('receive-changes', handler);
        return () => {
            socket.off('receive-changes', handler);
        }
    }, [socket, quill]);

    const wrapperRef = useCallback((wrapper) => {
        if (wrapper == null) return
        wrapper.innerHTML = '';
        const editor = document.createElement('div');
        wrapper.append(editor);
        const q = new Quill(editor, {theme: 'snow'});
        // q.disable();
        q.setText('loading...');
        setQuill(q);

    }, []);

    const staticDivRef = useCallback((wrapper) => {
        if (wrapper == null) return
        wrapper.innerHTML = '';
        
    })

    const handleClick = () => {
        setIsEditable(true);
    }

    const handleBlur = () => {
        setIsEditable(false);
        socket.disconnect();
    }

    return (<div>
        { isEditable && <div id="container" ref={wrapperRef} onBlur={handleBlur}></div> }
        { !isEditable && <div className="editor" onClick={handleClick}>test</div> }
    </div>
    );
};

export default QuillComponent;