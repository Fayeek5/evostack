"use client";

export default function CICDIntelligence({
  result
}: {
  result: any;
}) {

  const ci =
    result?.analysis?.semantics?.ci_cd;

  if (!ci) return null;

  return (

    <div className="mt-12 rounded-3xl border border-cyan-500/20 bg-black/40 p-8">

      <h2 className="text-3xl font-bold text-white mb-8">
        CI/CD Governance Intelligence
      </h2>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

        <div className="rounded-2xl bg-zinc-950 border border-zinc-800 p-6">
          <div className="text-zinc-400">
            CI Pipeline
          </div>

          <div className="text-2xl font-bold text-white mt-2">
            {ci.ci_detected ? "Detected" : "Missing"}
          </div>
        </div>

        <div className="rounded-2xl bg-zinc-950 border border-zinc-800 p-6">
          <div className="text-zinc-400">
            Deployment Automation
          </div>

          <div className="text-2xl font-bold text-white mt-2">
            {ci.deployment_detected ? "Enabled" : "Missing"}
          </div>
        </div>

        <div className="rounded-2xl bg-zinc-950 border border-zinc-800 p-6">
          <div className="text-zinc-400">
            Lint Enforcement
          </div>

          <div className="text-2xl font-bold text-white mt-2">
            {ci.linting_detected ? "Enabled" : "Missing"}
          </div>
        </div>

        <div className="rounded-2xl bg-zinc-950 border border-zinc-800 p-6">
          <div className="text-zinc-400">
            Testing Pipeline
          </div>

          <div className="text-2xl font-bold text-white mt-2">
            {ci.testing_pipeline_detected ? "Detected" : "Weak"}
          </div>
        </div>

      </div>

    </div>
  );
}
