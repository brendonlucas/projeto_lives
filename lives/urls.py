from django.urls import path
from django.urls import include

from lives import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('/', views.add_fac, name='add_fac'),
    path('fac/<pk>', views.show_live_fac, name='show_live_fac'),
    path('streamer/', views.add_streamer, name='add_streamer'),
    path('delete_canal/<pk>/', views.remove_canal, name='del_canal'),

]
