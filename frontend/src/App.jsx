// import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';  // App specific styles
import Login from './pages/Login.jsx';
import Signup from './pages/Signup.jsx';
import LandingPage from './pages/LandingPage.jsx';
import MainPage from './pages/MainPage.jsx';
import PersonalInfo from './pages/PersonalInfo.jsx';
import MenuPage from './pages/MenuPage.jsx';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<LandingPage />} />
                <Route path="/signup" element={<Signup />} />
                <Route path="/login" element={<Login />} />
                <Route path="/main" element={<MainPage />} />
                <Route path="/personal-info" element={<PersonalInfo />} />
                <Route path="/menus" element={<MenuPage />} />
            </Routes>
        </Router>
    );
}

export default App;

