// App.js
import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { Link, Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import HomePage from './HomePage';
import SearchPage from './SearchPage';
// import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';


const containerStyle = {
  width: '300px',
  margin: '100px auto',
  padding: '20px',
  border: '1px solid #ccc',
  borderRadius: '5px',
};

const inputStyle = {
  marginBottom: '10px', // Add margin at the bottom of the input
};

const buttonStyle = {
  backgroundColor: '#4caf50',
  color: 'white',
  padding: '10px 15px',
  border: 'none',
  borderRadius: '5px',
  cursor: 'pointer',
  margin: '0 5px', // Add margin to create space between buttons
};

function LoginPage() {
  const [username, setUsername] = useState('');
  const [userData, setUserData] = useState(null);
  const [errorMessage, setErrorMessage] = useState('');

  useEffect(() => {
    document.title = userData ? `Welcome, ${userData.user.name}!` : 'MovieMate';
  }, [userData]);

  const handleLogin = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/api/login', { username });
      //console.log('Response:', response.data.user.name); // Log the response data to the console
      setUserData(response.data);
      setErrorMessage('');

      //navigate('/home', { state: { userData: response.data } });
    } catch (error) {
      console.error('Error during login:', error);
      if (error.response && error.response.status === 401) {
        setErrorMessage('Incorrect username. Please try again.');
        setUserData(null);
      } else {
        setErrorMessage('An error occurred during login. Please try again later.');
      }
    }
  };

  return (
    <div style={containerStyle}>
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <label htmlFor="username" >Username:</label>
        <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} style={inputStyle} />
        <br />
        <button type="submit" style={buttonStyle}>
          Log in
        </button>
        <button type="submit" style={buttonStyle}>
          Sign up
        </button>
      </form>
      {errorMessage && (
        <p style={{ color: 'red', marginTop: '10px' }}>{errorMessage}</p>
      )}
      {userData && (
        <div>
          <p>
            Welcome, {userData.user.name} (ID: {userData.user.userId})!
          </p>
          <Link to='/home' state={ userData}>
            Learn More
            </Link>

        </div>
      )}
    </div>
  );
}

function App() {
  const [loggedInUser, setLoggedInUser] = useState(null);
  const handleLogin = (userData) => {
    // Assume a successful login for simplicity
    setLoggedInUser(userData);
  };

  return (
    <Router>
      <Routes>

        <Route path="/" element={<LoginPage />} />
        <Route path="/home" element={<HomePage />} />
        <Route
        path="/search"
        element={<SearchPage />}
        />

      </Routes>
    </Router>
  );
}

export default App;

// render={(props) => <SearchPage {...props} loggedInUser={loggedInUser} />}
