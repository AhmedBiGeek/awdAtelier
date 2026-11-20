const os = require('os');
const { Eureka } = require('eureka-js-client');

function resolveIp() {
  const nets = os.networkInterfaces();
  for (const entries of Object.values(nets)) {
    for (const net of entries || []) {
      if (net.family === 'IPv4' && !net.internal) {
        return net.address;
      }
    }
  }
  return '127.0.0.1';
}

function createEurekaClient(port) {
  const ipAddr = process.env.IP_ADDR || resolveIp();
  const hostName = process.env.HOST_NAME || ipAddr;
  const eurekaHost = process.env.EUREKA_HOST || 'localhost';
  const eurekaPort = Number(process.env.EUREKA_PORT || 8761);

  return new Eureka({
    instance: {
      app: 'MEETING',
      instanceId: `${ipAddr}:meeting:${port}`,
      hostName,
      ipAddr,
      port: {
        $: port,
        '@enabled': true,
      },
      vipAddress: 'MEETING',
      dataCenterInfo: {
        '@class': 'com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo',
        name: 'MyOwn',
      },
      statusPageUrl: `http://${ipAddr}:${port}/info`,
      healthCheckUrl: `http://${ipAddr}:${port}/health`,
      homePageUrl: `http://${ipAddr}:${port}/`,
    },
    eureka: {
      host: eurekaHost,
      port: eurekaPort,
      servicePath: '/eureka/apps/',
      maxRetries: 10,
      requestRetryDelay: 2000,
    },
  });
}

module.exports = { createEurekaClient };
