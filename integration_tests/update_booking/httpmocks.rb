<-CLI:PUT /booking/1 {
	"firstname":"Mary",
	"lastname":"Jones",
	"totalprice":53,
	"depositpaid":true,
	"bookingdates":{"checkin":"2018-12-31",
	"checkout":"2019-01-09"}
}
--HEA:Authorization=Basic YWRtaW46cGFzc3dvcmQxMjM=
--HEA:accept=application/json
--HEA:Content-Type=application/json
->SRV:200 {"firstname":"Mary","lastname":"Jones","totalprice":53,"depositpaid":true,"bookingdates":{"checkin":"2018-12-31","checkout":"2019-01-09"}}
--HEA:Content-Type=application/json; charset=utf-8
