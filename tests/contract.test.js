const specmatic = require('specmatic');
const { getApp, startAppServer, stopAppServer } = require('./util/app.server.js');
const initializeSeedData = require('../routes/seed.js');

const APP_HOST = 'localhost';
const APP_PORT = 3031;

let appServer;

test('true is true', () => {
  expect(true).toBe(true);
});

beforeAll(async () => {
  await initializeSeedData();
  appServer = await startAppServer(APP_PORT);
  await specmatic.testWithApiCoverage(getApp(), APP_HOST, APP_PORT);
});

afterAll(async () => {
  await stopAppServer(appServer);
});
