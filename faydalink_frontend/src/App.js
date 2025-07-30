import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import HospitalDashboard from './pages/HospitalDashboard';
import FarmerDashboard from './pages/FarmerDashboard';
import Login from './pages/Login';
import Navbar from './components/Navbar';


function App() {
  return (
    <>
      <Navbar />
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/hospital" element={<HospitalDashboard />} />
          <Route path="/farmer" element={<FarmerDashboard />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
