// src/components/NewsFeed.js

import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
//import axios from 'axios';
import './NewsFeed.css';
import { suggestUsers, suggestMoviesBasedOnActorInMovie } from './api';

const buttonStyle = {
  backgroundColor: '#4caf50',
  color: 'white',
  padding: '10px 15px',
  border: 'none',
  borderRadius: '5px',
  cursor: 'pointer',
  margin: '0 5px',
};

function NewsFeed({ news }) {
  const location = useLocation();
  const userData = location.state ? location.state : null;
  const [listUsers, setUsers] = useState(null);
  const [listSugMoviesBasedOnActorInMovie, setSugMoviesBasedOnActorInMovie] = useState(null);

  const handleUserSuggest = async () => {
    try {
      const response = await suggestUsers(userData.user.name);
      setUsers(response);
    } catch (error) {
      console.error('Error during login:', error);
    }
  };

  const handleSuggestMoviesBasedOnActorInMovie = async () => {
    try {
      const response = await suggestMoviesBasedOnActorInMovie(userData.user.name);
      setSugMoviesBasedOnActorInMovie(response);
    } catch (error) {
      console.error('Error during login:', error);
    }
  };

  useEffect(() => {
    // Call handleUserSuggest when the component mounts
    handleSuggestMoviesBasedOnActorInMovie();
    //handleUserSuggest();
  }, []); 

  return (
    <div className="news-feed">
      {listSugMoviesBasedOnActorInMovie && (
      <div className="news-feed">
        <h3>Movie Suggestions</h3>
        {listSugMoviesBasedOnActorInMovie.map((user, index) => (
          <div key={index} className="news-item">
            <h4>Because you loved {user.Actor} in {user.MyRatedMovie}</h4>
            <p>{user.RecommendedMovie} ({user.Year})</p>
            <p>{user.Plot}</p>
            <img src={user.Poster} style={{ maxWidth: '10%', height: 'auto' }} />
            <p>Directed by: {user.Director}</p>
          </div>
        ))}
      </div>
    )}

    </div>
  );
}

export default NewsFeed;
