<-CLI:POST /booking {
    "firstname": "Geoff",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": true,
    "bookingdates" : {
        "checkin" : "2021-01-01",
        "checkout" : "2021-01-03"
    },
    "additionalneeds": "Breakfast"
}
--HEA:accept=application/json
--HEA:Content-Type=application/json
->SRV:200 {"bookingid":4,"booking":{"firstname":"Geoff","lastname":"Brown","totalprice":111,"depositpaid":true,"bookingdates":{"checkin":"2021-01-01","checkout":"2021-01-03"},"additionalneeds":"Breakfast"}}
--HEA:X-Powered-By=Express
--HEA:Content-Type=application/json; charset=utf-8
--HEA:ETag=W/"c4-WhAG3vEBOUbsC2TKDq/Mh7Xg/o0"
