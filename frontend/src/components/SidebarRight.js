// src/components/SidebarRight.js
import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';

function SidebarRight() {
  const location = useLocation();
  const userData = location.state ? location.state : null;
  
  return (
    <div className="sidebar sidebar-right">
      <h2>Sidebar Right</h2>
      {/* Add sidebar content as needed */}
    </div>
  );
}

export default SidebarRight;
