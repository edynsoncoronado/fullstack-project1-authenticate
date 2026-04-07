import LoginWithGoogleButton from "@/components/LoginWithGoogleButton";
export default function HomePage() {
  return (
    <main className="min-h-screen flex items-center justify-center bg-gray-50 p-6">
      <section className="w-full max-w-sm rounded-lg bg-white p-6 shadow-sm">
        <h1 className="text-center text-2xl font-semibold text-gray-900">
          EdyN Notes
        </h1>
        <div className="mt-6 flex justify-center">
          <LoginWithGoogleButton />
        </div>
      </section>
    </main>
  );
}