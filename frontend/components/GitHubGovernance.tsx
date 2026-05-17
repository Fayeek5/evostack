"use client";

export default function GitHubGovernance({ result }: { result: any }) {

  const metadata =
    result?.github_metadata;

  if (!metadata) {
    return null;
  }

  return (

    <div className="w-full rounded-3xl border border-cyan-500/20 bg-black/40 p-8 mt-8">

      <div className="text-cyan-300 text-sm font-semibold tracking-widest uppercase mb-6">
        Repository Governance Intelligence
      </div>

      <div className="grid grid-cols-2 md:grid-cols-3 gap-6">

        <Metric
          label="Stars"
          value={metadata.stars}
        />

        <Metric
          label="Forks"
          value={metadata.forks}
        />

        <Metric
          label="Open Issues"
          value={metadata.open_issues}
        />

        <Metric
          label="Watchers"
          value={metadata.watchers}
        />

        <Metric
          label="Primary Language"
          value={metadata.language}
        />

        <Metric
          label="Last Activity"
          value={
            metadata.updated_at
              ?.split("T")[0]
          }
        />

      </div>

    </div>
  );
}

function Metric({
  label,
  value
}: unknown) {

  return (

    <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-6">

      <div className="text-zinc-400 text-sm">
        {label}
      </div>

      <div className="text-3xl font-bold text-white mt-3">
        {value}
      </div>

    </div>
  );
}
