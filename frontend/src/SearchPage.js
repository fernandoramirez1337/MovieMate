// SearchPage.js
import React from 'react';
// import { useLocation } from 'react-router-dom';
import './App.css';
import Header from './components/Header';
import SidebarLeft from './components/SidebarLeft';
import SidebarRight from './components/SidebarRight';

const SearchPage = ({ location}) => {
  // const location = useLocation();

  const responseData = location.state?.responseData;
  // const userData = location.state ? location.state : null;


  return (
    <div>
      <div className='header'>
        <Header />
      </div>

      <div className="app-container">
        <SidebarLeft />
        <div>
          <h1>Search Page</h1>
          {responseData && (
            <div>
              <p>Data: {JSON.stringify(responseData)}</p>
              {/* Use the data to create simple elements */}
            </div>
          )}
        </div>
        {/* <SearchFeed /> */}
        <SidebarRight />
      </div>
    </div>
  );
};

export default SearchPage;
