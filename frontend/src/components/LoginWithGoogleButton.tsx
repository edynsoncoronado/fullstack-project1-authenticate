"use client";

import { signIn } from "next-auth/react";

export default function LoginWithGoogleButton() {
  return (
    <button
      type="button"
      className="rounded-md bg-blue-600 px-4 py-2 text-sm font-medium text-white hover:bg-blue-700 disabled:opacity-60"
      onClick={() => {
        signIn("google", { callbackUrl: "/dashboard" });
      }}
    >
      Login with Google
    </button>
  );
}