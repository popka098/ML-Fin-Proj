import { useState, useEffect } from "react";
import { useAuth } from "../context/AuthContext";
import { useNavigate, Link } from "react-router-dom";
// import { login } from "../api/auth";

export default function Login() {
    const { login, user } = useAuth();
    const navigate = useNavigate();

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async () => {
        await login(username, password);
    };

    useEffect(() => {
        if (user !== null) {
            navigate("/me");
        }
    }, [user]);

    return (
        <div>
        <h1>Login</h1>
        <input
            placeholder="Email"
            onChange={(e) => setUsername(e.target.value)}
        />
        <input
            placeholder="Password"
            type="password"
            onChange={(e) => setPassword(e.target.value)}
        />
        <button onClick={handleLogin}>Login</button>
        <br />
        <Link to="/register">No account?</Link>
        </div>
    );
}