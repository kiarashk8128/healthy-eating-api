// import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../MainPage.css';

const MainPage = () => {
    const navigate = useNavigate();

    return (
        <div className="main-container">
            <h1>Welcome to Healthy Eating</h1>
            <button onClick={() => navigate('/personal-info')}>Personal Information</button>
            <button onClick={() => navigate('/menus')}>View Menus</button>
        </div>
    );
};

export default MainPage;