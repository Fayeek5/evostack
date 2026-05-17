"use client";

export default function HistoryTimeline({ history }: { history: any }) {

  if (!history?.length) return null;

  return (

    <div className="mt-8 rounded-3xl border border-cyan-500/20 bg-black/40 p-8">

      <h2 className="text-3xl font-bold text-white mb-8">
        Repository Evolution Timeline
      </h2>

      <div className="space-y-5">

        {history.map((snapshot: unknown) => (

          <div
            key={snapshot.id}
            className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6 flex flex-col md:flex-row md:items-center md:justify-between gap-4"
          >

            <div>

              <div className="text-xl font-semibold text-white">
                Score: {snapshot.overall_score}
              </div>

              <div className="text-zinc-400 mt-2">
                {snapshot.primary_language}
              </div>

            </div>

            <div className="text-zinc-500 text-sm">
              {snapshot.created_at}
            </div>

          </div>

        ))}

      </div>

    </div>
  );
}
