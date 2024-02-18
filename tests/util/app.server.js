const http = require('http')
let app, initializeSeedData

function startAppServer(port) {
    return new Promise((resolve, _reject) => {
        app = require('../../app.js')
        const server = http.createServer(app)
        server.listen(port)
        server.on('listening', async () => {
            resolve(server)
        })
    })
}

function stopAppServer(appServer) {
    return new Promise((resolve, reject) => {
        appServer.close(err => {
            if (err) {
                console.error(`Stopping app failed with ${err}`)
                reject()
            } else {
                resolve()
            }
        })
    })
}

function getApp() {
    return app
}

module.exports = { getApp, startAppServer, stopAppServer }