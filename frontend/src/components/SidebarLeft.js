// src/components/SidebarLeft.js
import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';

function SidebarLeft() {
    const location = useLocation();
    const userData = location.state ? location.state : null;

    return (
        <div className="sidebar sidebar-left">
        <h2>Sidebar Left</h2>
        <h2>{userData.user.name}</h2>
        {/* Add sidebar content as needed */}
        </div>
    );
    }

export default SidebarLeft;
