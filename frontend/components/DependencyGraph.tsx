"use client";

import dynamic from "next/dynamic";

const ForceGraph2D = dynamic(
  () => import("react-force-graph").then((mod) => mod.ForceGraph2D),
  {
    ssr: false,
  }
);

export default function DependencyGraph({ result }: any) {

  const graphData = {
    nodes: [
      { id: "Frontend", group: 1 },
      { id: "Backend API", group: 2 },
      { id: "Semantic Engine", group: 3 },
      { id: "Health Engine", group: 4 },
      { id: "AI Recommendation", group: 5 },
      { id: "Repository Parser", group: 6 },
    ],

    links: [
      { source: "Frontend", target: "Backend API" },
      { source: "Backend API", target: "Semantic Engine" },
      { source: "Backend API", target: "Health Engine" },
      { source: "Backend API", target: "AI Recommendation" },
      { source: "Backend API", target: "Repository Parser" },
    ],
  };

  return (
    <div className="mt-16 rounded-[36px] border border-cyan-500/20 bg-black/40 p-8">

      <h2 className="text-5xl font-bold mb-8 text-white">
        Dependency Intelligence Graph
      </h2>

      <div className="h-[700px] rounded-3xl overflow-hidden">

        <ForceGraph2D
          graphData={graphData}
          nodeLabel="id"
          nodeAutoColorBy="group"
          linkDirectionalParticles={2}
          linkDirectionalParticleSpeed={0.004}
          backgroundColor="#020617"
        />

      </div>

    </div>
  );
}
