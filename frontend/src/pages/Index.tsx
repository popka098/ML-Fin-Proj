import { useState } from "react";
import { getAllPreds } from "../api/mlmodel";
import { useAuth } from "../context/AuthContext";

export default function Index() {
    const { user, refreshUser } = useAuth();

    const [text, setText] = useState("");
    const [result, setResult] = useState<any>(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const handleAnalyze = async () => {
        if (!text.trim()) return;

        try {
            setLoading(true);
            setError("");

            const res = await getAllPreds(text);
            setResult(res);

            await refreshUser();
        } catch (e: any) {
            setError(e.response?.data?.detail || "Error");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h1>Text analysis</h1>

            <textarea
                rows={5}
                placeholder="Enter text..."
                value={text}
                onChange={(e) => setText(e.target.value)}
                style={{
                    width: "90%",
                    resize: "none",
                }}
            />
            <br />
            <button onClick={handleAnalyze} disabled={loading}>
                {loading ? "Analyzing" : "Analyze"}
            </button>

            {error && <div style={{ color: "red" }}>{error}</div>}

            {result && (
                <div>
                    <h3>Result:</h3>
                    <pre>
                        {JSON.stringify(result, null, 2)}
                    </pre>
                </div>
            )}
        </div>
    );
}