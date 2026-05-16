"use client"

import { useState } from "react"
import { motion } from "framer-motion"
import {
  Sparkles,
  Brain,
  Activity,
  GitBranch,
  ShieldCheck,
} from "lucide-react"

export default function Home() {

  const [repoUrl, setRepoUrl] = useState("")
  const [loading, setLoading] = useState(false)
  const [loadingStep, setLoadingStep] = useState(0)
  const [result, setResult] = useState<any>(null)
  const [error, setError] = useState("")

  const loadingStages = [
    {
      icon: GitBranch,
      label: "Cloning repository",
    },
    {
      icon: Brain,
      label: "Parsing architecture",
    },
    {
      icon: Activity,
      label: "Analyzing complexity",
    },
    {
      icon: Sparkles,
      label: "Building semantic intelligence",
    },
    {
      icon: ShieldCheck,
      label: "Generating engineering insights",
    },
  ]

  async function analyzeRepository() {

    if (!repoUrl) return

    setLoading(true)
    setLoadingStep(0)
    setError("")
    setResult(null)

    let stage = 0

    const interval = setInterval(() => {

      stage++

      if (stage < loadingStages.length) {
        setLoadingStep(stage)
      }

    }, 1800)

    try {

      const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/analyze?repo_url=${encodeURIComponent(repoUrl)}`,
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

    } finally {

      clearInterval(interval)
      setLoading(false)

    }
  }

  return (
    <motion.main
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.8 }}
      className="min-h-screen bg-black text-white px-6 py-10"
    >

      <div className="mx-auto max-w-5xl">

        <div className="mb-10">
          <h1 className="text-5xl font-bold tracking-tight">
            EvoStack
          </h1>

          <p className="mt-4 text-zinc-400 max-w-2xl">
            AI-native repository governance and semantic engineering intelligence platform.
          </p>
        </div>

        <div className="flex gap-4">

          <input
            value={repoUrl}
            onChange={(e) => setRepoUrl(e.target.value)}
            placeholder="https://github.com/vercel/next.js"
            className="flex-1 rounded-2xl border border-white/10 bg-white/5 px-5 py-4 outline-none"
          />

          <button
            onClick={analyzeRepository}
            className="rounded-2xl bg-cyan-500 px-6 py-4 font-medium text-black"
          >
            Analyze
          </button>

        </div>

        {loading && (

          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="mt-10 rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-xl"
          >

            <div className="mb-6 flex items-center gap-3">

              <Sparkles className="h-5 w-5 text-cyan-400" />

              <h3 className="text-lg font-medium text-white">
                EvoStack Intelligence Pipeline
              </h3>

            </div>

            <div className="space-y-4">

              {loadingStages.map((stage, index) => {

                const Icon = stage.icon

                return (

                  <motion.div
                    key={stage.label}
                    initial={{ opacity: 0.3 }}
                    animate={{
                      opacity: index <= loadingStep ? 1 : 0.3,
                      x: index === loadingStep ? 6 : 0,
                    }}
                    transition={{ duration: 0.4 }}
                    className="flex items-center gap-3"
                  >

                    <div
                      className={`rounded-xl p-2 ${
                        index <= loadingStep
                          ? "bg-cyan-500/20"
                          : "bg-white/5"
                      }`}
                    >

                      <Icon className="h-4 w-4 text-cyan-300" />

                    </div>

                    <span className="text-sm text-zinc-300">
                      {stage.label}
                    </span>

                  </motion.div>

                )

              })}

            </div>

          </motion.div>

        )}

        {error && (

          <div className="mt-6 rounded-2xl border border-red-500/20 bg-red-500/10 p-4 text-red-300">
            {error}
          </div>

        )}

        {result && (

          <div className="mt-10 rounded-3xl border border-white/10 bg-white/5 p-8">

            <h2 className="text-2xl font-semibold">
              Analysis Complete
            </h2>

            <pre className="mt-6 overflow-auto text-sm text-zinc-300">
              {JSON.stringify(result, null, 2)}
            </pre>

          </div>

        )}

      </div>

    </motion.main>
  )
}
