import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Header() {
    const { user, logout, loading } = useAuth();
    const navigate = useNavigate();

    const handleLogout = async () => {
        await logout();
        navigate("/login");
    };

    return (
        <header style={{ padding: "10px", borderBottom: "1px solid #ccc" }}>
            <nav style={{ display: "flex", justifyContent: "space-between" }}>
                <div>
                    <Link to="/">Home</Link>
                </div>
                <div>
                    {loading ? (
                        <span>Loading...</span>
                    ) : user ? (
                        <>
                            <span style={{ marginRight: "10px" }}>
                                💎 {user.crystals}
                            </span>
                            <span style={{ marginRight: "10px" }}>
                                <Link to="/me">{user.email}</Link>
                            </span>
                            <button onClick={handleLogout}>Logout</button>
                        </>
                    ) : (
                        <>
                            <Link to="/login" style={{ marginRight: "10px" }}>
                                Login
                            </Link>
                            <Link to="/register">
                                Register
                            </Link>
                        </>
                    )}
                </div>
            </nav>
        </header>
    );
}