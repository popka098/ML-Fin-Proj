import { useState } from "react";
import { login } from "../api/auth";

export default function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = async () => {
        const data = await login(username, password);
        console.log(data);
    };

    return (
        <div>
            <input onChange={(e) => setUsername(e.target.value)} />
            <input type="password" onChange={(e) => setPassword(e.target.value)} />
            <button onClick={handleSubmit}>Login</button>
        </div>
    );
}