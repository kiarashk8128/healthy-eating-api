import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';  // App specific styles
import Login from './pages/Login.jsx';
import Signup from './pages/Signup.jsx';
import LandingPage from './pages/LandingPage.jsx';  // Create a new LandingPage component

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<LandingPage />} />
                <Route path="/signup" element={<Signup />} />
                <Route path="/login" element={<Login />} />
            </Routes>
        </Router>
    );
}

export default App;
