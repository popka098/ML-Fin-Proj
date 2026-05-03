import { api } from "./client"

export const addCrystals = async (amount: number) => {
    const res = await api.post(
        "/api/v1/purchases/add-crystals",
        null,
        {params: { amount },}
    );

    return res.data;
}