<-CLI:POST /auth {
    "username" : "admin",
    "password" : "wrong"
}
--HEA:accept=application/json
--HEA:Content-Type=application/json
->SRV:200 {"reason":"Bad credentials"}
--HEA:X-Powered-By=Express
--HEA:Content-Type=application/json; charset=utf-8
--HEA:ETag=W/"1c-J3EiwfZwVQjKTKvpvazUfTni8fI"
