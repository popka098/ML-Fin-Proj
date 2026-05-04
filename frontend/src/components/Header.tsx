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
        <header className="border-b">
            <div className="max-w-5xl mx-auto px-4 py-3 flex justify-between items-center">

                <Link to="/" className="font-bold text-lg">App</Link>

                <div>
                    {loading ? (
                        <span>Loading...</span>
                    ) : user ? (
                        <div className="flex items-center gap-4">

                            <div className="text-sm text-gray-600">
                                💎 {user.crystals}
                            </div>

                            <div className="text-sm">
                                <Link to="/me">{user.email}</Link>
                            </div>

                            <button onClick={handleLogout} className="text-red-500 hover:underline">
                                Logout
                            </button>

                        </div>
                    ) : (
                        <div className="flex gap-4">
                            <Link to="/login" className="hover:underline">
                                Login
                            </Link>
                            <Link to="/register" className="hover:underline">
                                Register
                            </Link>
                        </div>
                    )}
                </div>
            </div>
        </header>
    );
}