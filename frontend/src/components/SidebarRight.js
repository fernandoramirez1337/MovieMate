// src/components/SidebarRight.js
import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import { suggestUsers, popularMovies, suggestMoviesBasedOnActor, suggestMoviesBasedOnActorInMovie } from './api';

const buttonStyle = {
  backgroundColor: '#4caf50',
  color: 'white',
  padding: '5px 10px',
  border: 'none',
  borderRadius: '5px',
  cursor: 'pointer',
  margin: '0 5px',
};

function SidebarRight() {
  const location = useLocation();
  const userData = location.state ? location.state : null;
  const [listUsers, setUsers] = useState(null);
  const [listPopMovies, setPopMovies] = useState(null);
  const [listSugMoviesBasedOnActor, setSugMoviesBasedOnActor] = useState(null);
  const [listSugMoviesBasedOnActorInMovie, setSugMoviesBasedOnActorInMovie] = useState(null);

  const handleUserSuggest = async () => {
    try {
      const response = await suggestUsers(userData.user.name);
      setUsers(response);
    } catch (error) {
      console.error('Error during login:', error);
    }
  };
  const handlePopularMovies = async () => {
    try {
      const response = await popularMovies(userData.user.name);
      setPopMovies(response);
    } catch (error) {
      console.error('Error during login:', error);
    }
  };

  const handleSuggestMoviesBasedOnActor = async () => {
    try {
      const response = await suggestMoviesBasedOnActor(userData.user.name);
      setSugMoviesBasedOnActor(response);
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
    handleUserSuggest();
    handlePopularMovies();
    handleSuggestMoviesBasedOnActor();
    handleSuggestMoviesBasedOnActorInMovie();
  }, []); 
  
  return (
    <div className="sidebar sidebar-right">

      <h2>Recommended Movies</h2>
      {listSugMoviesBasedOnActor !== null ? (
        listSugMoviesBasedOnActor.length > 0 ? (
          <ul className="user-list">
            {listSugMoviesBasedOnActor.map((user, index) => (
              <li key={index} className="user-item">
                {user.RecommendedMovie} <br />
              </li>
            ))}
          </ul>
        ) : (
          <p>No suggested movies found.</p>
        )
      ) : (
        <p>Loading...</p>
      )}
      <h2>Connect with Friends</h2>
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
      <h2>Featured Content</h2>
      {listPopMovies !== null ? (
        listPopMovies.length > 0 ? (
          <ul className="user-list">
            {listPopMovies.map((user, index) => (
              <li key={index} className="user-item">
                {user.Movie} ({user.Year})
              </li>
            ))}
          </ul>
        ) : (
          <p>No popular movies found.</p>
        )
      ) : (
        <p>Loading...</p>
      )}
      {/* Add sidebar content as needed */}
    </div>
  );
}

export default SidebarRight;
