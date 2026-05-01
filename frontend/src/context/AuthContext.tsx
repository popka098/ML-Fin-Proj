import { createContext, useContext, useState, useEffect } from "react";
import { login as apiLogin, getMe, logout } from "../api/auth";
import { api, setAccessToken } from "../api/client";

type User = {
    id: number;
    email: string;
};

type AuthContextType = {
    user: User | null;
    login: (email: string, password: string) => Promise<void>;
    logout: () => void;
};

const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({ children }: any) {
    const [user, setUser] = useState<User | null>(null);

    useEffect(() => {
        const init = async () => {
            try {
                const refresh_token = localStorage.getItem("refresh_token");

                if (!refresh_token) return;

                const res = await api.post("/auth/refresh", null, {
                    params: { refresh_token },
                });

                setAccessToken(res.data.access_token);

                const me = await getMe();
                setUser(me);
            } catch {
                logout();
            }
        };

        init();
    }, []);

    const login = async (email: string, password: string) => {
        const res = await apiLogin(email, password);

        setAccessToken(res.access_token);
        localStorage.setItem("refresh_token", res.refresh_token);

        const me = await getMe();
        setUser(me);
    };

    const logout = () => {
        setUser(null);
        localStorage.removeItem("refresh_token");
        setAccessToken(null as any);
    };

    return (
        <AuthContext.Provider value={{user, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
}

export const useAuth = () => {
    return useContext(AuthContext)!;
};