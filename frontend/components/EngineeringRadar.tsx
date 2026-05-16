"use client";

import {
  Radar,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  ResponsiveContainer,
} from "recharts";

export default function EngineeringRadar({ result }: any) {

  const data = [
    {
      subject: "Complexity",
      value: result?.health_score?.complexity_score || 0,
    },
    {
      subject: "Dependencies",
      value: result?.health_score?.dependency_score || 0,
    },
    {
      subject: "Debt",
      value: result?.health_score?.technical_debt_score || 0,
    },
    {
      subject: "Maintainability",
      value: result?.health_score?.overall || 0,
    },
    {
      subject: "Semantics",
      value:
        result?.analysis?.semantics?.functions
          ? 90
          : 40,
    },
  ];

  return (
    <div className="w-full h-[420px] rounded-3xl border border-cyan-500/20 bg-black/40 p-6">

      <h2 className="text-3xl font-bold mb-6 text-white">
        Engineering Intelligence Radar
      </h2>

      <ResponsiveContainer width="100%" height="100%">

        <RadarChart data={data}>

          <PolarGrid stroke="#164e63" />

          <PolarAngleAxis
            dataKey="subject"
            tick={{ fill: "#67e8f9", fontSize: 14 }}
          />

          <PolarRadiusAxis
            angle={30}
            domain={[0, 100]}
            tick={{ fill: "#0ea5e9" }}
          />

          <Radar
            name="Engineering"
            dataKey="value"
            stroke="#22d3ee"
            fill="#06b6d4"
            fillOpacity={0.5}
          />

        </RadarChart>

      </ResponsiveContainer>

    </div>
  );
}
