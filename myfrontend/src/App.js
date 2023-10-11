import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Cart from "./pages/Cart";
import Signup from "./pages/Signup";
import Login from "./pages/Login";

export default function App() {
  return (
    <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Cart" element={<Cart />} />
          <Route path="/Signup" element={<Signup />} />
          <Route path="/Login" element={<Login />} />
        </Routes>
    </BrowserRouter>
  );
}
