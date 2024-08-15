import React, { useState } from 'react';
import axios from 'axios';

function CreateUser() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post('http://localhost:5000/user', { username, password });
            console.log(response.data);
            alert('User created successfully!');
        } catch (error) {
            console.error('Failed to create user:', error);
            alert('Failed to create user');
        }
    };

    return (
        <div>
            <h2>Create User</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Username:
                    <input type="text" value={username} onChange={e => setUsername(e.target.value)} />
                </label>
                <label>
                    Password:
                    <input type="password" value={password} onChange={e => setPassword(e.target.value)} />
                </label>
                <button type="submit">Create User</button>
            </form>
        </div>
    );
}

export default CreateUser;
