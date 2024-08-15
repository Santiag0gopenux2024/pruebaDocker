import React, { useEffect, useState } from 'react';
import axios from 'axios';

function UserList() {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetchUsers();
    }, []);

    const fetchUsers = async () => {
        try {
            console.log(process.env.REACT_APP_API_HOST)
            const response = await axios.get('http://localhost:5000/user');
            setUsers(response.data);
        } catch (error) {
            console.error('Error fetching users:', error);
        }
    };

    return (
        <div>
            <h2>User List</h2>
            <ul>
                {users.map(user => (
                    <li key={user.id}>
                        <img src={user.profile_picture} alt="User Profile" style={{ width: 100, height: 100 }} />
                        <p>{user.username}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default UserList;
