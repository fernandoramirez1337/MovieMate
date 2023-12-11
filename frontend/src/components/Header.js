// src/components/Header.js

import axios from 'axios';
import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';

// import './Header.css';

// const ButtonComponent = () => {
//   const [responseData, setResponseData] = useState(null);

//   const fetchData = async () => {
//     try {
//       // Make your API call here
//       const response = await fetch('your-api-endpoint');
//       const data = await response.json();
//       setResponseData(data);
//     } catch (error) {
//       console.error('Error fetching data:', error);
//     }
//   };

const buttonStyle = {
  backgroundColor: '#4caf50',
  color: 'white',
  padding: '10px 15px',
  border: 'none',
  borderRadius: '5px',
  cursor: 'pointer',
  margin: '0 5px',
};

function Header() {
  const [selectValue, setSelectValue] = useState('');
  const [inputTextValue, setInputTextValue] = useState('');
  const [responseData, setResponseData] = useState(null);
  const [postData, setPostData] = useState({});

  const location = useLocation();
  const userData = location.state ? location.state : null;
  const [listUsers, setUsers] = useState(null);

  // const fetchData = async () => {
  //   try {
  //     // Make your API call here, sending selectValue and inputTextValue
  //     // const response = await fetch('/api/search', {
  //     //   method: 'POST',
  //     //   headers: {
  //     //     'Content-Type': 'application/json',
  //     //   },
  //     //   body: JSON.stringify({
  //     //     select: selectValue,
  //     //     inputText: inputTextValue,
  //     //   }),
  //     // });

  //     // const data = await response.json();
  //     const response = await axios.post('/api/search',postData);
  //     const data = await response.data;
  //     setResponseData(data);
  //   } catch (error) {
  //     console.error('Error fetching data:', error);
  //   }
  // };

  const postDataToApi = async () => {
    try {
      const response = await axios.post('/api/search', postData);
      const data = response.data;
      setResponseData(data);
    } catch (error) {
      console.error('Error posting data:', error);
    }
  };

  // return (
//   <div>
//     <button onClick={fetchData}>Press Me</button>
//     {responseData && <p>Data: {JSON.stringify(responseData)}</p>}
//   </div>
// );

  return (
    <div className="search_bar_container">
        <select
          value={selectValue} onChange={
            (e)=> setSelectValue(e.target.value)
          }
          id="search_type"
          name="search_type"
        >
          <option value="All">All</option>
          <option value="Person">Person</option>
          <option value="Community">Community</option>
          <option value="Titles">Titles</option>
          <option value="TV_eps">TV eps</option>
          <option value="Celebs">Celebs</option>
          <option value="Companies">Companies</option>
          <option value="Genre">Genre</option>
        </select>
        <input
          type="text"
          value={inputTextValue}
          onChange={
            // (e) => setInputTextValue(e.target.value)
            (e)=> setPostData(e.target.value)
          }
          list="suggestions"
          id="search_text"
          name="search_text"
          required
          placeholder="Search Movie"
        />

        <button className="search_button" onClick={postDataToApi}>
          <img
            className="search_icon"
            alt="search"
          />
          {responseData && <p>Data: {JSON.stringify(responseData)}</p>}
        </button>

        <datalist id="suggestions">
        </datalist>
    </div>
  );
}




export default Header;
