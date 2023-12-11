import React, { useState } from 'react';
// import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import './App.css';
import Header from './components/Header';
import NewsFeed from './components/NewsFeed';
import SidebarLeft from './components/SidebarLeft';
import SidebarRight from './components/SidebarRight';

function HomePage() {
  const location = useLocation();
  const navigate = useNavigate();
  const [responseData, setResponseData] = useState(null);
  const userData = location.state ? location.state : null;

  const handleDataReceived = (data)=>{
    setResponseData(data)
    navigate('/search',{state:{responseData:data}});
  }

  return (
    <div>
      <div className='header'>
        <Header onDataReceived={handleDataReceived} />
        {/* <div className="search_bar_container">
            <select
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
              list="suggestions"
              id="search_text"
              name="search_text"
              required
              placeholder="Search Movie"
            />

            <button type="submit" className="search_button" onDataReceived={handleDataReceived}>
              <img
                className="search_icon"
                src="{{url_for('static', filename='assets/search_icon.svg')}}"
                alt="search"
              />
            </button>
        </div> */}

      </div>

      <div className="app-container">
        <SidebarLeft />
        <NewsFeed />
        <SidebarRight />
      </div>
    </div>
  );
}

export default HomePage;
