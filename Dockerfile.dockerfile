FROM node:23.9 as build

WORKDIR ./app/

COPY package.json package-lock.json .

RUN npm install


FROM node:23.9 as dev

COPY --from=build ./app/ .

ENTRYPOINT [ "npm", "build" ]



