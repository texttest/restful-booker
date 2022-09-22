<-CLI:POST /auth {
    "username" : "admin",
    "password" : "wrong"
}
--HEA:accept=application/json
--HEA:Content-Type=application/json
->SRV:200 {"reason":"Bad credentials"}
--HEA:Content-Type=application/json; charset=utf-8
