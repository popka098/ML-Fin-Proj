import { createContext, useContext, useState, useEffect } from "react";
import { apiLogin as apiLogin, getMe, logout } from "../api/auth";
import { api, setAccessToken } from "../api/client";

type User = {
    id: number;
    email: string;
    crystals: number;
};

type AuthContextType = {
    user: User | null;
    loading: boolean;
    login: (email: string, password: string) => Promise<void>;
    logout: () => void;
    refreshUser: () => Promise<void>;
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

        // !!!
        console.log("ACCESS TOKEN:", res.access_token);

        setAccessToken(res.access_token);

        const me = await getMe();

        // !!!
        console.log("ME:", me);

        setUser(me);

        return me;
    };

    const logout = async () => {
        try {
            await api.post("/auth/logout");
        } catch {}
        setUser(null);
        setAccessToken(null as any);
    };

    const refreshUser = async () => {
        const me = await getMe();
        setUser(me);
    };

    return (
        <AuthContext.Provider value={{
            user,
            loading,
            login,
            logout,
            refreshUser,
        }}>
            {children}
        </AuthContext.Provider>
    );
}

export const useAuth = () => {
    return useContext(AuthContext)!;
};