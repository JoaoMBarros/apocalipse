FROM node:lts-alpine

ARG PROJECT_DIR=/apocalipse

RUN mkdir -p ${PROJECT_DIR}
COPY ./apocalipse_vue ${PROJECT_DIR}

WORKDIR ${PROJECT_DIR}

RUN npm install -g npm

COPY ./apocalipse_vue/package.json ${PROJECT_DIR}
COPY ./apocalipse_vue/package-lock.json ${PROJECT_DIR}

RUN npm install

CMD ["npm", "run", "serve"]