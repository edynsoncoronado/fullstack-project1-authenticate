import { getServerSession } from "next-auth/next";
import { redirect } from "next/navigation";
import { authOptions } from "@/auth";
import RunTestButton from "@/components/RunTestButton";

export default async function DashboardPage() {
  const session = await getServerSession(authOptions);

  if (!session?.user) {
    redirect("/");
  }

  return (
    <main className="min-h-screen flex items-center justify-center bg-gray-50 p-6">
      <section className="w-full max-w-sm rounded-lg bg-white p-6 shadow-sm">
        <h1 className="text-xl font-semibold text-gray-900">Dashboard</h1>

        <div className="mt-5 space-y-3">
          <div className="flex items-center gap-3">
            {session.user.image ? (
              // Simple <img> for functional UI; can move to `next/image` later.
              <img
                src={session.user.image}
                alt={session.user.name ?? "User"}
                className="h-12 w-12 rounded-full object-cover"
              />
            ) : (
              <div className="h-12 w-12 rounded-full bg-gray-200" />
            )}

            <div>
              <p className="text-sm font-medium text-gray-900">
                {session.user.name ?? "Unknown user"}
              </p>
              <p className="text-sm text-gray-600">{session.user.email}</p>
            </div>
          </div>

          <div className="pt-2">
            <RunTestButton />
          </div>
        </div>
      </section>
    </main>
  );
}

