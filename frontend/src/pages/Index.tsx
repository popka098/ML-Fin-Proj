import { useAuth } from "../context/AuthContext";

export default function Index() {
    const { user } = useAuth();

    return (
        <div>
            <h1>Text analyzer</h1>
        </div>
    )
}