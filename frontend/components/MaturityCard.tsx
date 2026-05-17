"use client";

export default function MaturityCard({
  result
}: any) {

  const maturity =
    result?.health_score?.maturity;

  if (!maturity) return null;

  const grade =
    maturity.grade;

  const label =
    maturity.label;

  const gradeColor =
    grade === "A+"
      ? "text-green-400"
      : grade === "A"
      ? "text-cyan-400"
      : grade === "B"
      ? "text-yellow-300"
      : "text-red-400";

  return (

    <div className="mt-8 rounded-3xl border border-cyan-500/20 bg-black/40 p-8">

      <h2 className="text-3xl font-bold text-white mb-8">
        Engineering Maturity Intelligence
      </h2>

      <div className="flex flex-col items-center justify-center rounded-3xl border border-zinc-800 bg-zinc-950 p-10">

        <div className={`text-8xl font-black ${gradeColor}`}>
          {grade}
        </div>

        <div className="mt-4 text-2xl font-semibold text-white">
          {label}
        </div>

        <div className="mt-6 text-center text-zinc-400 max-w-2xl leading-relaxed">
          EvoStack AI has evaluated this repository's
          engineering maturity based on architecture,
          maintainability, dependency health, testing
          maturity, and orchestration complexity.
        </div>

      </div>

    </div>
  );
}
