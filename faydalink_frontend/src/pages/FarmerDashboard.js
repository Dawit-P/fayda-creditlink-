import React, { useState } from 'react';
import api from '../api/axios';

export default function FarmerDashboard() {
  const [farmerId, setFarmerId] = useState('');
  const [goods, setGoods] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setGoods([]);
    try {
      const response = await api.post('/agrisupplier/request-goods/', {
        farmer_id: farmerId,
      });
      setGoods(response.data.goods || []);
    } catch (err) {
      setError(err.response?.data?.error || 'Submission failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Farmer Dashboard</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Farmer National ID or Name:</label>
          <input
            type="text"
            value={farmerId}
            onChange={(e) => setFarmerId(e.target.value)}
            required
          />
        </div>
        <button type="submit" disabled={loading}>
          {loading ? 'Submitting...' : 'Submit'}
        </button>
      </form>
      {goods.length > 0 && (
        <div>
          <h2>Approved Goods</h2>
          <ul>
            {goods.map((item, idx) => (
              <li key={idx}>
                {item.name} - {item.price}
              </li>
            ))}
          </ul>
        </div>
      )}
      {error && <div style={{ color: 'red' }}>{error}</div>}
    </div>
  );
}
