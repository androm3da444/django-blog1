from django.urls import path, re_path
from .import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name="list"),
    path('create/', views.article_create, name="create"),
    #re_path('(?P<slug>[\w-]+)/$', views.article_detail),
    path('<slug>/', views.article_detail, name="detail"),
]
