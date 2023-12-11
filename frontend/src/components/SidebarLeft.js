// src/components/SidebarLeft.js
import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import { ratedMovies,  } from './api';

function SidebarLeft() {
    const location = useLocation();
    const userData = location.state ? location.state : null;
    const [listRatedMovies, setRatedMovies] = useState(null);
    const handleRatedMovies = async () => {
        try {
          const response = await ratedMovies(userData.user.name);
          setRatedMovies(response);
        } catch (error) {
          console.error('Error during login:', error);
        }
      };

    useEffect(() => {
    // Call handleUserSuggest when the component mounts
    handleRatedMovies();
    }, []); 

    return (
        <div className="sidebar sidebar-left">
        <h2>User profile</h2>
        <h4>{userData.user.name}</h4>
        <h2>My favorite movies</h2>
        {listRatedMovies !== null ? (
        listRatedMovies.length > 0 ? (
          <ul className="user-list">
            {listRatedMovies.map((user, index) => (
              <li key={index} className="user-item">
                {user.movie}
              </li>
            ))}
          </ul>
        ) : (
          <p>No rated movies found.</p>
        )
      ) : (
        <p>Loading...</p>
      )}
        <h2>My friends</h2>
        <h2>Quick actions</h2>
        {/* Add sidebar content as needed */}
        </div>
    );
    }

export default SidebarLeft;
