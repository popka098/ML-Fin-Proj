import { useState, useEffect } from "react";
import { register } from "../api/auth";
import { useAuth } from "../context/AuthContext";
import { useNavigate, Link } from "react-router-dom";

export default function Register() {
    const { user, login } = useAuth();
    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirm, setConfirm] = useState("");

    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const handleRegister = async () => {
        if (password !== confirm) {
            return setError("Passwords do not match");
        }

        try {
            setLoading(true);
            setError("");

            await register(email, password);
            const user = await login(email, password);

            // !!!
            console.log("USER AFTER LOGIN:", user);

        } catch(e: any) {
            alert(e.response?.data?.detail || "Registration error");
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
                    Register
                </h1>

                <div className="space-y-4">
                    <input
                        type="email"
                        placeholder="Email"
                        onChange={(e) => setEmail(e.target.value)}
                        className="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                    <input
                        type="password"
                        placeholder="Password"
                        onChange={(e) => setPassword(e.target.value)}
                        className="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />

                    <button 
                        onClick={handleRegister}
                        disabled={loading}
                        className="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition disabled:opacity-50"
                    >
                        {loading ? "Creating..." : "Register"}
                    </button>

                {error && (
                    <div className="text-red-500 text-sm text-center">
                        {error}
                    </div>
                )}
            </div>

            <div className="mt-6 text-center text-sm">
                Already have an account?{" "}
                <Link to="/login" className="text-blue-600 hover:underline">
                    Login
                </Link>
            </div>

            </div>
        </div>
    );
}