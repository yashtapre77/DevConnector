import React from "react";

function Navbar() {

    const guestLinks = (
        <ul>
          <li>
            <Link to="/profiles">Developers</Link>
          </li>
          <li>
            <NavLink to="/register">Register</NavLink>
          </li>
          <li>
            <NavLink to="/login">Login</NavLink>
          </li>
        </ul>
      );
    
      const authLinks = (
        <ul>
          <li>
            <Link to="/profiles">Developers</Link>
          </li>
          <li>
            <Link to="/posts">Posts</Link>
          </li>
          <li>
            <Link to="/dashboard">
              <i className="fas fa-user"></i>{" "}
              <span className="hide-sm">Dashboard</span>
            </Link>
          </li>
          <li>
            <a href="/logout" onClick={onLogout}>
              <i className="fas fa-sign-out-alt"></i>{" "}
              <span className="hide-sm">Logout</span>
            </a>
          </li>
        </ul>
      );
      
  return (
    <div>
      <nav className="navbar bg-dark">
        <h1>
          <Link to="/">
            <i className="fas fa-code"></i> DevConnector
          </Link>
        </h1>
        {!loading && (
          <Fragment>{isAuthenticated ? authLinks : guestLinks}</Fragment>
        )}
      </nav>
    </div>
  );
}

export default Navbar;
