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
        <div className="max-w-xl mx-auto mt-10 px-4">
            <h1 className="text-2xl font-bold mb-4">{user.email}</h1>

            <div className="mb-4">
                💎 Crystals: <b>{user.crystals}</b>
            </div>

            <input
                type="range"
                min={1}
                max={100}
                onChange={(e) => setAmount(Number(e.target.value))}
                className="w-full"
            />

            <div className="mt-2">Amount: {amount}</div>

            <button onClick={handleAdd} className="mt-4 w-full bg-green-600 text-white py-2 rounded-lg hover:bg-green-700">
                Add Crystals
            </button>
        </div>
    );
}