"use client";

export default function FileIntelligenceTable({ result }: { result: any }) {

  const files =
    result?.analysis?.semantics?.file_metrics || [];

  const sortedFiles = [...files]
    .sort(
      (a, b) => b.risk_score - a.risk_score
    )
    .slice(0, 15);

  const getBadge = (level: string) => {

    if (level === "high") {
      return "bg-red-500/20 text-red-300";
    }

    if (level === "medium") {
      return "bg-yellow-500/20 text-yellow-300";
    }

    return "bg-cyan-500/20 text-cyan-200";
  };

  return (

    <div className="mt-16">

      <h2 className="text-4xl md:text-5xl font-bold mb-8 text-white">
        Repository File Intelligence
      </h2>

      <div className="overflow-x-auto rounded-3xl border border-zinc-800 bg-zinc-950/70">

        <table className="w-full min-w-[900px]">

          <thead>

            <tr className="border-b border-zinc-800 text-zinc-400">

              <th className="text-left p-6">
                File
              </th>

              <th className="text-left p-6">
                Functions
              </th>

              <th className="text-left p-6">
                Imports
              </th>

              <th className="text-left p-6">
                Async
              </th>

              <th className="text-left p-6">
                LOC
              </th>

              <th className="text-left p-6">
                Conditions
              </th>

              <th className="text-left p-6">
                Loops
              </th>

              <th className="text-left p-6">
                Nesting
              </th>

              <th className="text-left p-6">
                Risk
              </th>

            </tr>

          </thead>

          <tbody>

            {sortedFiles.length === 0 ? (

              <tr>

                <td
                  colSpan={9}
                  className="p-10 text-center text-zinc-500"
                >
                  No repository intelligence available
                </td>

              </tr>

            ) : (

              sortedFiles.map((file: unknown, index: number) => (

                <div key={index}>

                <tr
                  key={index}
                  className="border-b border-zinc-900 hover:bg-zinc-900/40 transition"
                >

                  <td className="p-6 text-sm text-zinc-300">
                    {(file as any).path}
                  </td>

                  <td className="p-6">
                    {(file as any).functions}
                  </td>

                  <td className="p-6">
                    {(file as any).imports}
                  </td>

                  <td className="p-6">
                    {(file as any).async_functions}
                  </td>

                  <td className="p-6">
                    {(file as any).lines_of_code}
                  </td>

                  <td className="p-6">
                    {(file as any).conditional_count}
                  </td>

                  <td className="p-6">
                    {(file as any).loop_count}
                  </td>

                  <td className="p-6">
                    {(file as any).nesting_depth}
                  </td>

                  <td className="p-6">

                    <span
                      className={`px-4 py-2 rounded-full text-sm font-bold ${getBadge((file as any).risk_level)}`}
                    >
                      {(file as any).risk_score}
                    </span>

                  </td>

                </tr>

                <tr>

                  <td
                    colSpan={9}
                    className="px-6 pb-6"
                  >

                    <div className="flex flex-wrap gap-2">

                      {((file as any).technical_debt_insights || []).map(
                        (
                          insight: string,
                          insightIndex: number
                        ) => (

                          <div
                            key={insightIndex}
                            className="rounded-full bg-red-500/10 border border-red-500/20 px-3 py-1 text-xs text-red-300"
                          >
                            {insight}
                          </div>

                        )
                      )}

                    </div>

                  </td>

                </tr>

                </div>

              ))

            )}

          </tbody>

        </table>

      </div>

    </div>
  );
}
