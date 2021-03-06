var express = require('express');
var path = require('path');

var indexRouter = require('./routes/index');
var news = require('./routes/news');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, '../client/build'));//cross origin for now
app.set('view engine', 'jade');
//app.all() allow cross origin.
app.use('/static', express.static(path.join(__dirname, '../client/build/static')));

app.use('/', indexRouter);
app.use('/news', news);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  res.status(404);
});

module.exports = app;
