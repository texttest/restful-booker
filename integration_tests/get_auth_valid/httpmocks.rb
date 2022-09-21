<-CLI:POST /auth {
    "username" : "admin",
    "password" : "password123"
}
--HEA:accept=application/json
--HEA:Content-Type=application/json
->SRV:200 {"token":"5c7567f702e39d8"}
--HEA:X-Powered-By=Express
--HEA:Content-Type=application/json; charset=utf-8
--HEA:ETag=W/"1b-HJGdPAc/wZ5wx1rD/SYhjygqzT0"
