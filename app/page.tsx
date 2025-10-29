"use client";
import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [text, setText] = useState("");
  const [result, setResult] = useState<{ label: string } | null>(null);
  const [loading, setLoading] = useState(false);

  const analyze = async () => {
    if (!text.trim()) return alert("Enter the text first!");
    setLoading(true);
    try {
      const res = await axios.post("http://localhost:8000/predict", { text });
      setResult(res.data);
    } catch (err) {
      alert("Unable to connect to the backend ");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-8 bg-gray-50">
      <h1 className="text-3xl font-bold mb-6 text-blue-950 text-shadow-amber-950">Text Sentiment Analysis</h1>
      

      <textarea
        className="w-96 h-13 p-3 border border-gray-400 rounded-md focus:outline-blue-400"
        placeholder="Type something here...."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <button
        className="mt-4 px-6 py-2 bg-blue-700 text-white rounded-lg hover:bg-blue-0 disabled:bg-gray-400"
        onClick={analyze}
        disabled={loading}
      >
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      {result && (
        <div className="mt-6 bg-white shadow-md p-5 rounded-md w-96 text-center border">
          <p className="text-lg font-semibold">
            Result : <span className="capitalize">{result.label}</span>
          </p>

          {
          result.label === "Negative" && (
            <div className="mt-4 text-red-600 font-bold">
               Suggestion: Please review this statement!
            </div>
          )}
        </div>
      )}
    </main>
  );
}
