const app = require('./app');
const { createEurekaClient } = require('./eureka');

const PORT = Number(process.env.PORT || 8083);
const eurekaClient = createEurekaClient(PORT);

const server = app.listen(PORT, () => {
  console.log(`meeting microservice running on http://localhost:${PORT}`);
  console.log(`Swagger UI: http://localhost:${PORT}/swagger-ui`);
  console.log(`Health: http://localhost:${PORT}/health`);
  console.log(`Info: http://localhost:${PORT}/info`);

  eurekaClient.start((error) => {
    if (error) {
      console.error('Failed to register MEETING with Eureka:', error.message || error);
      return;
    }
    console.log(`MEETING registered with Eureka on port ${PORT}`);
  });
});

function shutdown() {
  eurekaClient.stop();
  server.close(() => process.exit(0));
}

process.on('SIGINT', shutdown);
process.on('SIGTERM', shutdown);
