<-CLI:GET /booking?checkout=dfdssd
--HEA:accept=application/json
--HEA:Origin=http://localhost:58306
--HEA:Accept-Encoding=gzip, deflate, br
--HEA:Accept-Language=en-GB,en;q=0.9,en-US;q=0.8,sv;q=0.7,de;q=0.6,nb;q=0.5
->SRV:200 [{"bookingid":1}]
--HEA:Content-Type=application/json; charset=utf-8
