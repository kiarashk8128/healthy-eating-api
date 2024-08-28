// import React from 'react';
import { useState } from 'react';
import '../LoginSignup.css';
import healthyFoodImage from '../assets/Healthy-eating.jpg';

const Login = () => {
    const [formData, setFormData] = useState({ username: '', password: '' });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Logic to handle login using formData goes here
    };

    return (
        <div className="form-container">
            <div className="image-container">
                <img src={healthyFoodImage} alt="Healthy Food" />
            </div>
            <div className="form-content">
                <h1>Login</h1>
                <form onSubmit={handleSubmit}>
                    <input
                        type="text"
                        name="username"
                        placeholder="Username"
                        value={formData.username}
                        onChange={handleChange}
                    />
                    <input
                        type="password"
                        name="password"
                        placeholder="Password"
                        value={formData.password}
                        onChange={handleChange}
                    />
                    <button type="submit">Login</button>
                </form>
            </div>
        </div>
    );
};

export default Login;
