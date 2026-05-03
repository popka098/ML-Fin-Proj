import { api } from "./client";

export const getAllPreds = async (text: string) => {
    const res = await api.get(
        "/api/v1/mlmomdels/all",
        { params: { text }}
    );
    return res.data;
}