import React from 'react';
import { Link } from 'react-router-dom';

export default function Dashboard() {
  return (
    <div className="p-4">
      <nav className="mb-4">
        <Link to="/search" className="mr-4 text-blue-600">Customer Search</Link>
        <Link to="/" className="text-gray-600">Home</Link>
      </nav>
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
      {/* Add more dashboard content here */}
    </div>
  );
}
