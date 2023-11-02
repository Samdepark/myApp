import React, { useState } from "react";
import "../Styles/login.css";

function Login() {
  const [formData, setFormData] = useState({ username: "", password: "" });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Login form submitted:", formData);
  };

  return (
    <form onSubmit={handleSubmit} className="login">
      <input
        type="text"
        className="inpt"
        name="username||email"
        placeholder="username/email"
        onChange={handleChange}
      />
      <input
        type="password"
        className="inpt"
        name="password"
        placeholder="Password"
        onChange={handleChange}
      />
      <button type="submit" className="btn">
        Login
      </button>
    </form>
  );
}

export default Login;
