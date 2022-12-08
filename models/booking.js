// original version used the in-memory database "nedb"
//var Datastore = require('nedb');
//var booking = new Datastore();

const { MongoClient } = require("mongodb");
const uri = process.env.BOOKER_DB_URL || "mongodb://127.0.0.1:27017";
const client = new MongoClient(uri);
const database = client.db('booker');
var booking = database.collection('bookings');

exports.getIDs = function(query, callback){
  booking.find(query).toArray(function(err, result){
    if(err){
      callback(err);
    } else {
      callback(null, result);
    }
  });
},

exports.get = function(id, callback){
  booking.findOne({'bookingid': parseInt(id)}, function(err, booking) {
    if(err){
      callback(err, null)
    } else {
      callback(null, booking);
    }
  });
},

exports.create = function(payload, callback){
  booking.countDocuments(function(err, count) {
    payload.bookingid = count + 1;
  
    booking.insertOne(payload, function(err, doc) {
      if(err){
        callback(err);
      } else {
        callback(null, payload);
      }
    });
  });
},

exports.update = function(id, updatedBooking, callback){
  booking.updateOne({'bookingid': parseInt(id)}, { $set: updatedBooking }, {}, function(err){
    if(err){
      callback(err);
    } else {
      callback(null);
    }
  });
},

exports.delete = function(id, callback){
  booking.deleteOne({'bookingid': parseInt(id)}, function(err){
    if(err){
      callback(err);
    } else {
      callback(null);
    }
  })
},

exports.deleteAll = function(callback){
  booking.deleteMany({}, function(err){
    callback();
  });
}
