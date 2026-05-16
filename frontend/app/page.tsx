"use client";

import { useState } from "react";
import { motion } from "framer-motion";

export default function Home() {

  const [repoUrl, setRepoUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);
  const [error, setError] = useState("");

  const steps = [
    "Cloning repository",
    "Parsing architecture",
    "Analyzing complexity",
    "Building dependency graph",
    "Running semantic analysis",
    "Generating engineering insights",
  ];

  async function analyzeRepo() {

    setLoading(true);
    setError("");
    setResult(null);

    try {

      const response = await fetch(
        `https://evostack-backend.onrender.com/analyze?repo_url=${encodeURIComponent(repoUrl)}`,
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
  }

  return (
    <main className="min-h-screen bg-black text-white px-6 py-12 overflow-hidden">

      <div className="max-w-6xl mx-auto">

        <motion.h1
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-8xl font-bold tracking-tight"
        >
          EvoStack
        </motion.h1>

        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.2 }}
          className="text-gray-400 mt-6 text-2xl"
        >
          AI-native repository governance and semantic engineering intelligence platform.
        </motion.p>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="flex gap-4 mt-16"
        >

          <input
            value={repoUrl}
            onChange={(e) => setRepoUrl(e.target.value)}
            placeholder="https://github.com/vercel/next.js"
            className="flex-1 bg-black border border-zinc-800 rounded-3xl px-8 py-6 text-xl outline-none focus:border-cyan-400 transition"
          />

          <motion.button
            whileHover={{ scale: 1.03 }}
            whileTap={{ scale: 0.97 }}
            onClick={analyzeRepo}
            className="bg-cyan-400 text-black font-semibold px-10 py-6 rounded-3xl text-xl"
          >
            {loading ? "Analyzing..." : "Analyze"}
          </motion.button>

        </motion.div>

        {loading && (

          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="mt-14 border border-zinc-900 rounded-[32px] p-10 bg-zinc-950 relative overflow-hidden"
          >

            <motion.div
              animate={{
                x: ["-100%", "100%"],
              }}
              transition={{
                repeat: Infinity,
                duration: 2,
                ease: "linear",
              }}
              className="absolute inset-0 bg-gradient-to-r from-transparent via-cyan-500/10 to-transparent"
            />

            <h2 className="text-5xl font-bold mb-12">
              EvoStack Intelligence Pipeline
            </h2>

            <div className="space-y-8">

              {steps.map((step, index) => (

                <motion.div
                  key={step}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{
                    opacity: 1,
                    x: 0,
                  }}
                  transition={{
                    delay: index * 0.2,
                  }}
                  className="flex items-center gap-5"
                >

                  <motion.div
                    animate={{
                      scale: [1, 1.4, 1],
                      opacity: [0.5, 1, 0.5],
                    }}
                    transition={{
                      repeat: Infinity,
                      duration: 1.5,
                      delay: index * 0.2,
                    }}
                    className="w-4 h-4 rounded-full bg-cyan-400"
                  />

                  <span className="text-2xl text-zinc-200">
                    {step}...
                  </span>

                </motion.div>

              ))}

            </div>

            <motion.div
              initial={{ width: 0 }}
              animate={{ width: "100%" }}
              transition={{
                duration: 8,
              }}
              className="h-2 bg-cyan-400 rounded-full mt-14"
            />

          </motion.div>

        )}

        {error && (

          <div className="mt-10 border border-red-500/20 bg-red-500/10 text-red-300 rounded-3xl p-6 text-xl">
            {error}
          </div>

        )}

        {result && (

          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            className="mt-14 border border-zinc-900 rounded-[32px] p-10 bg-zinc-950"
          >

            <h2 className="text-6xl font-bold mb-10">
              Repository Intelligence Report
            </h2>

            <div className="grid grid-cols-4 gap-6">

              <div className="bg-cyan-500/10 border border-cyan-500/20 rounded-3xl p-6">
                <div className="text-zinc-400 text-lg">
                  Overall Score
                </div>
                <div className="text-7xl font-bold text-cyan-400 mt-3">
                  {result.health_score.overall}
                </div>
              </div>

              <div className="bg-zinc-950 border border-zinc-800 rounded-3xl p-6">
                <div className="text-zinc-400 text-lg">
                  Primary Language
                </div>
                <div className="text-4xl font-bold mt-6">
                  {result.analysis.architecture.primary_language}
                </div>
              </div>

              <div className="bg-zinc-950 border border-zinc-800 rounded-3xl p-6">
                <div className="text-zinc-400 text-lg">
                  Functions
                </div>
                <div className="text-4xl font-bold mt-6">
                  {result.analysis.semantics.functions}
                </div>
              </div>

              <div className="bg-zinc-950 border border-zinc-800 rounded-3xl p-6">
                <div className="text-zinc-400 text-lg">
                  React Components
                </div>
                <div className="text-4xl font-bold mt-6">
                  {result.analysis.semantics.react_components}
                </div>
              </div>

            </div>

            <div className="mt-10 border border-zinc-900 rounded-3xl p-8">

              <h3 className="text-4xl font-bold mb-8">
                Architecture Analysis
              </h3>

              <div className="space-y-4 text-2xl">

                <div>
                  Repository Type: {" "}
                  <span className="text-zinc-300">
                    {result.analysis.architecture.repository_type}
                  </span>
                </div>

                <div>
                  Maintainability: {" "}
                  <span className="text-cyan-400">
                    {result.health_score.maintainability_rating}
                  </span>
                </div>

                <div>
                  Async Functions: {" "}
                  <span className="text-zinc-300">
                    {result.analysis.semantics.async_functions}
                  </span>
                </div>

              </div>

            </div>

          </motion.div>

        )}

      </div>

    </main>
  );
}
