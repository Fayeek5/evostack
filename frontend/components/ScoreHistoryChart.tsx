"use client";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid
} from "recharts";

export default function ScoreHistoryChart({
  history
}: any) {

  if (!history?.length) return null;

  const data = [...history]
    .reverse()
    .map((item: any, index: number) => ({

      run: index + 1,

      score: item.overall_score
    }));

  return (

    <div className="mt-8 rounded-3xl border border-cyan-500/20 bg-black/40 p-8">

      <h2 className="text-3xl font-bold text-white mb-8">
        Engineering Score Evolution
      </h2>

      <div className="h-[320px] w-full">

        <ResponsiveContainer width="100%" height="100%">

          <LineChart data={data}>

            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="run" />

            <YAxis domain={[0, 100]} />

            <Tooltip />

            <Line
              type="monotone"
              dataKey="score"
              stroke="#06b6d4"
              strokeWidth={4}
            />

          </LineChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}
