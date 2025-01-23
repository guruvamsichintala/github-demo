FROM node:23.6 as build

WORKDIR ./app/

COPY package.json package-lock.json .

RUN npm install


FROM node:23.6 as dev

COPY --from=build ./app/ .

ENTRYPOINT [ "npm", "build" ]



