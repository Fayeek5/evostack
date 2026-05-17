"use client";

export default function ExecutiveSummary({ result }: { result: any }) {

  const summary =
    result?.executive_summary;

  if (!summary) {
    return null;
  }

  return (

    <div className="w-full rounded-3xl border border-cyan-500/20 bg-black/40 p-8 mt-8">

      <div className="text-cyan-300 text-sm font-semibold tracking-widest uppercase mb-4">
        AI Executive Summary
      </div>

      <div className="text-2xl leading-relaxed text-white">
        {summary}
      </div>

    </div>
  );
}
