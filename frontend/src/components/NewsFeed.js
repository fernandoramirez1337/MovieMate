// src/components/NewsFeed.js

import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
//import axios from 'axios';
import './NewsFeed.css';
import { suggestUsers } from './api';

const buttonStyle = {
  backgroundColor: '#4caf50',
  color: 'white',
  padding: '10px 15px',
  border: 'none',
  borderRadius: '5px',
  cursor: 'pointer',
  margin: '0 5px',
};

function NewsFeed() {
  const location = useLocation();
  const userData = location.state ? location.state : null;
  const [listUsers, setUsers] = useState(null);

  const handleUserSuggest = async () => {
    try {
      const response = await suggestUsers(userData.user.name);
      setUsers(response);
    } catch (error) {
      console.error('Error during login:', error);
    }
  };

  useEffect(() => {
    // Call handleUserSuggest when the component mounts
    handleUserSuggest();
  }, []); 

  return (
    <div className="news-feed">
      <h2>MovieMate Feed {userData.user.name}</h2>
      {listUsers !== null ? (
        listUsers.length > 0 ? (
          <ul className="user-list">
            {listUsers.map((user, index) => (
              <li key={index} className="user-item">
                {user.Friend_suggestion} <br /> Movies in common: {user.n} 
                <button style={buttonStyle}>
                Send Friend Request
              </button>
              </li>
            ))}
          </ul>
        ) : (
          <p>No suggested users found.</p>
        )
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default NewsFeed;
