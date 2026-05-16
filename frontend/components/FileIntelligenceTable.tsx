"use client";

export default function FileIntelligenceTable({ result }: any) {

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
                Risk
              </th>

            </tr>

          </thead>

          <tbody>

            {sortedFiles.length === 0 ? (

              <tr>

                <td
                  colSpan={6}
                  className="p-10 text-center text-zinc-500"
                >
                  No repository intelligence available
                </td>

              </tr>

            ) : (

              sortedFiles.map((file: any, index: number) => (

                <tr
                  key={index}
                  className="border-b border-zinc-900 hover:bg-zinc-900/40 transition"
                >

                  <td className="p-6 text-sm text-zinc-300">
                    {file.path}
                  </td>

                  <td className="p-6">
                    {file.functions}
                  </td>

                  <td className="p-6">
                    {file.imports}
                  </td>

                  <td className="p-6">
                    {file.async_functions}
                  </td>

                  <td className="p-6">
                    {file.lines_of_code}
                  </td>

                  <td className="p-6">

                    <span
                      className={`px-4 py-2 rounded-full text-sm font-bold ${getBadge(file.risk_level)}`}
                    >
                      {file.risk_score}
                    </span>

                  </td>

                </tr>

              ))

            )}

          </tbody>

        </table>

      </div>

    </div>
  );
}
