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

```
    @staticmethod
    def _create_scoped_session(config: DbConfig):
        engine = create_engine(
            config.get_url(),
            # pool_size=config.pool_size,
            # max_overflow=config.max_overflow,
            # pool_recycle=config.pool_recycle,
            # echo=config.echo
        )
```

## modify dateType in fastapi_plug
.\venv\Lib\site-packages\fastapi_plus\model\base.py
```
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, LONGTEXT, TINYINT
to
from sqlalchemy.dialects.sqlite import DECIMAL, INTEGER, TEXT, SMALLINT

// change all BIGINT to DECIMAL
// change all LONGTEXT to TEXT
// change all TINYINT to SMALLINT
```

full
```
from sqlalchemy import Column, String, TIMESTAMP, text, DECIMAL, Date
from sqlalchemy.dialects.sqlite import DECIMAL, INTEGER, TEXT, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


class Base(DeclarativeBase):
    """
    基础Model模型对象
    """
    __abstract__ = True

    id = Column(DECIMAL(20), primary_key=True, comment='序号')
    parent_id = Column(DECIMAL(20), nullable=False, server_default=text("0"), comment='父序号')
    type = Column(INTEGER, nullable=False, server_default=text("0"), comment='类型')
    sort = Column(INTEGER, nullable=False, server_default=text("0"), comment='排序')
    status = Column(SMALLINT, nullable=False, server_default=text("0"), comment='状态')
    is_deleted = Column(SMALLINT, nullable=False, server_default=text("0"), comment='软删')
    created_by = Column(DECIMAL(20), nullable=False, server_default=text("0"), comment='创建人')
    created_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    updated_by = Column(DECIMAL(20), nullable=False, server_default=text("0"), comment='更新人')
    updated_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='更新时间')
    code = Column(String(255), nullable=False, server_default=text("''"), comment='编码')
    name = Column(String(255), nullable=False, server_default=text("''"), comment='名称')
    label = Column(String(255), nullable=False, server_default=text("''"), comment='标签')
    logo = Column(String(255), nullable=False, server_default=text("''"), comment='图标')
    url = Column(String(255), nullable=False, server_default=text("''"), comment='URL')
    info = Column(String(1000), nullable=False, server_default=text("''"), comment='内容')
    remark = Column(String(1000), nullable=False, server_default=text("''"), comment='备注')
    search = Column(TEXT, comment='搜索')

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


### FAQ

[RecursionError: maximum recursion depth exceeded](https://github.com/schapman1974/tinymongo/issues/58)


## generate db

### user table

```
CREATE TABLE user (
    id           BIGINT (20)    NOT NULL,
    username     CHAR (20)      NOT NULL,
    password     CHAR (20)      NOT NULL,
    parent_id    BIGINT (20),
    type         INTEGER (11),
    sort         INTEGER (11),
    status       TINYINT (2),
    is_deleted   TINYINT (1),
    created_by   BIGINT (20),
    created_time TIMESTAMP,
    updated_by   BIGINT (20),
    updated_time TIMESTAMP,
    code         VARCHAR (255),
    name         VARCHAR (255),
    label        VARCHAR (255),
    logo         VARCHAR (255),
    url          VARCHAR (255),
    info         VARCHAR (1000),
    remark       VARCHAR (1000),
    search       VARCHAR (1000) 
);

```

### insert user data

```
--
-- 由SQLiteStudio v3.3.3 产生的文件 周二 11月 2 00:12:12 2021
--
-- 文本编码：System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- 表：user
DROP TABLE IF EXISTS user;
CREATE TABLE "user"(
  [id] BIGINT(20) NOT NULL,
  [username] CHAR(20) NOT NULL,
  [password] CHAR(20) NOT NULL,
    [parent_id] BIGINT(20), 
    [type] INTEGER(11), 
    [sort] INTEGER(11), 
    [status] TINYINT(2), 
    [is_deleted] TINYINT(1), 
    [created_by] BIGINT(20), 
    [created_time] TIMESTAMP, 
    [updated_by] BIGINT(20), 
    [updated_time] TIMESTAMP, 
    [code] varchar(255), 
    [name] varchar(255), 
    [label] varchar(255), 
    [logo] varchar(255), 
    [url] varchar(255), 
    [info] varchar(1000), 
    [remark] varchar(1000), 
    [search] varchar(1000)
  );
INSERT INTO user (id, username, password, parent_id, type, sort, status, is_deleted, created_by, created_time, updated_by, updated_time, code, name, label, logo, url, info, remark, search) VALUES (1, 'test', 'e290d6c2246a3a45386e72b3c3a5868c', 0, 'password', NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, 'user1', NULL, NULL, NULL, NULL, NULL, NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

```


### generate password

```
> python
>>> import hashlib
>>> name = "user1"
>>> password = "123456"
>>> hashlib.md5((name + password).encode(encoding='UTF-8')).hexdigest()
'e290d6c2246a3a45386e72b3c3a5868c'
```
