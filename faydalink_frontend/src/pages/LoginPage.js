import React from 'react';
import { login } from '../services/auth';

export default function LoginPage() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <button
        className="bg-blue-600 text-white px-6 py-2 rounded shadow"
        onClick={login}
      >
        Login with National ID
      </button>
    </div>
  );
}
