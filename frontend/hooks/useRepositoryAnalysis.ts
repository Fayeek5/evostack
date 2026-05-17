"use client";

import { useState } from "react";

export default function useRepositoryAnalysis() {

  const [loading, setLoading] =
    useState(false);

  const [error, setError] =
    useState("");

  const [result, setResult] =
    useState<any>(null);

  const [history, setHistory] =
    useState<any[]>([]);

  const [trends, setTrends] =
    useState<any>(null);

  const [repositories, setRepositories] =
    useState<any[]>([]);

  const analyzeRepository = async (
    repoUrl: string
  ) => {

    try {

      if (!repoUrl.trim()) {

        setError(
          "Please enter a GitHub repository URL"
        );

        return;
      }

      if (!repoUrl.includes("github.com")) {

        setError(
          "Only GitHub repositories are supported"
        );

        return;
      }

      setLoading(true);

      setError("");

      const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/analyze?repo_url=${encodeURIComponent(repoUrl)}`,
        {
          method: "POST"
        }
      );

      const data =
        await response.json();

      setResult(data);

      const historyResponse =
        await fetch(
          `${process.env.NEXT_PUBLIC_API_URL}/history?repo_url=${encodeURIComponent(repoUrl)}`
        );

      const historyData =
        await historyResponse.json();

      setHistory(historyData);

      const trendsResponse =
        await fetch(
          `${process.env.NEXT_PUBLIC_API_URL}/trends?repo_url=${encodeURIComponent(repoUrl)}`
        );

      const trendsData =
        await trendsResponse.json();

      setTrends(trendsData);

      const repositoriesResponse =
        await fetch(
          `${process.env.NEXT_PUBLIC_API_URL}/repositories`
        );

      const repositoriesData =
        await repositoriesResponse.json();

      setRepositories(
        repositoriesData
      );

    } catch (err) {

      setError(
        (err as Error)?.message ||
        "Repository analysis failed"
      );

    } finally {

      setLoading(false);
    }
  };

  return {

    loading,

    error,

    result,

    history,

    trends,

    repositories,

    analyzeRepository
  };
}
