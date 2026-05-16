"use client";

import { useState } from "react";

export default function Home() {

  const [repoUrl, setRepoUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);
  const [error, setError] = useState("");

  const analyzeRepository = async () => {

    try {

      setLoading(true);
      setError("");
      setResult(null);

      const response = await fetch(
        `https://evostack.onrender.com/analyze?repo_url=${encodeURIComponent(repoUrl)}`,
        {
          method: "POST",
        }
      );

      if (!response.ok) {
        throw new Error("Analysis failed");
      }

      const data = await response.json();

      setResult(data);

    } catch (err: any) {

      setError(err.message || "Failed to fetch");

    } finally {

      setLoading(false);

    }
  };

  return (
    <main className="min-h-screen bg-black text-white px-6 py-16">

      <div className="max-w-6xl mx-auto">

        <h1 className="text-7xl font-bold tracking-tight mb-6">
          EvoStack
        </h1>

        <p className="text-zinc-400 text-xl mb-14">
          AI-native repository governance and semantic engineering intelligence platform.
        </p>

        <div className="flex gap-4 mb-8">

          <input
            value={repoUrl}
            onChange={(e) => setRepoUrl(e.target.value)}
            placeholder="https://github.com/vercel/next.js"
            className="flex-1 rounded-2xl border border-white/10 bg-white/[0.03] px-6 py-5 text-lg outline-none"
          />

          <button
            onClick={analyzeRepository}
            disabled={loading}
            className="rounded-2xl bg-cyan-400 text-black px-10 py-5 text-lg font-semibold hover:scale-105 transition"
          >
            {loading ? "Analyzing..." : "Analyze"}
          </button>

        </div>

        {error && (
          <div className="rounded-2xl border border-red-500/20 bg-red-500/10 p-4 text-red-300 mb-8">
            {error}
          </div>
        )}

        {loading && (
          <div className="mt-10 rounded-3xl border border-white/10 bg-white/[0.03] p-8 backdrop-blur-xl">

            <h2 className="text-3xl font-semibold mb-8">
              EvoStack Intelligence Pipeline
            </h2>

            <div className="space-y-5 text-zinc-300 text-lg">

              <div>Cloning repository...</div>
              <div>Parsing architecture...</div>
              <div>Analyzing complexity...</div>
              <div>Building dependency graph...</div>
              <div>Running semantic analysis...</div>
              <div>Generating engineering insights...</div>

            </div>

          </div>
        )}

        {result && (
          <div className="mt-10 rounded-3xl border border-white/10 bg-white/[0.03] p-8 backdrop-blur-xl">

            <h2 className="text-4xl font-semibold mb-8">
              Repository Intelligence Report
            </h2>

            <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-10">

              <div className="rounded-2xl bg-cyan-500/10 border border-cyan-500/20 p-6">
                <p className="text-sm text-zinc-400 mb-2">Overall Score</p>
                <h3 className="text-5xl font-bold text-cyan-400">
                  {result.health_score.overall}
                </h3>
              </div>

              <div className="rounded-2xl bg-white/[0.03] border border-white/10 p-6">
                <p className="text-sm text-zinc-400 mb-2">Primary Language</p>
                <h3 className="text-2xl font-semibold">
                  {result.analysis.architecture.primary_language}
                </h3>
              </div>

              <div className="rounded-2xl bg-white/[0.03] border border-white/10 p-6">
                <p className="text-sm text-zinc-400 mb-2">Functions</p>
                <h3 className="text-2xl font-semibold">
                  {result.analysis.semantics.functions}
                </h3>
              </div>

              <div className="rounded-2xl bg-white/[0.03] border border-white/10 p-6">
                <p className="text-sm text-zinc-400 mb-2">React Components</p>
                <h3 className="text-2xl font-semibold">
                  {result.analysis.semantics.react_components}
                </h3>
              </div>

            </div>

            <div className="rounded-2xl border border-white/10 bg-black/30 p-6">

              <h3 className="text-2xl font-semibold mb-4">
                Architecture Analysis
              </h3>

              <div className="space-y-3 text-zinc-300">

                <p>
                  Repository Type:
                  <span className="text-white ml-2">
                    {result.analysis.architecture.repository_type}
                  </span>
                </p>

                <p>
                  Maintainability:
                  <span className="text-cyan-400 ml-2">
                    {result.health_score.maintainability_rating}
                  </span>
                </p>

                <p>
                  Async Functions:
                  <span className="text-white ml-2">
                    {result.analysis.semantics.async_functions}
                  </span>
                </p>

              </div>

            </div>

          </div>
        )}

      </div>

    </main>
  );
}
