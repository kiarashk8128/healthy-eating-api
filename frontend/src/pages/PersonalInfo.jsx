// import React from 'react';

import { useState, useEffect } from 'react';
import axios from 'axios';
import '../PersonalInfo.css';

const PersonalInfo = () => {
    const [personalInfo, setPersonalInfo] = useState(null);
    const [familyMembers, setFamilyMembers] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                // Fetch personal information
                const userResponse = await axios.get('http://localhost/auth/user-info/', {
                    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
                });
                setPersonalInfo(userResponse.data);

                // If the user is a family head, fetch family members' information
                if (userResponse.data.is_family_head) {
                    const familyResponse = await axios.get('http://localhost/auth/family-members/', {
                        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
                    });
                    setFamilyMembers(familyResponse.data);
                }
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, []);

    return (
        <div className="personal-info-container">
            <h1>Personal Information</h1>
            {personalInfo && (
                <div className="personal-details">
                    <p><strong>Username:</strong> {personalInfo.username}</p>
                    <p><strong>Email:</strong> {personalInfo.email}</p>
                    <p><strong>First Name:</strong> {personalInfo.first_name}</p>
                    <p><strong>Last Name:</strong> {personalInfo.last_name}</p>
                    <p><strong>Birthday:</strong> {personalInfo.birthday}</p>
                    <p><strong>Gender:</strong> {personalInfo.gender}</p>
                    <p><strong>Height:</strong> {personalInfo.height} cm</p>
                    <p><strong>Weight:</strong> {personalInfo.weight} kg</p>
                    <p><strong>Family Head:</strong> {personalInfo.is_family_head ? 'Yes' : 'No'}</p>
                </div>
            )}

            {familyMembers.length > 0 && (
                <div className="family-members-section">
                    <h2>Family Members</h2>
                    <ul>
                        {familyMembers.map(member => (
                            <li key={member.id}>
                                <p><strong>First Name:</strong> {member.first_name}</p>
                                <p><strong>Last Name:</strong> {member.last_name}</p>
                                <p><strong>Birthday:</strong> {member.birthday}</p>
                                <p><strong>Gender:</strong> {member.gender}</p>
                                <p><strong>Height:</strong> {member.height} cm</p>
                                <p><strong>Weight:</strong> {member.weight} kg</p>
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
};

export default PersonalInfo;
