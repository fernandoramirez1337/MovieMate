// api.js

import axios from "axios";

export const suggestUsers = async (name) => {
    try {
      const response = await axios.post('/api/suggest_users', { username: name });
      return response.data;
    } catch (error) {
      console.error('Error during user suggestion:', error);
      throw error; // Re-throw the error so that the component can handle it
    }
  };

export const popularMovies = async (name) => {
  try {
    const response = await axios.post('/api/popular_movies', { username: name });
    return response.data;
  } catch (error) {
    console.error('Error during user suggestion:', error);
    throw error; // Re-throw the error so that the component can handle it
  }
};

export const ratedMovies = async (name) => {
  try {
    const response = await axios.post('/api/rated_movies', { username: name });
    return response.data;
  } catch (error) {
    console.error('Error during user suggestion:', error);
    throw error; // Re-throw the error so that the component can handle it
  }
};