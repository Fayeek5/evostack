"use client";

export default function RepositoryInsights({ result }: any) {

  const semantics =
    result?.analysis?.semantics || {};

  const frameworks =
    semantics.frameworks || [];

  const insights = [

    {
      title: "Framework Stack",
      value:
        frameworks.length > 0
          ? frameworks.join(" + ")
          : "Unknown"
    },

    {
      title: "Dependency Density",
      value:
        semantics.dependency_density > 8
          ? "High"
          : semantics.dependency_density > 4
          ? "Medium"
          : "Low"
    },

    {
      title: "API Surface",
      value:
        `${semantics.api_routes || 0} Routes`
    },

    {
      title: "Testing Maturity",
      value:
        semantics.test_files > 20
          ? "Strong"
          : semantics.test_files > 5
          ? "Moderate"
          : "Weak"
    },

    {
      title: "Async Complexity",
      value:
        semantics.async_functions > 50
          ? "Elevated"
          : "Normal"
    },

    {
      title: "Architecture Pattern",
      value:
        semantics.scanned_files > 200
          ? "Large Monolith"
          : "Modular Repository"
    }

  ];

  return (

    <div className="mt-16">

      <h2 className="text-5xl font-bold mb-8 text-white">
        Repository Intelligence
      </h2>

      <div className="grid grid-cols-3 gap-6">

        {insights.map((item) => (

          <div
            key={item.title}
            className="rounded-3xl border border-cyan-500/20 bg-black/40 p-8 hover:scale-[1.02] transition"
          >

            <div className="text-zinc-400 text-lg">
              {item.title}
            </div>

            <div className="text-3xl font-bold mt-4 text-cyan-200">
              {item.value}
            </div>

          </div>

        ))}

      </div>

    </div>
  );
}
