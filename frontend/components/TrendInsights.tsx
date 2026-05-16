"use client";

export default function TrendInsights({
  trends
}: any) {

  if (!trends) return null;

  const trend = trends.trend;

  const trendColor =
    trend === "improving"
      ? "text-green-400"
      : trend === "degrading"
      ? "text-red-400"
      : "text-yellow-300";

  return (

    <div className="mt-8 rounded-3xl border border-cyan-500/20 bg-black/40 p-8">

      <h2 className="text-3xl font-bold text-white mb-8">
        Repository Evolution Intelligence
      </h2>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">

        <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6">

          <div className="text-zinc-400 text-lg">
            Trend Status
          </div>

          <div className={`mt-4 text-3xl font-bold ${trendColor}`}>
            {trends.trend}
          </div>

        </div>

        <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6">

          <div className="text-zinc-400 text-lg">
            Latest Score
          </div>

          <div className="mt-4 text-4xl font-bold text-white">
            {trends.latest_score}
          </div>

        </div>

        <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6">

          <div className="text-zinc-400 text-lg">
            Score Delta
          </div>

          <div className={`mt-4 text-4xl font-bold ${trendColor}`}>
            {trends.score_change > 0 ? "+" : ""}
            {trends.score_change}
          </div>

        </div>

        <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6">

          <div className="text-zinc-400 text-lg">
            Historical Analyses
          </div>

          <div className="mt-4 text-4xl font-bold text-white">
            {trends.analysis_count}
          </div>

        </div>

      </div>

    </div>
  );
}
