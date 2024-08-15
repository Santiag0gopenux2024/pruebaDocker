import React, { useState } from 'react';
import axios from 'axios';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');

    const handleLogin = async (e) => {
        e.preventDefault();
        setMessage('');
        try {
            const response = await axios.post('http://localhost:5000/login', {
                username,
                password
            });
            setMessage(`Login successful! Your token: ${response.data.token}`);
        } catch (error) {
            if (error.response) {
                // Respuestas específicas del servidor
                setMessage('Failed to login: ' + error.response.data.message);
            } else {
                // Algunos errores de conexión o alcanzado el servidor
                setMessage('Login failed: Server unreachable');
            }
        }
    };

    return (
        <div>
            <h2>Login</h2>
            <form onSubmit={handleLogin}>
                <label>
                    Username:
                    <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
                </label>
                <label>
                    Password:
                    <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                </label>
                <button type="submit">Login</button>
            </form>
            {message && <div style={{ marginTop: '20px', color: message.includes('successful') ? 'green' : 'red' }}>{message}</div>}
        </div>
    );
}

export default Login;
