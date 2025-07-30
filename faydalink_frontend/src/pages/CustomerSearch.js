import React, { useState, useContext } from 'react';
import api from '../api/axios';
import { AuthContext } from '../context/AuthContext';

export default function CustomerSearch() {
  const [fin, setFin] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const { accessToken } = useContext(AuthContext);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResult(null);
    try {
      const response = await api.post('/customer/search/', { fin }, {
        headers: { Authorization: `Bearer ${accessToken}` },
      });
      setResult(response.data);
    } catch (err) {
      setError(err.response?.data?.error || 'Search failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-md mx-auto p-4">
      <h2 className="text-xl font-bold mb-2">Customer Search</h2>
      <form onSubmit={handleSubmit} className="mb-4">
        <input
          type="text"
          placeholder="Enter FIN"
          value={fin}
          onChange={(e) => setFin(e.target.value)}
          className="border px-2 py-1 mr-2"
          required
        />
        <button type="submit" className="bg-blue-600 text-white px-4 py-1 rounded" disabled={loading}>
          {loading ? 'Searching...' : 'Search'}
        </button>
      </form>
      {error && <div className="text-red-600 mb-2">{error}</div>}
      {result && (
        <div className="border p-2 rounded">
          <img src={result.photo_url} alt="National ID" className="w-24 h-24 mb-2" />
          <div><strong>Name:</strong> {result.name}</div>
          <div><strong>FIN:</strong> {result.fin}</div>
          <div><strong>Credit Score:</strong> {result.credit_score}</div>
          <div><strong>Credit Limit:</strong> {result.credit_limit}</div>
          <div><strong>National ID:</strong> {result.national_id}</div>
        </div>
      )}
    </div>
  );
}
