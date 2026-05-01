import { useAuth } from "../context/AuthContext";
import { useEffect, useState } from "react";
import { getMe } from "../api/auth";

export default function Me() {
    const { user, logout } = useAuth();

    if (!user) return <div>Loading...</div>

    return (
        <div>
            <h1>{user.email}</h1>
            <button onClick={logout}>Logout</button>
        </div>
    );
}