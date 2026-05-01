import axios from "axios";

export const api = axios.create({
    baseURL: "http://localhost:8000",
    withCredentials: true,
});

let accessToken: string | null = null;
let isRefreshing = false;
let failedQueue: any[] = [];

const ProccessQueue = (error: any, token: string | null = null) => {
    failedQueue.forEach((prom) => {
        if (error) {
            prom.reject(error);
        } else {
            prom.resolve(token);
        }
    });

    failedQueue = [];
};

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
        const originalRequest = error.config;

        if (!error.response || error.response.status !== 401){
            return Promise.reject(error)
        }
        if (originalRequest.url.include("/auth/refresh")) {
            return Promise.reject(error);
        }
        if (isRefreshing) {
            return new Promise((resolve, reject) => {
                failedQueue.push({ resolve, reject });
            }).then((token) => {
                originalRequest.headers.Authorization = `Bearer ${token}`;
                return api.request(originalRequest);
            });
        }

        isRefreshing = true;

        try {
            const res = await api.post(
                "/auth/refresh",
                {},
                { withCredentials: true }
            );
            
            const newToken = res.data.access_token;
            accessToken = newToken;

            api.defaults.headers.common.Authorization = `Bearer ${newToken}`;
            originalRequest.headers.Authorization =  `Bearer ${newToken}`;

            ProccessQueue(null, newToken);

            return api.request(originalRequest);
        } catch (err) {
            ProccessQueue(err, null);
            window.location.href = "/login";
            return Promise.reject(err);
        } finally {
            isRefreshing = false;
        }
    }
);