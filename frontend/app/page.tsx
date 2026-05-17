"use client";

import { useState } from "react";
import { motion } from "framer-motion";

import EngineeringRadar from "../components/EngineeringRadar";
import AnalysisPipeline from "../components/AnalysisPipeline";
import RepositoryInsights from "../components/RepositoryInsights";
import ArchitectureExplorer from "../components/ArchitectureExplorer";
import HotspotExplorer from "../components/HotspotExplorer";
import FileIntelligenceTable from "../components/FileIntelligenceTable";

import TrendInsights from "../components/TrendInsights";
import HistoryTimeline from "../components/HistoryTimeline";
import ScoreHistoryChart from "../components/ScoreHistoryChart";
import RecentRepositories from "../components/RecentRepositories";





import AIRecommendations from "../components/AIRecommendations";

import ExecutiveSummary from "../components/ExecutiveSummary";

import GitHubGovernance from "../components/GitHubGovernance";

export default function Home() {

  const [repoUrl, setRepoUrl] = useState("");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const [loadingStage, setLoadingStage] = useState("");
  const [error, setError] = useState("");

  const [history, setHistory] = useState<any>([]);
  const [trends, setTrends] = useState<any>(null);

  const [repositories, setRepositories] = useState<any>([]);

  const analyzeRepository = async () => {

    try {

      if (!repoUrl.trim()) {

        setError("Please enter a GitHub repository URL");
        return;
      }

      if (!repoUrl.includes("github.com")) {

        setError("Only GitHub repositories are supported");
        return;
      }

      setLoading(true);
      setError("");

      const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/analyze?repo_url=${encodeURIComponent(repoUrl)}`,
        {
          method: "POST",
        }
      );

      const data = await response.json();

      await new Promise((resolve) =>
        setTimeout(resolve, 3500)
      );

      setResult(data);

      const historyResponse = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/history?repo_url=${encodeURIComponent(repoUrl)}`
      );

      const historyData = await historyResponse.json();

      setHistory(historyData);

      const trendsResponse = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/trends?repo_url=${encodeURIComponent(repoUrl)}`
      );

      const trendsData = await trendsResponse.json();

      console.log("TRENDS DATA:", trendsData);

      setTrends(trendsData);

      const repositoriesResponse = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/repositories`
      );

      const repositoriesData = await repositoriesResponse.json();

      setRepositories(repositoriesData);

    } catch (err) {

      setError(
        (err as Error)?.message ||
        "Repository analysis failed"
      );

    } finally {

      setLoading(false);

    }
  };

  return (

    <main className="min-h-screen bg-black text-white p-10">

      <div className="max-w-7xl mx-auto">

        <h1
          onClick={() => window.location.reload()}
          className="text-5xl md:text-7xl xl:text-8xl font-black mb-8 cursor-pointer hover:opacity-80 transition"
        >
          EvoStack
        </h1>

        <p className="text-2xl text-zinc-400 mb-12">
          AI-native repository governance and semantic engineering intelligence platform.
        </p>

        <div className="flex flex-col md:flex-row gap-6">

          <input
            value={repoUrl}
            onChange={(e) => setRepoUrl(e.target.value)}

            onKeyDown={(e) => {

              if (e.key === "Enter") {
                analyzeRepository();
              }

            }}
            placeholder="Enter GitHub repository URL"
            className="flex-1 rounded-3xl border border-zinc-800 bg-zinc-950 p-6 text-2xl outline-none"
          />

          <button
            onClick={analyzeRepository}
            className="rounded-3xl bg-cyan-500 px-10 text-2xl font-bold text-black hover:scale-105 transition"
          >
            Analyze
          </button>

        </div>

        {loading && (

          <AnalysisPipeline />

        )}

        {error && (

          <div className="mt-10 rounded-3xl border border-red-500/20 bg-red-500/10 p-6 text-red-300 text-xl">
            {error}
          </div>

        )}

        {result && (

          <motion.div
            initial={{ opacity: 0, y: 40 }}
            animate={{ opacity: 1, y: 0 }}
            className="mt-16 rounded-[36px] border border-zinc-800 bg-zinc-950/70 p-12"
          >

            <h2 className="text-4xl md:text-5xl xl:text-6xl font-bold mb-12">
              Repository Intelligence Report
            </h2>

            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-8">

              <div className="rounded-[28px] border border-cyan-500/20 bg-cyan-500/10 p-8">
                <div className="text-zinc-400 text-xl">
                  Overall Score
                </div>
                <div className="text-4xl md:text-5xl xl:text-6xl font-bold mt-6">
                  {result?.health_score?.overall ?? 0}
                </div>
              </div>

              <div className="rounded-[28px] border border-zinc-800 bg-zinc-950 p-8">
                <div className="text-zinc-400 text-xl">
                  Primary Language
                </div>
                <div className="text-5xl font-bold mt-6">
                  {result?.analysis?.architecture?.primary_language ?? "Unknown"}
                </div>
              </div>

              <div className="rounded-[28px] border border-zinc-800 bg-zinc-950 p-8">
                <div className="text-zinc-400 text-xl">
                  Functions
                </div>
                <div className="text-4xl md:text-5xl xl:text-6xl font-bold mt-6">
                  {result?.analysis?.semantics?.functions ?? 0}
                </div>
              </div>

              <div className="rounded-[28px] border border-zinc-800 bg-zinc-950 p-8">
                <div className="text-zinc-400 text-xl">
                  React Components
                </div>
                <div className="text-4xl md:text-5xl xl:text-6xl font-bold mt-6">
                  {result?.analysis?.semantics?.react_components ?? 0}
                </div>
              </div>

            </div>

            <div className="mt-16">
              <EngineeringRadar result={result} />
            </div>

            <RepositoryInsights result={result} />

            <ArchitectureExplorer result={result} />

            <HotspotExplorer result={result} />

            <FileIntelligenceTable result={result} />



            <div className="mt-16">
              
            <RecentRepositories
              repositories={repositories}
              onSelect={(repo: string) => setRepoUrl(repo)}
            />

            <TrendInsights trends={trends} />

            <HistoryTimeline history={history} />

            <ScoreHistoryChart history={history} />

            <ExecutiveSummary result={result} />

            <GitHubGovernance result={result} />

            <AIRecommendations result={result} />

            </div>

            <div className="mt-16">
            </div>

          </motion.div>

        )}

      </div>

    </main>
  );
}
// refresh deploy
