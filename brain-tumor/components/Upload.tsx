"use client";
import { useState } from "react";
import { predict } from "@/lib/api";
import Loader from "./Loader";
import ResultCard from "./ResultCard";

export default function Upload() {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [preview, setPreview] = useState<string | null>(null);

  const handleFileChange = (e: any) => {
    const f = e.target.files?.[0];
    if (!f) return;

    setFile(f);
    setPreview(URL.createObjectURL(f));
  };

  const handleUpload = async () => {
    if (!file) return;

    setLoading(true);
    setResult(null);

    try {
      const data = await predict(file);
      setResult(data);
    } catch (err) {
      alert("Error processing MRI");
    }

    setLoading(false);
  };

  return (
    <div className="flex flex-col items-center gap-6">
      <div className="bg-white shadow-lg rounded-xl p-6 w-[360px] text-center">
        <h2 className="text-lg font-semibold mb-4">
          Upload MRI Scan
        </h2>

        <input type="file" onChange={handleFileChange} />

        {preview && (
          <p className="text-xs text-gray-500 mt-2">
            File selected: {file?.name}
          </p>
        )}

        <button
          onClick={handleUpload}
          className="mt-4 bg-blue-600 hover:bg-blue-700 transition text-white px-4 py-2 rounded"
        >
          Analyze Scan
        </button>
      </div>

      {loading && <Loader />}
      {result && <ResultCard result={result} />}
    </div>
  );
}
