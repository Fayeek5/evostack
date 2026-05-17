"use client";

export default function AIRecommendations({ result }: any) {

  const recommendations =
    Array.isArray(result?.recommendations)
      ? result.recommendations
      : [];

  if (recommendations.length === 0) {
    return null;
  }

  return (

    <div className="w-full rounded-3xl border border-cyan-500/20 bg-black/40 p-8 mt-8">

      <h2 className="text-3xl font-bold text-white mb-6">
        AI Engineering Recommendations
      </h2>

      <div className="space-y-5">

        {recommendations.map(
          (item: any, index: number) => {

            const title =
              item?.title || "Engineering Insight";

            const description =
              item?.description || "";

            const type =
              item?.type || "info";

            const badgeColor =
              type === "warning"
                ? "bg-yellow-500/20 text-yellow-300"
                : type === "success"
                ? "bg-green-500/20 text-green-300"
                : "bg-cyan-500/20 text-cyan-300";

            return (

              <div
                key={index}
                className="p-6 rounded-2xl border border-cyan-400/20 bg-cyan-500/5 hover:scale-[1.01] transition duration-300"
              >

                <div className="flex items-center gap-3 mb-3">

                  <div className={`px-3 py-1 rounded-full text-sm font-semibold ${badgeColor}`}>
                    {type.toUpperCase()}
                  </div>

                  <div className="text-xl font-semibold text-white">
                    {title}
                  </div>

                </div>

                <div className="text-cyan-100 leading-relaxed">
                  {description}
                </div>

              </div>
            );
          }
        )}

      </div>

    </div>
  );
}
