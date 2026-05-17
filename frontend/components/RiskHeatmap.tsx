"use client";

export default function RiskHeatmap({ result }: { result: any }) {

  const files =
    result?.analysis?.semantics?.top_risky_files || [];

  if (!files.length) return null;

  return (

    <div className="mt-8 rounded-3xl border border-cyan-500/20 bg-black/40 p-8">

      <h2 className="text-3xl font-bold text-white mb-8">
        AI Repository Risk Heatmap
      </h2>

      <div className="space-y-5">

        {files.map(
          (file: unknown, index: number) => {

            const risk =
              Number((file as any).risk_score || 0);

            const width =
              Math.min(risk * 2.5, 100);

            const severity =
              risk >= 25
                ? "HIGH"
                : risk >= 10
                ? "MEDIUM"
                : "LOW";

            const severityColor =
              severity === "HIGH"
                ? "bg-red-500"
                : severity === "MEDIUM"
                ? "bg-yellow-400"
                : "bg-cyan-400";

            return (

              <div
                key={index}
                className="rounded-2xl border border-zinc-800 bg-zinc-950 p-5"
              >

                <div className="flex items-center justify-between mb-3">

                  <div className="text-white font-semibold text-lg break-all">
                    {(file as any).path}
                  </div>

                  <div className={`px-3 py-1 rounded-full text-xs font-bold text-black ${severityColor}`}>
                    {severity}
                  </div>

                </div>

                <div className="w-full h-5 rounded-full bg-zinc-900 overflow-hidden">

                  <div
                    className={`h-full ${severityColor} transition-all duration-700`}
                    style={{
                      width: `${width}%`
                    }}
                  />

                </div>

                <div className="mt-3 flex items-center justify-between text-sm text-zinc-400">

                  <div>
                    Risk Score: {risk}
                  </div>

                  <div>
                    LOC: {(file as any).lines_of_code}
                  </div>

                </div>

              </div>
            );
          }
        )}

      </div>

    </div>
  );
}
