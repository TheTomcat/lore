import React, { useEffect, useRef, useState } from "react";
import { useParams } from 'react-router-dom';
import ContentEditable from "react-contenteditable";
import sanitizeHtml from "sanitize-html";
import useFetch from "./useFetch";
import axios from 'axios';

const base = window.location.protocol + '//' + window.location.host + '/';

const PageEditor = (props) => {
    const {id} = useParams();

    const { data, isPending, error } = useFetch(window.location.protocol + '//' + window.location.host + '/page/'+id);
    
    return ( 
      <div className="page-detail">
          { isPending && <div>Loading...</div> }
          { error && <div>{ error }</div> }
          { data && (
          <article>
              {data['paragraphs'].map((paragraph) => (
                <ParagraphEditor id={paragraph.paragraph_id} key={paragraph.paragraph_id}/>
              ))}
          </article>
          )}
      </div>
   );
}

const ParagraphEditor = (props) => {
  const body = useRef("");
  const title = useRef("");
  const [ isPending, setIsPending ] = useState(true);
  const [ error, setError ] = useState(null);
  const [ editable, setEditable ] = useState(true);
  
  document.execCommand('defaultParagraphSeparator', false, 'br');

  const fetchData = () => {
    const options = {
      method: 'GET',
      timeout: 2000,
      url: base + 'paragraph/' + props.id
    };
    setTimeout( () => { // Remove
    axios(options)
    .then((response) => {
      body.current = response.data['body'];
      title.current = response.data['title'];
      setIsPending(false);
      setError(null);
    })
    .catch ( (err) => {
      if (err.name === 'AbortError') {
        console.log("Fetch aborted");
      } else {
        setIsPending(false);
        setError(err.message);
      }
    });
  }, 1000); // Remove
  }

  const putData = (id) => {
    const options = {
      method: 'PUT',
      timeout: 2000,
      url: base + 'paragraph/' + id,
      data: {
        title: title.current,
        body: body.current
      }
    };
    setTimeout( () => { // Remove
    axios(options)
    .then((response) => {
      console.log(response);
    })
    .catch ( (err) => {
      if (err.name === 'AbortError') {
        console.log("Fetch aborted");
      } else {
        setIsPending(false);
        setError(err.message);
      }
    });
  }, 1000); // Remove
  }

  useEffect(fetchData,[props.id]);

  const handleChange = (e) => {
    body.current = e.target.value;
  };
  const sanitizeConf = {
    allowedTags: ["b", "i", "em", "strong", "a", "h1"],
    allowedAttributes: { a: ["href"] }
  };
  const handleBlur = () => {
    console.log("BLURRED")
    body.current = sanitizeHtml(body.current, sanitizeConf);
    putData(props.id);
  };
  const toggleEditable = () => {
    setEditable(!editable);
  };

  return (
    <>
    { isPending && <div>Loading...</div> }
    { error && <div>{ error }</div> }
    { !isPending && !error && 
      <>
      <h3>{ title.current }</h3>
        <ContentEditable
          className="editable"
          tagName="pre"
          html={body.current} // innerHTML of the editable div
          disabled={!editable} // use true to disable edition
          onChange={handleChange} // handle innerHTML change
          onBlur={handleBlur}
        />
      </>
    }
    </>
  )
}

const EditButton = (props) => {
  return (
    <button
      key={props.cmd}
      onMouseDown={evt => {
        evt.preventDefault(); // Avoids loosing focus from the editable area
        document.execCommand(props.cmd, false, props.arg); // Send the command to the browser
      }}
    >
      {props.name || props.cmd}
    </button>
  );
}

export default PageEditor;
