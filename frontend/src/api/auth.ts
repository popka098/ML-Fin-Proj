import { api, setAccessToken } from "./client";

export const login = async (username: string, password: string) => {
    const formData = new URLSearchParams();
    formData.append("username", username);
    formData.append("password", password);

    const res = await api.post("/auth/login", formData, {
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
    });
    // setAccessToken(res.data.access_token);
    return res.data;
};

export const getMe = async () => {
    const res = await api.get("/api/v1/users/me");
    return res.data;
};

export const logout = async () => {
    await api.post("/auth/logout");
};