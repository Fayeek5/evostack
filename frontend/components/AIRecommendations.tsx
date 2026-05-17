"use client";

export default function AIRecommendations({ result }: { result: any }) {

  const recommendations =
    result?.recommendations || [];

  if (!recommendations.length) return null;

  return (

    <div className="mt-12 rounded-3xl border border-cyan-500/20 bg-black/40 p-8">

      <h2 className="text-3xl font-bold text-white mb-8">
        AI Engineering Recommendations
      </h2>

      <div className="space-y-6">

        {recommendations.map((item: any, index: number) => (

          <div
            key={index}
            className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6"
          >

            <div className="text-lg font-semibold text-cyan-400">
              {item.title}
            </div>

            <div className="text-zinc-400 mt-2">
              {item.description}
            </div>

          </div>

        ))}

      </div>

    </div>
  );
}
