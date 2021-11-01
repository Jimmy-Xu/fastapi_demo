# 配置目录

- redis
- tinymongo
- sqlite


## redis for windows

### download
https://github.com/tporadowski/redis/releases/tag/v5.0.14

- 解压后直接运行目录下的 redis-server.exe
- cmd新起一个命令行窗口，切换到redis目录，输入 redis-cli 进入redis命令行，验证安装是否成功。

### auth
> D:\Program Files\Redis\redis.windows-service.conf
```
requirepass 1q2w3e4R
```

### restart service

```
sc stop Redis
sc start Redis
```

### test
```
> .\redis-cli.exe -a 1q2w3e4R
或者
> .\redis-cli.exe
 127.0.0.1:6379> auth 1q2w3e4R
OK

127.0.0.1:6379> config get requirepass
1) "requirepass"
2) "1q2w3e4R"
```

## mysql to sqlite

### sqlite gui
- SQLiteStudio
- SQLiteExpertPersonal
- sqliteadmin

### sqlalchemy + sqlite

```
engine = create_engine(r'D:\binance_app\data.db')
```

### modify DBConfig in fastapi_plug

> .\venv\Lib\site-packages\fastapi_plus\utils\db.py

```
    def get_url(self):
        config = [
            self.driver,
            '://',
            # self.username,
            # ':',
            # self.password,
            # '@',
            # self.host,
            # ':',
            # self.port,
            '/',
            self.database,
            # '?charset=',
            # self.charset,
        ]
        print("connection url={0}".format( ''.join(config)))
        return ''.join(config)
```

## pymongo to tinymongo

### modify MongoConfig in fastapi_plus
> .\venv\Lib\site-packages\fastapi_plus\utils\mongo.py

```
#from pymongo import MongoClient
#from pymongo.collection import Collection

to

from tinymongo import TinyMongoClient as MongoClient
from tinymongo import TinyMongoCollection as Collection


    def get_url(self):
        print("mongo url={0}".format(self.database))
        return self.database
```
