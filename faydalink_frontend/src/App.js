import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AuthProvider from './context/AuthContext';
import Home from './pages/Home';
import HospitalDashboard from './pages/HospitalDashboard';
import FarmerDashboard from './pages/FarmerDashboard';
import LoginPage from './pages/LoginPage';
import CallbackPage from './pages/CallbackPage';
import Dashboard from './pages/Dashboard';
import CustomerSearch from './pages/CustomerSearch';
import Navbar from './components/Navbar';


function App() {
  return (
    <AuthProvider>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/hospital" element={<HospitalDashboard />} />
          <Route path="/farmer" element={<FarmerDashboard />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/callback" element={<CallbackPage />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/search" element={<CustomerSearch />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
