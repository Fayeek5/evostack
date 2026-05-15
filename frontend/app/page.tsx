"use client"

import { useEffect, useState } from "react"

const loadingStages = [
  "Cloning repository...",
  "Parsing architecture...",
  "Analyzing complexity...",
  "Building dependency graph...",
  "Running semantic analysis...",
  "Generating engineering insights..."
]

export default function Home() {
  const [repoUrl, setRepoUrl] = useState("")
  const [loading, setLoading] = useState(false)
  const [loadingStep, setLoadingStep] = useState(0)
  const [result, setResult] = useState<any>(null)
  const [error, setError] = useState("")

  useEffect(() => {
    let interval: any

    if (loading) {
      interval = setInterval(() => {
        setLoadingStep((prev) => {
          if (prev >= loadingStages.length - 1) {
            return prev
          }

          return prev + 1
        })
      }, 1200)
    }

    return () => clearInterval(interval)
  }, [loading])

  const analyzeRepo = async () => {
    if (!repoUrl) return

    setLoading(true)
    setLoadingStep(0)

    setError("")
    setResult(null)

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/analyze?repo_url=${encodeURIComponent(repoUrl)}`,
        {
          method: "POST",
        }
      )

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.detail || "Analysis failed")
      }

      setResult(data)

    } catch (err: any) {
      setError(err.message)
    }

    setLoading(false)
  }

  return (
    <main className="min-h-screen bg-black text-white overflow-hidden">

      <div className="absolute inset-0 bg-[radial-gradient(circle_at_top,rgba(120,119,198,0.18),transparent_40%)]" />

      <div className="relative z-10 max-w-7xl mx-auto px-8 py-16">

        <div className="mb-16">

          <div className="inline-flex items-center gap-3 px-4 py-2 rounded-full border border-zinc-800 bg-zinc-900/60 backdrop-blur mb-6">
            <div className="w-2 h-2 rounded-full bg-green-400 animate-pulse" />

            <span className="text-sm text-zinc-300">
              Autonomous Software Evolution Intelligence
            </span>
          </div>

          <h1 className="text-8xl font-black tracking-tight mb-6">
            EvoStack
          </h1>

          <p className="text-2xl text-zinc-400 max-w-4xl leading-relaxed">
            AI-native repository governance and semantic engineering intelligence platform.
          </p>

        </div>

        <div className="bg-zinc-900/50 backdrop-blur-xl border border-zinc-800 rounded-[32px] p-8 mb-12 shadow-2xl">

          <div className="flex gap-4">

            <input
              value={repoUrl}
              onChange={(e) => setRepoUrl(e.target.value)}
              placeholder="https://github.com/your/repository"
              className="flex-1 bg-black/40 border border-zinc-700 rounded-2xl px-6 py-5 text-lg outline-none focus:border-white transition"
            />

            <button
              onClick={analyzeRepo}
              className="px-8 py-5 rounded-2xl bg-white text-black font-bold hover:scale-105 transition-all duration-200"
            >
              {loading ? "Analyzing..." : "Analyze"}
            </button>

          </div>

        </div>

        {error && (
          <div className="bg-red-500/10 border border-red-500/20 text-red-300 rounded-2xl p-6 mb-8">
            {error}
          </div>
        )}

        {loading && (

          <div className="bg-zinc-900/60 border border-zinc-800 rounded-3xl p-10 mb-10">

            <p className="text-3xl font-bold mb-8">
              EvoStack Intelligence Pipeline
            </p>

            <div className="space-y-5">

              {loadingStages.map((stage, index) => (
                <div
                  key={index}
                  className={`flex items-center gap-4 transition-all duration-500 ${
                    index <= loadingStep
                      ? "opacity-100"
                      : "opacity-30"
                  }`}
                >
                  <div
                    className={`w-3 h-3 rounded-full ${
                      index <= loadingStep
                        ? "bg-green-400"
                        : "bg-zinc-700"
                    }`}
                  />

                  <p className="text-lg">
                    {stage}
                  </p>
                </div>
              ))}

            </div>

          </div>

        )}

        {result && (

          <div className="space-y-10 animate-in fade-in duration-700">

            <div className="grid grid-cols-1 md:grid-cols-4 gap-6">

              <MetricCard
                title="Health Score"
                value={result.health_score?.overall}
              />

              <MetricCard
                title="Maintainability"
                value={result.health_score?.maintainability_rating}
              />

              <MetricCard
                title="High Risk Files"
                value={result.complexity_analysis?.high_risk_count}
              />

              <MetricCard
                title="Modules"
                value={result.dependency_analysis?.total_modules}
              />

            </div>

            <div className="grid md:grid-cols-2 gap-6">

              <InfoCard title="Architecture Analysis">

                <InfoRow
                  label="Repository Type"
                  value={result.architecture_analysis?.repository_type}
                />

                <InfoRow
                  label="Primary Language"
                  value={result.architecture_analysis?.primary_language}
                />

                <InfoRow
                  label="Architecture Style"
                  value={result.architecture_analysis?.architecture_style}
                />

                <InfoRow
                  label="Testing Density"
                  value={result.architecture_analysis?.testing_density}
                />

                <div className="mt-6">

                  <p className="text-zinc-500 mb-3">
                    Frameworks
                  </p>

                  <div className="flex flex-wrap gap-3">

                    {result.architecture_analysis?.frameworks_detected?.map(
                      (framework: string, index: number) => (
                        <div
                          key={index}
                          className="px-4 py-2 rounded-full bg-white text-black font-semibold"
                        >
                          {framework}
                        </div>
                      )
                    )}

                  </div>

                </div>

              </InfoCard>

              <InfoCard title="Semantic Intelligence">

                <InfoRow
                  label="Functions"
                  value={result.semantic_analysis?.functions}
                />

                <InfoRow
                  label="Classes"
                  value={result.semantic_analysis?.classes}
                />

                <InfoRow
                  label="Async Functions"
                  value={result.semantic_analysis?.async_functions}
                />

              </InfoCard>

            </div>

            <div className="grid md:grid-cols-2 gap-6">

              <InfoCard title="Large Function Hotspots">

                <div className="space-y-4">

                  {result.semantic_analysis?.large_functions?.map(
                    (func: any, index: number) => (
                      <div
                        key={index}
                        className="bg-black/40 border border-zinc-800 rounded-2xl p-5"
                      >
                        <p className="font-semibold break-all">
                          {func.name}
                        </p>

                        <p className="text-zinc-500 text-sm mt-2 break-all">
                          {func.file}
                        </p>

                        <p className="text-red-400 mt-3">
                          {func.lines} lines
                        </p>
                      </div>
                    )
                  )}

                </div>

              </InfoCard>

              <InfoCard title="Engineering Recommendations">

                <div className="space-y-4">

                  {result.recommendations?.map(
                    (rec: string, index: number) => (
                      <div
                        key={index}
                        className="bg-black/40 border border-zinc-800 rounded-2xl p-5"
                      >
                        {rec}
                      </div>
                    )
                  )}

                </div>

              </InfoCard>

            </div>

            <div className="grid md:grid-cols-3 gap-6">

              <ScoreCard
                title="Complexity"
                score={result.health_score?.complexity_score}
              />

              <ScoreCard
                title="Dependency"
                score={result.health_score?.dependency_score}
              />

              <ScoreCard
                title="Technical Debt"
                score={result.health_score?.technical_debt_score}
              />

            </div>

          </div>

        )}

      </div>

    </main>
  )
}

function MetricCard({
  title,
  value
}: any) {
  return (
    <div className="bg-zinc-900/60 border border-zinc-800 rounded-3xl p-8">
      <p className="text-zinc-400 mb-4">
        {title}
      </p>

      <h2 className="text-7xl font-black">
        {value}
      </h2>
    </div>
  )
}

function InfoCard({
  title,
  children
}: any) {
  return (
    <div className="bg-zinc-900/60 border border-zinc-800 rounded-3xl p-8">

      <h3 className="text-2xl font-bold mb-8">
        {title}
      </h3>

      {children}

    </div>
  )
}

function InfoRow({
  label,
  value
}: any) {
  return (
    <div className="flex justify-between border-b border-zinc-800 py-4">

      <p className="text-zinc-500">
        {label}
      </p>

      <p className="font-semibold text-right max-w-[60%]">
        {value}
      </p>

    </div>
  )
}

function ScoreCard({
  title,
  score
}: any) {

  return (
    <div className="bg-zinc-900/60 border border-zinc-800 rounded-3xl p-8">

      <div className="flex justify-between mb-5">

        <p className="text-zinc-400">
          {title}
        </p>

        <p className="font-bold">
          {score}
        </p>

      </div>

      <div className="w-full h-4 bg-zinc-800 rounded-full overflow-hidden">

        <div
          className="h-full bg-white transition-all duration-700"
          style={{
            width: `${score}%`
          }}
        />

      </div>

    </div>
  )
}
