### STAGE 1: Build ###
FROM node:12.7-alpine AS build
WORKDIR /usr/src/app
COPY package.json /usr/src/app
RUN npm install
COPY ./ /usr/src/app
RUN npm run build

### STAGE 2: Run ###
FROM nginx:1.17.1-alpine
RUN rm -rf /usr/share/nginx/html/*
COPY nginx.conf /etc/nginx/conf.d/nginx.conf
COPY --from=build /usr/src/app /usr/share/nginx/html   