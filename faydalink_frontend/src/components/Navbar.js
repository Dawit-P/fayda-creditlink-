import React from 'react';
import { Link, useNavigate } from 'react-router-dom';

function getRoleFromToken() {
  const token = localStorage.getItem('token');
  if (!token) return null;
  try {
    const payload = JSON.parse(atob(token.split('.')[1]));
    return payload.role || null;
  } catch {
    return null;
  }
}

export default function Navbar() {
  const navigate = useNavigate();
  const role = getRoleFromToken();

  const handleLogout = () => {
    localStorage.clear();
    navigate('/login');
  };

  return (
    <nav style={{ padding: '1rem', borderBottom: '1px solid #ccc' }}>
      <Link to="/">Home</Link>
      {role === 'hospital' && <Link to="/hospital" style={{ marginLeft: 10 }}>Hospital</Link>}
      {role === 'farmer' && <Link to="/farmer" style={{ marginLeft: 10 }}>Farmer</Link>}
      {role && (
        <button onClick={handleLogout} style={{ marginLeft: 10 }}>Logout</button>
      )}
      {!role && <Link to="/login" style={{ marginLeft: 10 }}>Login</Link>}
    </nav>
  );
}
