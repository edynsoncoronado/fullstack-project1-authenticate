FROM node:22-bookworm-slim

WORKDIR /app

ENV NEXT_TELEMETRY_DISABLED=1 \
    NODE_ENV=development

COPY package.json package-lock.json* ./
RUN npm install

EXPOSE 3000

CMD ["npm", "run", "dev", "--", "--hostname", "0.0.0.0", "--port", "3000"]
