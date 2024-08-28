// import React from 'react';
import { useState } from 'react';
import '../LoginSignup.css';
import healthyFoodImage from '../assets/Healthy-eating.jpg';

const Signup = () => {
    const [formData, setFormData] = useState({
        username: '',
        password: '',
        email: '',
        first_name: '',
        last_name: '',
        birthday: '',
        gender: '',
        height: '',
        weight: '',
        is_family_head: false,
        family_members: [],
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Logic to handle signup using formData goes here
    };

    return (
        <div className="form-container">
            <div className="image-container">
                <img src={healthyFoodImage} alt="Healthy Food" />
            </div>
            <div className="form-content">
                <h1>Sign Up</h1>
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
                    <input
                        type="email"
                        name="email"
                        placeholder="Email"
                        value={formData.email}
                        onChange={handleChange}
                    />
                    <input
                        type="text"
                        name="first_name"
                        placeholder="First Name"
                        value={formData.first_name}
                        onChange={handleChange}
                    />
                    <input
                        type="text"
                        name="last_name"
                        placeholder="Last Name"
                        value={formData.last_name}
                        onChange={handleChange}
                    />
                    <input
                        type="date"
                        name="birthday"
                        value={formData.birthday}
                        onChange={handleChange}
                    />
                    <select
                        name="gender"
                        value={formData.gender}
                        onChange={handleChange}
                    >
                        <option value="">Select Gender</option>
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                        <option value="other">Other</option>
                    </select>
                    <input
                        type="number"
                        name="height"
                        placeholder="Height (cm)"
                        value={formData.height}
                        onChange={handleChange}
                    />
                    <input
                        type="number"
                        name="weight"
                        placeholder="Weight (kg)"
                        value={formData.weight}
                        onChange={handleChange}
                    />
                    <label>
                        <input
                            type="checkbox"
                            name="is_family_head"
                            checked={formData.is_family_head}
                            onChange={(e) =>
                                setFormData({ ...formData, is_family_head: e.target.checked })
                            }
                        />
                        Are you the family head?
                    </label>
                    {/* Add fields for family members if needed */}
                    <button type="submit">Sign Up</button>
                </form>
            </div>
        </div>
    );
};

export default Signup;
