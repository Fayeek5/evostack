"use client";

export default function AIRecommendations({ result }: any) {

  const recommendations = [];

  if ((result?.analysis?.complexity?.high_risk_count || 0) > 10) {
    recommendations.push(
      "High-risk files detected. Refactor large modules into smaller services."
    );
  }

  if ((result?.analysis?.dependencies?.total_modules || 0) > 100) {
    recommendations.push(
      "Repository has heavy dependency usage. Consider dependency optimization."
    );
  }

  if ((result?.analysis?.semantics?.async_functions || 0) > 50) {
    recommendations.push(
      "Large async workload detected. Monitor concurrency and promise handling."
    );
  }

  if (recommendations.length === 0) {
    recommendations.push(
      "Repository architecture looks healthy and maintainable."
    );
  }

  return (
    <div className="w-full rounded-3xl border border-cyan-500/20 bg-black/40 p-8 mt-8">

      <h2 className="text-3xl font-bold text-white mb-6">
        AI Engineering Recommendations
      </h2>

      <div className="space-y-4">

        {recommendations.map((item, index) => (

          <div
            key={index}
            className="p-5 rounded-2xl border border-cyan-400/20 bg-cyan-500/5 text-cyan-100 hover:scale-[1.01] transition"
          >
            ⚡ {item}
          </div>

        ))}

      </div>

    </div>
  );
}
