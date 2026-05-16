import React from 'react';
import { Link, useLocation } from 'react-router-dom';

const Header = () => {
  const location = useLocation();

  return (
    <header className="header">
      <div className="header-content">
        <Link to="/" className="logo">
          <span>🔧</span>
          <span>Legacy Code Surgeon AI</span>
        </Link>
        <nav className="nav">
          <Link to="/" className={location.pathname === '/' ? 'active' : ''}>
            Home
          </Link>
        </nav>
      </div>
    </header>
  );
};

export default Header;

// Made with Bob
