# 应用代码目录

## swagger ui

http://127.0.0.1:8000/docs

## postman 

### import api
import http://127.0.0.1:8000/openapi.json

### set environment

baseUrl=http://127.0.0.1:8000


## Test API

### GET:sys_info
```
$ curl --location -s --request GET 'http://127.0.0.1:8000/sys_info'
{"platform":"Windows-10-10.0.17763-SP0","machine":"AMD64","node":"DESKTOP-ECHJN7O","processor":"Intel64 Family 6 Model 58 Stepping 9, GenuineIntel","python_version":"3.9.6"}
```

### POST:login
```
$ curl --location -s --request POST 'http://127.0.0.1:8000/v1/user/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "type": "password",
    "key": "test",
    "password": "123456"
}'
{"token":"130897ad0-3b2f-11ec-ba57-74e54320b56d","user_id":1,"user":{"id":1,"name":"user1"}}

```