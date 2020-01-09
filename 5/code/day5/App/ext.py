from flask_cache import Cache
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 创建对象
cache = Cache(with_jinja2_ext=False)

