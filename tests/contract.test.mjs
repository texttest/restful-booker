import specmatic from 'specmatic';
import { getApp, startAppServer, stopAppServer } from './util/app.server.js';
import { GenericContainer, Wait } from 'testcontainers';

const APP_HOST = 'localhost';
const APP_PORT = 3031;

let mongoContainer = await new GenericContainer('mongo')
  .withExposedPorts(27017)
  .withWaitStrategy(Wait.forLogMessage("Listening on"))
  .start();

process.env.BOOKER_DB_URL = `mongodb://${mongoContainer.getHost()}:${mongoContainer.getMappedPort(27017)}`;

var initializeSeedData = (await import('../routes/seed.js')).default;

console.log(initializeSeedData);

await initializeSeedData();

let appServer = await startAppServer(APP_PORT);
await specmatic.testWithApiCoverage(getApp(), APP_HOST, APP_PORT);

specmatic.showTestResults(test);

await stopAppServer(appServer);
await mongoContainer.stop();
