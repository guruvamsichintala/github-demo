FROM node:23.7 as build

WORKDIR ./app/

COPY package.json package-lock.json .

RUN npm install


FROM node:23.7 as dev

COPY --from=build ./app/ .

ENTRYPOINT [ "npm", "build" ]



