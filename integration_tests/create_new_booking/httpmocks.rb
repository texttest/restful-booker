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
--HEA:Content-Type=application/json; charset=utf-8
<-CLI:GET /booking?lastname=Brown
--HEA:accept=application/json
--HEA:Origin=http://localhost:58306
--HEA:Accept-Encoding=gzip, deflate, br
--HEA:Accept-Language=en-GB,en;q=0.9,en-US;q=0.8,sv;q=0.7,de;q=0.6,nb;q=0.5
->SRV:200 [{"bookingid":1},{"bookingid":4}]
--HEA:Content-Type=application/json; charset=utf-8
