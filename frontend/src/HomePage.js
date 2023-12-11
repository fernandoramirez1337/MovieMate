import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import SidebarLeft from './components/SidebarLeft';
import SidebarRight from './components/SidebarRight';
import NewsFeed from './components/NewsFeed';
import './App.css';
import { suggestUsers, suggestMoviesBasedOnActorInMovie } from './components/api';


function HomePage() {
  const location = useLocation();
  const userData = location.state ? location.state : null;
  const [news, setNews] = useState([
    { id: 1, title: userData.user.name, content: 'This is the first breaking news.' },
    { id: 2, title: userData.user.userId, content: 'An important update just in.' },
    // Add more news items as needed
  ]);

  const [listSugMoviesBasedOnActorInMovie, setSugMoviesBasedOnActorInMovie] = useState(null);

  const handleSuggestMoviesBasedOnActorInMovie = async () => {
    try {
      const response = await suggestMoviesBasedOnActorInMovie(userData.user.name);
      setSugMoviesBasedOnActorInMovie(response);
    } catch (error) {
      console.error('Error suggesting movies:', error);
    }
  };

  useEffect(() => {
    handleSuggestMoviesBasedOnActorInMovie();
  }, []);


  return (
    <div className="app-container">
      <SidebarLeft />
      <NewsFeed news={news} />
      <SidebarRight />
    </div>
  );
}

export default HomePage;
