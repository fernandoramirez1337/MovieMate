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