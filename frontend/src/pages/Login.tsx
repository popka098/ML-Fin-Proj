import { useState, useEffect } from "react";
import { useAuth } from "../context/AuthContext";
import { useNavigate, Link } from "react-router-dom";
// import { login } from "../api/auth";

export default function Login() {
    const { login, user } = useAuth();
    const navigate = useNavigate();

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const handleLogin = async () => {
        try {
            setLoading(true);
            setError("");

            await login(username, password);
        } catch (e: any) {
            setError(e.response?.data?.detail || "Login error")
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        if (user !== null) {
            navigate("/me");
        }
    }, [user]);

    return (
        <div className="min-h-[80vh] flex items-center justify-center px-4">
            <div className="w-full max-w-md p-6 border rounded-2xl shadow-sm">

                <h1 className="text-2xl font-bold mb-6 text-center">
                    Login
                </h1>

                <div className="space-y-4">
                    <input
                        type="email"
                        placeholder="Email"
                        className="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                        onChange={(e) => setUsername(e.target.value)}
                    />

                    <input
                        placeholder="Password"
                        type="password"
                        className="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                        onChange={(e) => setPassword(e.target.value)}
                    />
                    <button
                        onClick={handleLogin}
                        disabled={loading}
                        className="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition disabled:opacity-50"
                    >
                        {loading ? "Logging in..." : "Login"}
                    </button>
                    {error && (
                        <div className="text-red-500 text-sm text-center">
                            {error}
                        </div>
                    )}
                </div>

                <div className="mt-6 text-center text-sm">
                    No account?{" "}
                    <Link to="/register" className="text-blue-600 hover:underline">
                        Register
                    </Link>
                </div>

            </div>
        </div>
    );
}