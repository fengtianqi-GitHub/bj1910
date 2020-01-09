import views
# 路由映射表
urlpatterns = [
    (r'^/$',views.index),
    (r'^/login$',views.login),
    (r'^/register$',views.register)
]
