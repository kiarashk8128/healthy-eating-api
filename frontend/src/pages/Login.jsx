// import React from 'react';
import { useState } from 'react';
import axios from 'axios';
import '../LoginSignup.css';
import healthyFoodImage from '../assets/Healthy-eating.jpg';

const Login = () => {
    const [formData, setFormData] = useState({ username: '', password: '' });
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost/auth/login/', formData);
            localStorage.setItem('token', response.data.access);
            setSuccess('Login successful!');
            setError('');
            console.log('Login successful!', response.data);
        } catch (err) {
            console.error('Login failed:', err.response.data);
            setError('Invalid username or password');
            setSuccess('');
        }
    };

    return (
        <div className="form-container">
            <div className="image-container">
                <img src={healthyFoodImage} alt="Healthy Food" />
            </div>
            <div className="form-content">
                <h1>Login</h1>
                {error && <p style={{ color: 'red' }}>{error}</p>}
                {success && <p style={{ color: 'green' }}>{success}</p>}
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
