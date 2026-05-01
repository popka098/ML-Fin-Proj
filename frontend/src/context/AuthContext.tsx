import { createContext, useContext, useState, useEffect } from "react";
import { login as apiLogin, getMe, logout } from "../api/auth";
import { api, setAccessToken } from "../api/client";

type User = {
    id: number;
    email: string;
};

type AuthContextType = {
    user: User | null;
    loading: boolean;
    login: (email: string, password: string) => Promise<void>;
    logout: () => void;
};

const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({ children }: any) {
    const [user, setUser] = useState<User | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const init = async () => {
            try {
                const res = await api.post("/auth/refresh");

                setAccessToken(res.data.access_token);

                const me = await getMe();
                setUser(me);
            } catch {
                setUser(null);
                // logout();
            } finally {
                setLoading(false);
            }
        };

        init();
    }, []);

    const login = async (email: string, password: string) => {
        const res = await apiLogin(email, password);

        setAccessToken(res.access_token);

        const me = await getMe();
        setUser(me);
    };

    const logout = async () => {
        try {
            await api.post("/auth/logout");
        } catch {}
        setUser(null);
        setAccessToken(null as any);
    };

    return (
        <AuthContext.Provider value={{
            user,
            loading,
            login,
            logout
        }}>
            {children}
        </AuthContext.Provider>
    );
}

export const useAuth = () => {
    return useContext(AuthContext)!;
};