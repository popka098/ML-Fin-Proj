import { useState, useEffect } from "react";
import { register } from "../api/auth";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

export default function Register() {
    const { user, login } = useAuth();
    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleRegister = async () => {
        try {
            await register(email, password);
            const user = await login(email, password)

            // !!!
            console.log("USER AFTER LOGIN:", user);

        } catch(e: any) {
            alert(e.response?.data?.detail || "Registration error");
        }
    };

    useEffect(() => {
        if (user !== null) {
            navigate("/me");
        }
    }, [user]);

    return (
        <div>
            <h1>Register</h1>

            <input
                placeholder="Email"
                onChange={(e) => setEmail(e.target.value)}
            />
            <input
                type="password"
                placeholder="Password"
                onChange={(e) => setPassword(e.target.value)}
            />

            <button onClick={handleRegister}>Register</button>
        </div>
    );
}