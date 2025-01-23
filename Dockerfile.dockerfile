FROM node:4.x as build

WORKDIR ./app/

COPY package.json package-lock.json .

RUN npm install


FROM node:4.x as dev

COPY --from=build ./app/ .

ENTRYPOINT [ "npm", "build" ]



