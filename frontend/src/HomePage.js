import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import SidebarLeft from './components/SidebarLeft';
import SidebarRight from './components/SidebarRight';
import NewsFeed from './components/NewsFeed';
import './App.css';

const containerStyle = {
  width: '300px',
  margin: '100px auto',
  padding: '20px',
  border: '1px solid #ccc',
  borderRadius: '5px',
};

function HomePage() {
  const location = useLocation();
  const userData = location.state ? location.state : null;
  const [news, setNews] = useState([
    { id: 1, title: userData.user.name, content: 'This is the first breaking news.' },
    { id: 2, title: userData.user.userId, content: 'An important update just in.' },
    // Add more news items as needed
  ]);

  return (
    <div className="app-container">
      <SidebarLeft />
      <NewsFeed news={news} />
      <SidebarRight />
    </div>
  );
}

export default HomePage;
