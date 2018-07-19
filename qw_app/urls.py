
from django.contrib import admin
from django.urls import path
from qw_app import views
urlpatterns = [
    path('',views.goHome),
    path('xuanhuan',views.xuanhuan),
    path('liuzhen',views.xiuzhen),
    path('dushi',views.dushi),
    path('lishi',views.lishi),
    path('wangyou',views.wangyou),
    path('kehuan',views.kehuan),
    path('kongbu',views.kongbu),
    path('quanben',views.quanben),
]
