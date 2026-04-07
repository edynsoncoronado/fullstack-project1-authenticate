import type { NextAuthOptions } from "next-auth";
import GoogleProvider from "next-auth/providers/google";

export const authOptions: NextAuthOptions = {
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID ?? "",
      clientSecret: process.env.GOOGLE_CLIENT_SECRET ?? "",
    }),
  ],
  session: {
    strategy: "jwt",
  },
  callbacks: {
    async signIn({ account }) {
      if (account?.provider !== "google") {
        return false;
      }
      const idToken = account.id_token;
      if (!idToken) {
        return false;
      }

      const backendUrl = process.env.BACKEND_URL ?? "http://backend:8000";
      const res = await fetch(`${backendUrl}/api/login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        body: JSON.stringify({ id_token: idToken }),
      });

      if (!res.ok) {
        return false;
      }
      return true;
    },
    async jwt({ token, account }) {
      // Google returns `id_token` as a JWT that backend can validate.
      if (account?.id_token) {
        token.idToken = account.id_token;
      }
      return token;
    },
    async session({ session, token }) {
      if (typeof token.idToken === "string") {
        session.idToken = token.idToken;
      }
      return session;
    },
  },
};

