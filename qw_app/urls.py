from django.urls import path
from qw_app import views

app_name = 'books'
urlpatterns = [
    path('index/', views.goHome, name='index'),
    path('xuanhuan/', views.xuanhuan, name='xuanhuan'),
    path('xiuzhen/', views.xiuzhen, name='xiuzhen'),
    path('dushi/', views.dushi, name='dushi'),
    path('lishi/', views.lishi, name='lishi'),
    path('wangyou/', views.wangyou, name='wangyou'),
    path('kehuan/', views.kehuan, name='kehuan'),
    path('kongbu/', views.kongbu, name='kongbu'),
    path('quanben/', views.quanben, name='quanben'),
    path('shuji/', views.shuji, name="detail"),

]
