import React from 'react';
import '../Styles/Nav.css'
import {Link} from 'react-router-dom';

function Navbar() {
  return (
    <div>
      <nav className="navbar navbar-expand-lg bg-body-tertiary">
  <div className="container-fluid">
    <Link className="navbar-brand" href="/">Logo</Link>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse" id="navbarSupportedContent">
      <ul className="navbar-nav me-auto mb-2 mb-lg-0">
        <li className="nav-item">
          <Link className="nav-link active" aria-current="page" href="/">Home</Link>
        </li>
        <li className="nav-item">
          <Link className="nav-link" href="/Cart">Cart</Link>
        </li>
        <li className="nav-item dropdown">
          <Link className="nav-link dropdown-toggle" href="/Cartegory" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Cartegory
          </Link>
          <ul className="dropdown-menu">
            <li><Link className="dropdown-item" href="/Ho">Procut 1</Link></li>
            <li><Link className="dropdown-item" href="#">Product 2</Link></li>
            <li><hr className="dropdown-divider"/></li>
            <li><Link className="dropdown-item" href="#">Something else here</Link></li>
          </ul>
        </li>
        <li className="nav-item">
          <Link className="nav-link disabled" aria-disabled="true">Signup</Link>
        </li>
      </ul>
    </div>
  </div>
</nav>
    </div>
  )
}

export default Navbar