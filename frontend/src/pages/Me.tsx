import { useAuth } from "../context/AuthContext";
import { Navigate, useNavigate } from "react-router-dom";

export default function Me() {
    const { user, logout, loading } = useAuth();
    const navigate = useNavigate();
    const handleLogout = async () => {
        await logout();
        navigate("/login")
    };

    if (loading) return <div>Loading...</div>;
    if (!user) return <Navigate to="/login"/>;

    console.log("USER:", user);
    return (
        <div>
            <h1>{user.email}</h1>
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
}