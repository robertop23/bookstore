FROM node:10.18.1

ENV APP_ROOT /frontend

RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}
ADD . ${APP_ROOT}

RUN npm install
RUN npm run build

ENV HOST 0.0.0.0
