FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN npm install -g pm2-cluster-manager
COPY . .
CMD ["pm2-cluster-manager", "start", "app.js"]