"use client";
import { useState } from "react";

export default function ImageOverlay({ original, mask }: any) {
  const [opacity, setOpacity] = useState(0.5);

  return (
    <div className="flex flex-col items-center gap-4">
      <div className="relative w-80 h-80 border rounded-lg overflow-hidden shadow">
        <img
          src={`data:image/png;base64,${original}`}
          className="absolute w-full h-full object-cover"
        />

        <img
          src={`data:image/png;base64,${mask}`}
          className="absolute w-full h-full object-cover"
          style={{ opacity }}
        />
      </div>

      <div className="w-full px-4">
        <label className="text-sm text-gray-600">
          Overlay Intensity: {(opacity * 100).toFixed(0)}%
        </label>

        <input
          type="range"
          min="0"
          max="1"
          step="0.05"
          value={opacity}
          onChange={(e) => setOpacity(Number(e.target.value))}
          className="w-full"
        />
      </div>
    </div>
  );
}
