import React from 'react';
import UserList from './components/UserList';
import CreateUser from './components/CreateUser';
import Login from './components/Login';

import './App.css';


function App() {
    return (        
        <div className="App">
            <Login />
            <CreateUser />
            <UserList />
        </div>
    );
}

export default App;
