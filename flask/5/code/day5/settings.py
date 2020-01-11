#数据库配置

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1:3306/day06"
SQLALCHEMY_TRACK_MODIFICATIONS = False


#redis缓存
# 配置
# 缓存类型
CACHE_TYPE = 'redis'
# redis主机
CACHE_REDIS_HOST = '127.0.0.1'
CACHE_REDIS_PORT = 6379
# redis数据库
CACHE_REDIS_DB = 1
