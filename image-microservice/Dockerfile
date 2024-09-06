 FROM node:18

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

ENV APP_PORT=3001

EXPOSE 3001

CMD ["node", "index.js"]