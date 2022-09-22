<-CLI:POST /auth {
    "username" : "admin",
    "password" : "password123"
}
--HEA:accept=application/json
--HEA:Content-Type=application/json
->SRV:200 {"token":"4f4d8f45017bf84"}
--HEA:Content-Type=application/json; charset=utf-8
