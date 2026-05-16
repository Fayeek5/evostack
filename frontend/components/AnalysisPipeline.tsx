"use client";

import { motion } from "framer-motion";

const stages = [
  "Cloning repository",
  "Parsing architecture",
  "Extracting dependencies",
  "Running semantic intelligence",
  "Calculating engineering health",
  "Generating AI recommendations",
];

export default function AnalysisPipeline() {

  return (

    <div className="mt-12 rounded-[36px] border border-cyan-500/20 bg-black/40 p-10">

      <h2 className="text-4xl font-bold mb-10 text-white">
        AI Analysis Pipeline
      </h2>

      <div className="space-y-6">

        {stages.map((stage, index) => (

          <motion.div
            key={stage}
            initial={{ opacity: 0, x: -40 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{
              delay: index * 0.3,
            }}
            className="flex items-center gap-5 rounded-2xl border border-cyan-500/20 bg-cyan-500/5 p-5"
          >

            <motion.div
              animate={{
                scale: [1, 1.3, 1],
              }}
              transition={{
                repeat: Infinity,
                duration: 1.5,
              }}
              className="h-4 w-4 rounded-full bg-cyan-400"
            />

            <div className="text-xl text-cyan-100">
              {stage}
            </div>

          </motion.div>

        ))}

      </div>

    </div>

  );
}
