"use client";

import { motion } from "framer-motion";

export default function HotspotExplorer({ result }: any) {

  const hotspots =
    result?.analysis?.semantics?.top_risky_files || [];

  const asyncHotspots =
    result?.analysis?.semantics?.async_hotspots || [];

  const dependencyHotspots =
    result?.analysis?.semantics?.dependency_hotspots || [];

  const getRiskColor = (level: string) => {

    if (level === "high") {
      return "border-red-500/30 bg-red-500/10 text-red-200";
    }

    if (level === "medium") {
      return "border-yellow-500/30 bg-yellow-500/10 text-yellow-200";
    }

    return "border-cyan-500/20 bg-cyan-500/5 text-cyan-100";
  };

  return (

    <div className="mt-16">

      <h2 className="text-4xl md:text-5xl font-bold mb-8 text-white">
        Repository Hotspots
      </h2>

      <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">

        <div className="rounded-3xl border border-zinc-800 bg-zinc-950/70 p-8">

          <h3 className="text-2xl font-bold mb-6 text-white">
            Top Risky Files
          </h3>

          <div className="space-y-4">

            {hotspots.map((file: any, index: number) => (

              <motion.div
                key={index}
                whileHover={{ scale: 1.02 }}
                className={`rounded-2xl border p-5 ${getRiskColor(file.risk_level)}`}
              >

                <div className="text-sm opacity-70 mb-2">
                  {file.path}
                </div>

                <div className="flex justify-between items-center">

                  <div className="font-bold">
                    Risk Score
                  </div>

                  <div className="text-2xl font-black">
                    {file.risk_score}
                  </div>

                </div>

              </motion.div>

            ))}

          </div>

        </div>

        <div className="rounded-3xl border border-zinc-800 bg-zinc-950/70 p-8">

          <h3 className="text-2xl font-bold mb-6 text-white">
            Async Hotspots
          </h3>

          <div className="space-y-4">

            {asyncHotspots.map((file: any, index: number) => (

              <div
                key={index}
                className="rounded-2xl border border-cyan-500/20 bg-cyan-500/5 p-5"
              >

                <div className="text-sm opacity-70 mb-2">
                  {file.path}
                </div>

                <div className="flex justify-between">

                  <span>Async Functions</span>

                  <span className="font-bold text-cyan-200">
                    {file.async_functions}
                  </span>

                </div>

              </div>

            ))}

          </div>

        </div>

        <div className="rounded-3xl border border-zinc-800 bg-zinc-950/70 p-8">

          <h3 className="text-2xl font-bold mb-6 text-white">
            Dependency Hotspots
          </h3>

          <div className="space-y-4">

            {dependencyHotspots.map((file: any, index: number) => (

              <div
                key={index}
                className="rounded-2xl border border-cyan-500/20 bg-cyan-500/5 p-5"
              >

                <div className="text-sm opacity-70 mb-2">
                  {file.path}
                </div>

                <div className="flex justify-between">

                  <span>Imports</span>

                  <span className="font-bold text-cyan-200">
                    {file.imports}
                  </span>

                </div>

              </div>

            ))}

          </div>

        </div>

      </div>

    </div>
  );
}
