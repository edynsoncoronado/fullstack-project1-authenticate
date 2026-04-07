"use client";

import { useState } from "react";

type TestResponse = { status?: number; error?: string };

export default function RunTestButton() {
  const [loading, setLoading] = useState(false);
  const [responseStatus, setResponseStatus] = useState<string | null>(null);

  async function onRunTest() {
    setLoading(true);
    setResponseStatus(null);

    try {
      const res = await fetch("/api/test_print", {
        method: "GET",
        headers: { Accept: "application/json" },
      });

      const data = (await res.json().catch(() => null)) as TestResponse | null;

      if (data?.status != null) {
        setResponseStatus(String(data.status));
      } else {
        setResponseStatus(`Error ${res.status}`);
      }
    } catch {
      setResponseStatus("Network error");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="space-y-3">
      <button
        type="button"
        className="rounded-md bg-slate-900 px-4 py-2 text-sm font-medium text-white hover:bg-slate-800 disabled:opacity-60"
        onClick={onRunTest}
        disabled={loading}
      >
        {loading ? "Running..." : "Run Test"}
      </button>

      {responseStatus != null ? (
        <p className="text-sm text-gray-700">
          Response status: <span className="font-medium">{responseStatus}</span>
        </p>
      ) : null}
    </div>
  );
}

