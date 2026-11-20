# meeting microservice

Node.js / Express microservice, **no database**, documented with Swagger (OpenAPI 3).
It exposes one endpoint for now; the meeting logic is a TODO for students (see [TODO.md](TODO.md)).

## Run
```bash
npm install
npm start          # or: npm run dev  (auto-restart on changes)
```
Requires Eureka on http://localhost:8761.
- API: http://localhost:8083/api/meetings/hello
- Health: http://localhost:8083/health
- Info: http://localhost:8083/info
- Swagger UI: http://localhost:8083/swagger-ui
- OpenAPI JSON: http://localhost:8083/v3/api-docs

Port: `8083` by default. Change with `PORT=9000 npm start` (registers another Eureka instance).

## Endpoint
| Method | Path | Response |
|---|---|---|
| GET | /api/meetings/hello | `200 {"message": "hello I'm microservice meeting"}` |
| GET | /health | `200 {"status":"UP"}` |
| GET | /info | `200` name + version from package.json |

## Tests
```bash
npm test
```
Uses Node's built-in test runner (`node:test`), Node 18+.

## Structure
```
meeting/
├── src/
│   ├── server.js                      starts the HTTP server
│   ├── app.js                         Express app: JSON, Swagger, routes, 404, errors
│   ├── config/swagger.js              OpenAPI spec (document new routes here)
│   ├── routes/meeting.routes.js       URL -> controller mapping
│   └── controllers/meeting.controller.js   request handling (hello + TODO)
├── test/hello.test.js
├── TODO.md                            work for students
└── package.json
```
