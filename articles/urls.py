from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.main_page, name = 'mainpage'),
    path('articles/', views.index, name = 'index'),
    path('articles/<int:article_id>/', views.detail, name = 'detail'),
    path('articles/<int:article_id>/leave_comment', views.leave_comment, name='leave_comment'),
]
