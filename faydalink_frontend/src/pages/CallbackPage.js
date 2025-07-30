import React, { useEffect } from 'react';
import { handleCallback } from '../services/auth';
import { useNavigate } from 'react-router-dom';

export default function CallbackPage() {
  const navigate = useNavigate();
  useEffect(() => {
    async function processAuth() {
      await handleCallback();
      navigate('/dashboard');
    }
    processAuth();
  }, [navigate]);
  return <div>Processing login...</div>;
}
