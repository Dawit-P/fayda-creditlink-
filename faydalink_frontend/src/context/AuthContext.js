import React, { createContext, useState, useEffect } from 'react';
import { getUser, logout } from '../services/auth';

export const AuthContext = createContext();

export default function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [accessToken, setAccessToken] = useState(null);

  useEffect(() => {
    async function fetchUser() {
      const userObj = await getUser();
      setUser(userObj);
      setAccessToken(userObj?.access_token || null);
    }
    fetchUser();
  }, []);

  return (
    <AuthContext.Provider value={{ user, accessToken, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
