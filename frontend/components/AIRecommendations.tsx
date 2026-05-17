"use client";

export default function AIRecommendations({ result }: any) {

  const recommendations =
    result?.recommendations || [];

  if (recommendations.length === 0) {

    return null;
  }

  return (

    <div className="w-full rounded-3xl border border-cyan-500/20 bg-black/40 p-8 mt-8">

      <h2 className="text-3xl font-bold text-white mb-6">
        AI Engineering Recommendations
      </h2>

      <div className="space-y-4">

        {recommendations.map(
          (item: any, index: number) => (

            <div
              key={index}
              className="p-5 rounded-2xl border border-cyan-400/20 bg-cyan-500/5 hover:scale-[1.02] transition duration-300"
            >

              <div className="text-xl font-semibold text-white mb-2">
                {item.title}
              </div>

              <div className="text-cyan-100">
                {item.description}
              </div>

            </div>

          )
        )}

      </div>

    </div>
  );
}
