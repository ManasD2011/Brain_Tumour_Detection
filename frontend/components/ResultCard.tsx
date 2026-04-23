"use client";
import { motion } from "framer-motion";
import ImageOverlay from "./ImageOverlay";

export default function ResultCard({ result }: any) {
  const severity =
    result.tumor_percentage < 5
      ? "Low"
      : result.tumor_percentage < 15
      ? "Moderate"
      : "High";

  return (
    <motion.div
      initial={{ opacity: 0, y: 30 }}
      animate={{ opacity: 1, y: 0 }}
      className="bg-white shadow-xl rounded-xl p-6 mt-6 w-[420px]"
    >
      <h2 className="text-xl font-semibold mb-4 text-center">
        MRI Analysis Report
      </h2>

      <div className="flex justify-between mb-4 text-sm">
        <span className="text-gray-500">Tumor Coverage</span>
        <span className="font-semibold text-blue-600">
          {result.tumor_percentage.toFixed(2)}%
        </span>
      </div>

      <div className="flex justify-between mb-4 text-sm">
        <span className="text-gray-500">Severity</span>
        <span className="font-semibold">{severity}</span>
      </div>

      <div className="flex justify-center mt-4">
        <ImageOverlay
          original={result.original}
          mask={result.mask}
        />
      </div>
    </motion.div>
  );
}
