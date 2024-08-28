import React from 'react';
import { Link } from 'react-router-dom';
import '../LandingPage.css';  // Create a separate CSS file for LandingPage styles
import healthyFoodImage from '../assets/Healthy-eating.jpg';  // Import the image

function LandingPage() {
    return (
        <div className="landing-page-container">
            <div className="image-container">
                <img src={healthyFoodImage} alt="Healthy Food" />
            </div>
            <div className="content-container">
                <h1>Welcome to Healthy Eating</h1>
                <nav className="buttons">
                    <Link to="/signup" className="button">Sign Up</Link>
                    <Link to="/login" className="button">Login</Link>
                </nav>
            </div>
        </div>
    );
}

export default LandingPage;
