<-CLI:GET /booking/1
--HEA:accept=application/json
->SRV:200 {"firstname":"Mary","lastname":"Brown","totalprice":953,"depositpaid":true,"bookingdates":{"checkin":"2018-12-31","checkout":"2019-05-09"}}
--HEA:Content-Type=application/json; charset=utf-8
