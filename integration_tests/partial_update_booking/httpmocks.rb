<-CLI:PATCH /booking/1 {
	"lastname":"Jones",
	"bookingdates": {
		"checkin":"2018-05-29",
	    "checkout":"2019-01-09"
    }
}
--HEA:Authorization=Basic YWRtaW46cGFzc3dvcmQxMjM=
--HEA:accept=application/json
--HEA:Content-Type=application/json
->SRV:200 {"firstname":"Mary","lastname":"Jones","totalprice":953,"depositpaid":true,"bookingdates":{"checkin":"2018-05-29","checkout":"2019-01-09"}}
--HEA:Content-Type=application/json; charset=utf-8
