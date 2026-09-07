FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN npm install -g dotenv-clustr-mgr
COPY . .
CMD ["dotenv-clustr-mgr", "start", "app.js"]