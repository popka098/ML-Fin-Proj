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
        <div className="w-full max-w-3xl mx-auto mt-10 px-4">
            <h1 className="text-3xl font-bold mb-6">Text analysis</h1>

            <textarea
                className="w-full resize-none p-4 border rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
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
            <button 
                onClick={handleAnalyze} 
                disabled={loading}
                className="mt-4 w-full bg-blue-600 text-white py-3 rounded-xl hover:bg-blue-700 transition disabled:opacity-50"
            >
                {loading ? "Analyzing" : "Analyze"}
            </button>

            {error && <div className="mt-4 text-red-500">{error}</div>}

            {result && (
                <div className="mt-6 p-4 border rounded-xl bg-gray-50">
                    <h3 className="font-semibold mb-2">Result:</h3>

                    <div className="space-y-2">
                        <div>Sentiment: <b>{result.sentiment_pred_label}</b></div>
                        <div>Topic: <b>{result.topic_pred_label}</b></div>
                    </div>
                </div>
            )}
        </div>
    );
}