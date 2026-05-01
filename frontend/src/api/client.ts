import axios from "axios";

export const api = axios.create({
    baseURL: "http://localhost:8000",
    withCredentials: true,
});

let accessToken: string | null = null;

export const setAccessToken = (token: string) => {
    accessToken = token;
}

api.interceptors.request.use((config) => {
    if (accessToken) {
        config.headers.Authorization = `Bearer ${accessToken}`;
    }
    return config;
});

api.interceptors.response.use(
    (res) => res,
    async (error) => {
        if (error.response?.status === 401) {
            try {
                const res = await axios.post(
                    "http://localhost:8000/auth/refresh",
                    {},
                    { withCredentials: true }
                );
                accessToken = res.data.access_token;

                error.config.headers.Authorization = `Bearer ${accessToken}`;
                return api.request(error.config);
            } catch {
                window.location.href = "/login";
            }
        }
        return Promise.reject(error);
    }
);