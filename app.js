var express = require('express');
var path = require('path');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var xmlparser = require('express-xml-bodyparser');

const OpenApiValidator = require('express-openapi-validator');

var routes = require('./routes/index');

const swaggerUi = require('swagger-ui-express');
const swaggerDocument = require('./swagger.json');

var app = express();

let options = {};
const capturemock = process.env.CAPTUREMOCK_SERVER;
if (capturemock) {
    const requestInterceptorStr = "(req) => { req.url = req.url.replace(/http:..(127.0.0.1|localhost):[0-9]+/, '" + capturemock + "'); return req; }";
    options["swaggerOptions"] = {
        requestInterceptor: eval(requestInterceptorStr)
    };
}
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument, options));

app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(xmlparser({trim: false, explicitArray: false}));

app.use( OpenApiValidator.middleware({
    apiSpec: "./oas.yaml",
    validateRequests: true,
    validateResponses: true
}));


app.use('/', routes);

// catch 404 and forward to error handler
app.use(function (req, res, next) {
    var err = new Error('Not Found');
    err.status = 404;
    next(err);
});

// error handlers

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
    app.use(function (err, req, res, next) {
        console.log(err);
        console.error(err.stack)
        res.sendStatus(err.status || 500);
    });
}

// production error handler
// no stacktraces leaked to user
app.use(function (err, req, res, next) {
    console.error(err.stack)
    res.sendStatus(err.status || 500);
});


module.exports = app;
