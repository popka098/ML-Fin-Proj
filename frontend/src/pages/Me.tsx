import { useAuth } from "../context/AuthContext";
import { Navigate, useNavigate } from "react-router-dom";
import { useState } from "react";
import { addCrystals } from "../api/user";

export default function Me() {
    const { user, logout, loading, refreshUser } = useAuth();
    const [amount, setAmount] = useState(50);
    const navigate = useNavigate();
    const handleLogout = async () => {
        await logout();
        navigate("/login")
    };
    const handleAdd = async () => {
        await addCrystals(amount);
        await refreshUser();
    }

    if (loading) return <div>Loading...</div>;
    if (!user) return <Navigate to="/login"/>;

    console.log("USER:", user);
    return (
        <div>
            <h1>{user.email}</h1>
            <h2>Crystals: {user.crystals}</h2>
            <input
                type="range"
                min={1}
                max={100}
                onChange={(e) => setAmount(Number(e.target.value))}
            />
            <div>Amount: {amount}</div>
            <button onClick={handleAdd}>Add Crystals</button>
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
}