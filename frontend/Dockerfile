FROM node:20-alpine

WORKDIR /app

EXPOSE 3000

CMD ["sh", "-c", "if [ -f package.json ]; then npm install && npm run dev -- -H 0.0.0.0 -p 3000; else echo 'No package.json found in /app. Add your Next.js app files to ./frontend to start dev server.' && sleep infinity; fi"]
