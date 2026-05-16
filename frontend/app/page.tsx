"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import EngineeringRadar from "../components/EngineeringRadar";

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
  }

  return (

    <main className="relative min-h-screen bg-black text-white overflow-hidden">

      <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(0,255,255,0.08),transparent_60%)]" />

      <motion.div
        animate={{
          backgroundPosition: ["0% 0%", "100% 100%"],
        }}
        transition={{
          repeat: Infinity,
          duration: 20,
          ease: "linear",
        }}
        className="absolute inset-0 opacity-20 bg-[linear-gradient(to_right,#111_1px,transparent_1px),linear-gradient(to_bottom,#111_1px,transparent_1px)] bg-[size:60px_60px]"
      />

      <div className="relative z-10 max-w-7xl mx-auto px-8 py-16">

        <motion.div
          initial={{ opacity: 0, y: -40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7 }}
        >

          <motion.h1
            whileHover={{
              scale: 1.02,
              textShadow: "0px 0px 40px rgba(34,211,238,0.8)",
            }}
            className="text-[120px] font-black tracking-[-6px] leading-none"
          >
            EvoStack
          </motion.h1>

          <p className="text-zinc-400 text-2xl mt-6 max-w-4xl leading-relaxed">
            AI-native repository governance and semantic engineering intelligence platform.
          </p>

        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="flex gap-6 mt-20"
        >

          <motion.input
            value={repoUrl}
            onChange={(e) => setRepoUrl(e.target.value)}
            placeholder="https://github.com/vercel/next.js"
            className="flex-1 bg-zinc-950/70 backdrop-blur-xl border border-zinc-800 rounded-[28px] px-8 py-7 text-2xl outline-none transition"
          />

          <motion.button
            whileHover={{
              scale: 1.05,
              boxShadow: "0px 0px 50px rgba(34,211,238,0.4)",
            }}
            whileTap={{ scale: 0.96 }}
            onClick={analyzeRepo}
            className="bg-cyan-400 text-black font-bold px-12 py-7 rounded-[28px] text-2xl"
          >
            {loading ? "Analyzing..." : "Analyze"}
          </motion.button>

        </motion.div>

        {loading && (

          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            className="relative mt-16 overflow-hidden rounded-[36px] border border-cyan-500/10 bg-zinc-950/70 backdrop-blur-2xl p-12"
          >

            <motion.div
              animate={{
                x: ["-100%", "100%"],
              }}
              transition={{
                repeat: Infinity,
                duration: 3,
                ease: "linear",
              }}
              className="absolute inset-0 bg-gradient-to-r from-transparent via-cyan-400/10 to-transparent"
            />

            <h2 className="text-6xl font-bold mb-14">
              EvoStack Intelligence Pipeline
            </h2>

            <div className="space-y-8">

              {steps.map((step, index) => (

                <motion.div
                  key={step}
                  initial={{ opacity: 0, x: -40 }}
                  animate={{
                    opacity: 1,
                    x: 0,
                  }}
                  transition={{
                    delay: index * 0.2,
                  }}
                  whileHover={{
                    x: 12,
                    scale: 1.01,
                  }}
                  className="flex items-center gap-6 bg-zinc-900/40 border border-zinc-800 rounded-2xl px-6 py-5"
                >

                  <motion.div
                    animate={{
                      scale: [1, 1.8, 1],
                      opacity: [0.4, 1, 0.4],
                    }}
                    transition={{
                      repeat: Infinity,
                      duration: 1.4,
                      delay: index * 0.2,
                    }}
                    className="w-4 h-4 rounded-full bg-cyan-400"
                  />

                  <span className="text-2xl text-zinc-100">
                    {step}...
                  </span>

                </motion.div>

              ))}

            </div>

            <div className="mt-14 h-3 bg-zinc-900 rounded-full overflow-hidden">

              <motion.div
                animate={{
                  x: ["-100%", "100%"],
                }}
                transition={{
                  repeat: Infinity,
                  duration: 2,
                  ease: "linear",
                }}
                className="h-full w-1/2 bg-cyan-400 rounded-full"
              />

            </div>

          </motion.div>

        )}

        {error && (

          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="mt-10 rounded-3xl border border-red-500/20 bg-red-500/10 p-6 text-red-300 text-xl"
          >
            {error}
          </motion.div>

        )}

        {result && (

          <motion.div
            initial={{ opacity: 0, y: 40 }}
            animate={{ opacity: 1, y: 0 }}
            className="mt-16 rounded-[36px] border border-zinc-800 bg-zinc-950/70 backdrop-blur-2xl p-12"
          >

            <h2 className="text-7xl font-bold mb-14">
              Repository Intelligence Report
            </h2>

            <div className="grid grid-cols-4 gap-8">

              {[
                {
                  label: "Overall Score",
                  value: result?.health_score?.overall ?? 0,
                  highlight: true,
                },
                {
                  label: "Primary Language",
                  value: result?.analysis?.architecture.primary_language,
                },
                {
                  label: "Functions",
                  value: result?.analysis?.semantics.functions,
                },
                {
                  label: "React Components",
                  value: result?.analysis?.semantics.react_components,
                },
              ].map((card) => (

                <motion.div
                  key={card.label}
                  whileHover={{
                    y: -8,
                    scale: 1.03,
                    boxShadow: "0px 0px 40px rgba(34,211,238,0.15)",
                  }}
                  className={`rounded-[28px] border p-8 transition ${
                    card.highlight
                      ? "border-cyan-500/20 bg-cyan-500/10"
                      : "border-zinc-800 bg-zinc-950"
                  }`}
                >

                  <div className="text-zinc-400 text-xl">
                    {card.label}
                  </div>

                  <div className="text-6xl font-bold mt-6">
                    {card.value}
                  </div>

                </motion.div>

              ))}

            </div>

          </motion.div>

        )}

      </div>

    
{result && <EngineeringRadar result={result} />}
</main>

  );
}
// redeploy
