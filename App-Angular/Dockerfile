FROM node:10.0.0

WORKDIR /usr/src/app

COPY package*.json /usr/src/app/
#RUN npm install @angular/cli@7.0.0.0 -g

RUN npm install

COPY . /usr/src/app/


CMD [ "npm", "run", "start" ]
