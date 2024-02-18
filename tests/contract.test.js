const specmatic = require('specmatic');
const { getApp, startAppServer, stopAppServer } = require('./util/app.server.js');
const { GenericContainer, Wait } = require('testcontainers');

const APP_HOST = 'localhost';
const APP_PORT = 3031;

let appServer;
let mongoContainer;

jest.setTimeout(30000);

specmatic.showTestResults(test);

beforeAll(async () => {
  mongoContainer = await new GenericContainer('mongo')
    .withExposedPorts(27017)
    .withWaitStrategy(Wait.forLogMessage("Listening on"))
    .start();
  process.env.BOOKER_DB_URL = `mongodb://${mongoContainer.getHost()}:${mongoContainer.getMappedPort(27017)}`;
  var initializeSeedData = require('../routes/seed.js');
  await initializeSeedData();
  appServer = await startAppServer(APP_PORT);
  await specmatic.testWithApiCoverage(getApp(), APP_HOST, APP_PORT);
});

afterAll(async () => {
  await stopAppServer(appServer);
  await mongoContainer.stop();
});
