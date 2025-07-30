import React, { useState } from 'react';
import api from '../api/axios';

const treatments = [
  { name: 'Surgery', value: 'surgery' },
  { name: 'Medicine', value: 'medicine' },
  { name: 'Consultation', value: 'consultation' },
];

export default function HospitalDashboard() {
  const [patientName, setPatientName] = useState('');
  const [selectedTreatments, setSelectedTreatments] = useState([]);
  const [totalCost, setTotalCost] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleTreatmentChange = (e) => {
    const value = e.target.value;
    setSelectedTreatments((prev) =>
      prev.includes(value)
        ? prev.filter((t) => t !== value)
        : [...prev, value]
    );
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setTotalCost(null);
    try {
      const response = await api.post('/hospital/create-treatment/', {
        patient_name: patientName,
        treatments: selectedTreatments,
      });
      setTotalCost(response.data.total_cost);
    } catch (err) {
      setError(err.response?.data?.error || 'Submission failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Hospital Dashboard</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Patient Name:</label>
          <input
            type="text"
            value={patientName}
            onChange={(e) => setPatientName(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Select Treatments:</label>
          {treatments.map((t) => (
            <div key={t.value}>
              <input
                type="checkbox"
                value={t.value}
                checked={selectedTreatments.includes(t.value)}
                onChange={handleTreatmentChange}
              />
              {t.name}
            </div>
          ))}
        </div>
        <button type="submit" disabled={loading}>
          {loading ? 'Submitting...' : 'Submit'}
        </button>
      </form>
      {totalCost !== null && (
        <div>
          <h2>Total Cost: {totalCost}</h2>
        </div>
      )}
      {error && <div style={{ color: 'red' }}>{error}</div>}
    </div>
  );
}
