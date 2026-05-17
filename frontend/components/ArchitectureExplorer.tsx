"use client";

import { motion } from "framer-motion";

export default function ArchitectureExplorer({ result }: { result: any }) {

  const semantics =
    result?.analysis?.semantics || {};

  const architecture = [

    {
      title: "Components Layer",
      value:
        semantics.component_directories || 0,
    },

    {
      title: "Service Layer",
      value:
        semantics.service_directories || 0,
    },

    {
      title: "API Layer",
      value:
        semantics.api_directories || 0,
    },

    {
      title: "Hooks Layer",
      value:
        semantics.hook_directories || 0,
    },

  ];

  return (

    <div className="mt-16">

      <h2 className="text-4xl md:text-5xl font-bold mb-8 text-white">
        Repository Architecture
      </h2>

      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">

        {architecture.map((item, index) => (

          <motion.div
            key={(item as any).title}
            initial={{
              opacity: 0,
              y: 20,
            }}
            animate={{
              opacity: 1,
              y: 0,
            }}
            transition={{
              delay: index * 0.1,
            }}
            whileHover={{
              scale: 1.03,
            }}
            className="rounded-3xl border border-cyan-500/20 bg-black/40 p-8"
          >

            <div className="text-zinc-400 text-lg">
              {(item as any).title}
            </div>

            <div className="text-5xl font-bold mt-4 text-cyan-200">
              {(item as any).value}
            </div>

          </motion.div>

        ))}

      </div>

    </div>

  );
}
