import React, { useState } from 'react';
import {MdCloudUpload} from 'react-icons/md';
import BarLoader from "react-spinners/BarLoader";

const FileUpload = ({childToParent}) => {
  const [file, setFile] = useState(null);
  const [summarizedText, setSummarizedText] = useState('');
  const [fileName, setFileName] = useState('');
  const [loading, setLoading] = useState(false); 

  
  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    setFileName(selectedFile.name);
    console.log(fileName);

    // Validate file type
    if (selectedFile && selectedFile.type === 'text/plain') {
      setFile(selectedFile);
    } else {
      console.error('Invalid file type. Please select a text file.');
    }
  };

  const handleUpload = async () => {
    if (!file) {
      alert('Please select a file before uploading.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      setLoading(true);
      const response = await fetch('http://127.0.0.1:8000/upload', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        setLoading(false);
        setSummarizedText(data.summarized_text);
        childToParent(data.summarizedText)
        
        console.log('File uploaded successfully!');
      } else {
        console.error('Failed to upload file');
      }
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  return (
    <>
    <div className="App text-white">
      <div className="flex w-full p-6 mt-32">
        <div className='mr-20'>
          <h1 className="text-5xl font-bold mb-2">Summarize Transcripts</h1>
          <p className='mt-5 text-gray-300'>Upload a file and relax, the model will summarize the transcript for you.</p>
        </div>

        <div>
        <form className='flex flex-col items-center justify-center w-50 p-4 rounded-lg bg-gradient-to-r from-purple-500 to-indigo-500 hover:opacity-90 transition-opacity cursor-pointer'
      onClick={() => document.querySelector(".input-field").click()}>
        <input 
          type="file"
          accept=".txt"
          className='input-field'
          onChange={handleFileChange}
          hidden
        />
        <MdCloudUpload color='white' size = {60}/>
        <p>Browse Files to Upload</p>
        
      </form>

    <div>
      <span className='mr-5'>{fileName ? fileName : "No file selected"}</span>
      <button className="w-50 p-4 mt-8 rounded-lg bg-gradient-to-r from-purple-500 to-indigo-500 hover:opacity-90 transition-opacity cursor-pointer"
        onClick={handleUpload} >
            Summarize
      </button>
      {loading? <BarLoader
        color={'#6f0b74'}
        loading={loading}
        size={150}
        aria-label="Loading Spinner"
        data-testid="loader"/> : ""}
    </div> 
        </div>
      </div>

      <div>
        
      </div>
      <textarea
        className="w-full h-40 p-2 bg-gray-200 text-black mt-32"
        placeholder="Summarized Text will appear here"
        value={summarizedText}
        readOnly
      />
    </div>
      
  
  </>
  );
};

export default FileUpload;
