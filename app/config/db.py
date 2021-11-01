# 配置文件：DbConfig
from fastapi_plus.utils.db import DbConfig

db_config = DbConfig()
db_config.driver = r'sqlite'
db_config.host = ''
db_config.port = ''
db_config.username = ''
db_config.password = ''
db_config.database = r'D:\binance_app\data.db'
db_config.echo = True
