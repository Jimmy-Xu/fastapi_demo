# 配置文件：MongoConfig
from fastapi_plus.utils.mongo import MongoConfig

mongo_config = MongoConfig()
mongo_config.host = ''
mongo_config.port = ''
mongo_config.username = ''
mongo_config.password = ''
mongo_config.database = 'fastapi_demo'
