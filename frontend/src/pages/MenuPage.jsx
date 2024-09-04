import { useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import axios from 'axios';
import '../MenuPage.css';

const MenuPage = () => {
    const [menus, setMenus] = useState([]);
    const [selectedUser, setSelectedUser] = useState(null);
    const [familyMembers, setFamilyMembers] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchData = async () => {
            try {
                const menuResponse = await axios.get('http://localhost/nutrition/menus/', {
                    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
                });
                setMenus(menuResponse.data);

                const userResponse = await axios.get('http://localhost/auth/user-info/', {
                    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
                });
                if (userResponse.data.is_family_head) {
                    setFamilyMembers(userResponse.data.family_members);
                }
            } catch (error) {
                console.error('Error fetching menus:', error);
            }
        };

        fetchData();
    }, []);

    const generateNewMenus = async (userId, isFamilyMember = false, generateForAll = false) => {
        try {
            const endpoint = generateForAll
                ? 'http://localhost/nutrition/generate-menus-for-all/'
                : 'http://localhost/nutrition/generate-menus/';
            const requestData = generateForAll ? {} : { family_member_id: isFamilyMember ? userId : null };

            await axios.post(endpoint, requestData, {
                headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
            });
            window.location.reload(); // Reload the page to fetch new menus
        } catch (error) {
            console.error('Error generating new menus:', error);
        }
    };

    const renderMenu = (menu, index) => {
        const userKey = menu.family_member ? `${menu.family_member.first_name} ${menu.family_member.last_name}` : Object.keys(menu.menu_data)[0];
        const menuData = menu.menu_data[userKey];

        if (!menuData) {
            console.error(`No menu data found for: ${menu.family_member ? `${menu.family_member.first_name}'s Menu` : 'Your Menu'}`);
            return null;
        }

        const orderedDays = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];

        return (
            <div key={index} className="menu-item">
                <table className="menu-table">
                    <thead>
                    <tr>
                        <th>Day</th>
                        <th>Menu</th>
                    </tr>
                    </thead>
                    <tbody>
                    {orderedDays.map((day, dayIndex) => (
                        <tr key={dayIndex}>
                            <td><strong>{day}</strong></td>
                            <td>
                                {Array.isArray(menuData[day]) ? (
                                    menuData[day].map((item, itemIndex) => (
                                        <span key={itemIndex}>
                                                {item.food_item} ({item.serving_size})
                                            {itemIndex < menuData[day].length - 1 ? ', ' : ''}
                                            </span>
                                    ))
                                ) : (
                                    'No data available'
                                )}
                            </td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </div>
        );
    };

    const filterAndRenderMenus = () => {
        const filteredMenus = selectedUser
            ? menus.filter((menu) => menu.family_member?.id === parseInt(selectedUser) || (!menu.family_member && selectedUser === 'self'))
            : menus;

        const groupedMenus = {};

        filteredMenus.forEach((menu, index) => {
            const userId = menu.family_member ? menu.family_member.id : 'self';
            if (!groupedMenus[userId]) {
                groupedMenus[userId] = {
                    name: menu.family_member ? `${menu.family_member.first_name} ${menu.family_member.last_name}` : 'Your Menu',
                    menus: [],
                    userId: userId,  // Track the user ID
                    isFamilyMember: !!menu.family_member  // Track if this is a family member
                };
            }
            groupedMenus[userId].menus.push(renderMenu(menu, index));
        });

        return Object.entries(groupedMenus).map(([userId, userMenus]) => (
            <div key={userId} className="user-menu-section">
                <h2>{userMenus.name}</h2>
                {userMenus.menus}
                {selectedUser === userId.toString() && (
                    <button
                        className="generate-button"
                        onClick={() => generateNewMenus(userMenus.userId, userMenus.isFamilyMember)}
                    >
                        Generate New Menu for {userMenus.name}
                    </button>
                )}
            </div>
        ));
    };

    return (
        <div className="menu-container">
            <h1>Weekly Menus</h1>
            {familyMembers.length > 0 && (
                <div className="family-menu">
                    <h2>Select User</h2>
                    <select onChange={(e) => setSelectedUser(e.target.value || null)}>
                        <option value="">All Users</option>
                        <option value="self">Your Menu</option>
                        {familyMembers.map((member) => (
                            <option key={member.id} value={member.id}>
                                {member.first_name} {member.last_name}
                            </option>
                        ))}
                    </select>
                </div>
            )}
            <ul className="menu-list">{filterAndRenderMenus()}</ul>
            {!selectedUser && (
                <button className="generate-button" onClick={() => generateNewMenus(null, false, true)}>
                    Generate New Menu for All Users
                </button>
            )}
            <button onClick={() => navigate('/main')}>Back to Main Page</button> {/* Back Button */}

        </div>
    );
};

export default MenuPage;
