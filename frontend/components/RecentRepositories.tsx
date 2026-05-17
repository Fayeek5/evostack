"use client";

export default function RecentRepositories({
  repositories,
  onSelect
}: {
  repositories: string[];
  onSelect: (repo: string) => void;
}) {

  if (!repositories?.length) return null;

  return (

    <div className="mt-8 rounded-3xl border border-cyan-500/20 bg-black/40 p-8">

      <h2 className="text-3xl font-bold text-white mb-8">
        Recently Analyzed Repositories
      </h2>

      <div className="space-y-4">

        {repositories.map((repo: string) => (

          <button
            key={repo}
            onClick={() => onSelect(repo)}
            className="w-full rounded-2xl border border-zinc-800 bg-zinc-950 p-5 text-left text-zinc-300 hover:border-cyan-500 hover:text-white transition"
          >

            {repo}

          </button>

        ))}

      </div>

    </div>
  );
}
