import { NextResponse } from "next/server";
import { getServerSession } from "next-auth/next";
import { authOptions } from "@/auth";

type TestPrintResponse = { status: number } | { error: string };

export async function GET(): Promise<NextResponse<TestPrintResponse>> {
  const session = await getServerSession(authOptions);
  const bearer = session?.idToken;

  if (!bearer) {
    return NextResponse.json({ error: "unauthorized" }, { status: 401 });
  }

  // Compose provides this env var to the frontend container.
  const backendUrl = process.env.BACKEND_URL ?? "http://backend:8000";

  const res = await fetch(`${backendUrl}/api/test_print`, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${bearer}`,
    },
    cache: "no-store",
  });

  return NextResponse.json(
    { status: res.status },
    { status: 200 }
  );
}

