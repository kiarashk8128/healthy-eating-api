import {useState} from 'react';
import {useNavigate} from 'react-router-dom'; // Updated import
import axios from 'axios';
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
    const [familyMemberData, setFamilyMemberData] = useState([]);
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');
    const [usernameError, setUsernameError] = useState('');
    const [emailError, setEmailError] = useState('');
    const [passwordError, setPasswordError] = useState('');
    const navigate = useNavigate(); // Updated to useNavigate

    const handleChange = (e) => {
        setFormData({...formData, [e.target.name]: e.target.value});
    };

    const handleFamilyMemberChange = (index, e) => {
        const updatedFamilyMembers = [...familyMemberData];
        updatedFamilyMembers[index][e.target.name] = e.target.value;
        setFamilyMemberData(updatedFamilyMembers);
    };

    const addFamilyMember = () => {
        setFamilyMemberData([
            ...familyMemberData,
            {first_name: '', last_name: '', birthday: '', gender: '', height: '', weight: ''}
        ]);
    };

    const removeFamilyMember = (index) => {
        const updatedFamilyMembers = [...familyMemberData];
        updatedFamilyMembers.splice(index, 1);
        setFamilyMemberData(updatedFamilyMembers);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const dataToSubmit = {...formData, family_members: familyMemberData};
        try {
            const response = await axios.post('http://localhost/auth/signup/', dataToSubmit);
            setSuccess('Signup successful!');
            setError('');
            setUsernameError('');
            setEmailError('');
            setPasswordError('');
            console.log('Signup successful!', response.data);
            navigate('/login'); // Redirect to login page after successful signup
        } catch (err) {
            setError('');
            setUsernameError('');
            setEmailError('');
            setPasswordError('');
            if (err.response && err.response.status === 400) {
                if (err.response.data.username) {
                    console.log("meow1")
                    setUsernameError(err.response.data.username);  // Display username-specific error
                }
                else if (err.response.data.email) {
                    console.log("meow2")
                    setEmailError(err.response.data.email);  // Display email-specific error
                }
                else if (err.response.data.password) {
                    console.log("meow3")
                    setPasswordError(err.response.data.password);  // Display password-specific error
                } else {
                    setError('Signup failed. Please check the fields and try again.');
                }
            }
        }
    };

    return (
        <div className="form-container">
            <div className="image-container">
                <img src={healthyFoodImage} alt="Healthy Food"/>
            </div>
            <div className="form-content">
                <h1>Sign Up</h1>
                {error && <p style={{color: 'red'}}>{error}</p>}
                {success && <p style={{color: 'green'}}>{success}</p>}
                <form onSubmit={handleSubmit}>
                    <input
                        type="text"
                        name="username"
                        placeholder="Username"
                        value={formData.username}
                        onChange={handleChange}
                    />
                    {usernameError && <p style={{ color: 'red' }}>{usernameError}</p>} {/* Display username error */}

                    <input
                        type="password"
                        name="password"
                        placeholder="Password"
                        value={formData.password}
                        onChange={handleChange}
                    />
                    {passwordError && <p style={{ color: 'red' }}>{passwordError}</p>} {/* Display username error */}

                    <input
                        type="email"
                        name="email"
                        placeholder="Email"
                        value={formData.email}
                        onChange={handleChange}
                    />
                    {emailError && <p style={{ color: 'red' }}>{emailError}</p>} {/* Display username error */}

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
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                        <option value="Other">Other</option>
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
                            onChange={(e) => setFormData({...formData, is_family_head: e.target.checked})}
                        />
                        Are you the family head?
                    </label>

                    {formData.is_family_head && (
                        <div className="family-members-section">
                            <h2>Family Members</h2>
                            {familyMemberData.map((member, index) => (
                                <div key={index} className="family-member">
                                    <input
                                        type="text"
                                        name="first_name"
                                        placeholder="First Name"
                                        value={member.first_name}
                                        onChange={(e) => handleFamilyMemberChange(index, e)}
                                    />
                                    <input
                                        type="text"
                                        name="last_name"
                                        placeholder="Last Name"
                                        value={member.last_name}
                                        onChange={(e) => handleFamilyMemberChange(index, e)}
                                    />
                                    <input
                                        type="date"
                                        name="birthday"
                                        value={member.birthday}
                                        onChange={(e) => handleFamilyMemberChange(index, e)}
                                    />
                                    <select
                                        name="gender"
                                        value={member.gender}
                                        onChange={(e) => handleFamilyMemberChange(index, e)}
                                    >
                                        <option value="">Select Gender</option>
                                        <option value="Male">Male</option>
                                        <option value="Female">Female</option>
                                        <option value="Other">Other</option>
                                    </select>
                                    <input
                                        type="number"
                                        name="height"
                                        placeholder="Height (cm)"
                                        value={member.height}
                                        onChange={(e) => handleFamilyMemberChange(index, e)}
                                    />
                                    <input
                                        type="number"
                                        name="weight"
                                        placeholder="Weight (kg)"
                                        value={member.weight}
                                        onChange={(e) => handleFamilyMemberChange(index, e)}
                                    />
                                    <button type="button" onClick={() => removeFamilyMember(index)}>Remove</button>
                                </div>
                            ))}
                            <button type="button" onClick={addFamilyMember}>Add Family Member</button>
                        </div>
                    )}

                    <button type="submit">Sign Up</button>
                </form>
                <button className="back-button" onClick={() => navigate('/')}>Back to Landing Page</button>
                {/* Back Button */}
            </div>
        </div>
    );
};

export default Signup;
